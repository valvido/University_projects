//kad se spajam  u praktikumu moram 
//ssh username@remote_host - spajanje na racunalo student
//ftp - filetransportprotocol -> koristi sftp
//sftp login@imeUdaljenogRacunala
//sftp login@imeUdaljenogRacunala 
//dok koristim lokalno racunalo samo ispred svih naredbi ide l
// put imeDatoteke
//student.math.hr



#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

#include <pthread.h>

#define MAX_CLIENTS 10
#define MAX_VRSTA_POSLA 50
#define MAXDRETVI 10

//protokol
#define STRANKA_ZAHJEV 1
#define SLUZBENIK_ZAHJEV 2

int aktivneDretve[MAXDRETVI] = { 0 };
char poslovi[MAXDRETVI][100];
int brojListica=0;


typedef struct
{
	int commSocket;
	int indexDretve;
} obradiKlijenta__parametar;

obradiKlijenta__parametar parametarDretve[MAXDRETVI];
pthread_mutex_t lokot_aktivneDretve = PTHREAD_MUTEX_INITIALIZER;

void *obradiStranku( void *parametar ){
	obradiKlijenta__parametar *param = (obradiKlijenta__parametar *) parametar;
	int commSocket  = param->commSocket;
	int indexDretve = param->indexDretve;

	//spremi posao koji treba obaviti stranka
	char vrstaPosla[100];
    recv(param->commSocket, vrstaPosla, sizeof(vrstaPosla), 0);

	pthread_mutex_lock(&lokot_aktivneDretve);
	strcpy(poslovi[brojListica], vrstaPosla);
	brojListica++; //broj stranke u redu je jednak brojListica-1, tj. ako se podudara posao sa sluzbenikom broj stranke je index niza + 1

	printf("%d. stranka na redu treba obaviti %s\n",brojListica, poslovi[brojListica-1]);

	send(param->commSocket, &brojListica, sizeof(brojListica), 0);
	pthread_mutex_unlock(&lokot_aktivneDretve);

	close(param->commSocket);

	return 0;
}

void *obradiSluzbenika(void *parametar) {
    obradiKlijenta__parametar *param = (obradiKlijenta__parametar *) parametar;
	int commSocket  = param->commSocket;
	int indexDretve = param->indexDretve;

	char vrstaPosla[100];
    recv(param->commSocket, vrstaPosla, sizeof(vrstaPosla), 0);
	

	pthread_mutex_lock(&lokot_aktivneDretve);
	int i;
	for( i=0; i<brojListica;i++){
		if(strcmp(poslovi[i], vrstaPosla) == 0){
			//saljemo broj odgovarajuce stranke sluzbeniku
			int brojOdgovarajuceStranke = i+1;
			send(param->commSocket, &(brojOdgovarajuceStranke), sizeof(brojOdgovarajuceStranke), 0);

			//brisemo tog korisnika iz reda
		int j;
    	for (j = i; j < brojListica - 1; j++) {
    	    // Kopiramo sljedeći element na mjesto trenutnog
    	    memmove(poslovi[j], poslovi[j + 1], sizeof(poslovi[j + 1]));
    	}
		brojListica--;
		}
	}

	pthread_mutex_unlock(&lokot_aktivneDretve);
	return 0;
}	



//korisnik upisuje (IP adresu i) port
int main( int argc, char **argv )
{
	if( argc != 2 )
	{
		printf( "Upotreba: %s port\n", argv[0] );
		exit( 0 );
	}

	int port;
	sscanf( argv[1], "%d", &port );

	// socket...
	int listenerSocket = socket( PF_INET, SOCK_STREAM, 0 );
	if( listenerSocket == -1 )
	    perror( "socket" );

	// bind...
	struct sockaddr_in mojaAdresa;

	mojaAdresa.sin_family      = AF_INET;
	mojaAdresa.sin_port        = htons( port );
	mojaAdresa.sin_addr.s_addr = INADDR_ANY;
	memset( mojaAdresa.sin_zero, '\0', 8 );

	if( bind(
			listenerSocket,
			(struct sockaddr *) &mojaAdresa,
			sizeof( mojaAdresa ) ) == -1 )
		perror( "bind" );

	// listen...
	if( listen( listenerSocket, 10 ) == -1 )
		perror( "listen" );

    //kreiranje threadova u kojima ce se obradivati zahtjevi klijenata
    pthread_t dretve[10];
	

	while (1) {
       // accept...
		struct sockaddr_in klijentAdresa;
		int lenAddr = sizeof( klijentAdresa );
		int commSocket = accept( listenerSocket,
                         (struct sockaddr *) &klijentAdresa,&lenAddr );
                         
		if( commSocket == -1 )
			perror( "accept" );

		char *dekadskiIP = inet_ntoa( klijentAdresa.sin_addr );
		printf( "Prihvatio konekciju od %s ", dekadskiIP );

		int vrstaZahtjeva;
    	recv(commSocket, &vrstaZahtjeva, sizeof(vrstaZahtjeva), 0);
		printf("server je primio vrstu zahtjeva\n");
		
		pthread_mutex_lock( &lokot_aktivneDretve );
		int i, indexNeaktivne = -1;
		for( i = 0; i < MAXDRETVI; ++i )
			if( aktivneDretve[i] == 0 )
				indexNeaktivne = i;
			else if( aktivneDretve[i] == 2 )
			{
				pthread_join( dretve[i], NULL );
				aktivneDretve[i] = 0;
				indexNeaktivne = i;
			}
			    
		if( indexNeaktivne == -1 )
		{
			close( commSocket ); // nemam vise dretvi...
			printf( "--> ipak odbijam konekciju jer nemam vise dretvi.\n" );
		}
		else
		{
		    aktivneDretve[indexNeaktivne] = 1;
			parametarDretve[indexNeaktivne].commSocket = commSocket;
			parametarDretve[indexNeaktivne].indexDretve = indexNeaktivne;
			printf( "--> koristim dretvu broj %d.\n", indexNeaktivne );

		
			printf("%d", vrstaZahtjeva);
			
			if(vrstaZahtjeva == SLUZBENIK_ZAHJEV){
				if(brojListica==0){
				printf("Nema stranki na cekanju, ne mogu pozvati sluzbenika.");
				send(commSocket, &brojListica, sizeof(brojListica), 0);
				return 0;
				}
				printf("Obradujem sluzbenika");
				pthread_create(
				&dretve[indexNeaktivne], NULL,
				obradiSluzbenika, &parametarDretve[indexNeaktivne] );
			}else if(vrstaZahtjeva == STRANKA_ZAHJEV){
				pthread_create(
				&dretve[indexNeaktivne], NULL,
				obradiStranku, &parametarDretve[indexNeaktivne] );
				printf("obradujem stranku\n");
			}
			
		}
		pthread_mutex_unlock( &lokot_aktivneDretve );
	}

	int j;
	 for (j = 0; j < MAXDRETVI; ++j)
    {
        if (aktivneDretve[j] == 1)
        {
            pthread_join(dretve[j], NULL);
            aktivneDretve[j] = 0;
        }
    }

	return 0;
}
