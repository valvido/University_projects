#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

//protokol
#define STRANKA_ZAHJEV 1
#define SLUZBENIK_ZAHJEV 2

//Klijent mora program pozvati sa ./bank-client2 161.53.8.14 13 kunsko_poslovanje
int main( int argc, char **argv )
{
    if (argc != 4) {
        printf("Upotreba: %s ip-adresa port vrsta_posla\n", argv[0]);
        exit(0);
    }

	// socket...
	int clientSocket = socket( PF_INET, SOCK_STREAM, 0 );
	if( clientSocket == -1 )
   		perror( "socket" );

	// dohvati IP-adresu iz 1. argumenta komandne linije
	char dekadskiIP[ 10 ];
	strcpy( dekadskiIP, argv[1] );

	// dohvati port iz 2. argumenta komandne linije
	int port;
	sscanf( argv[2], "%d", &port );

    // connect...
	struct sockaddr_in adresaServera;

	adresaServera.sin_family = AF_INET;
	adresaServera.sin_port = htons( port );

	if( inet_aton( dekadskiIP, &adresaServera.sin_addr ) == 0 )
		printf( "%s nije dobra adresa!\n", dekadskiIP );

	memset( adresaServera.sin_zero, '\0', 8 );

	if( connect( clientSocket,
	             (struct sockaddr *) &adresaServera,
	             sizeof( adresaServera ) ) == -1 )
		perror( "connect" );

	printf("sluzbenik se spojio\n");

	//slanje serveru vrste zahtjeva
	int vrstaZahtjeva = SLUZBENIK_ZAHJEV;
    send(clientSocket, &vrstaZahtjeva, sizeof(vrstaZahtjeva), 0);
	printf("Sluzbenik je poslao vrstu posla\n");

    //slanje serveru vrste posla
    char *vrstaPosla = argv[3];
    send(clientSocket, vrstaPosla, strlen(vrstaPosla), 0);

    //Server vraća broj stranke koja je na redu za tu vrstu posla i koju službenik treba pozvati da priđe šalteru.
    int clientNumber;
    recv(clientSocket, &clientNumber, sizeof(clientNumber), 0);
	if(clientNumber==0){
		printf("Nema stranki u redu, sluzbenik odustaje od posla\n");
		return 0;
	}
	
	printf("Broj stranke koja je na redu: %d\n", clientNumber);

    close(clientSocket);
    return 0;
}