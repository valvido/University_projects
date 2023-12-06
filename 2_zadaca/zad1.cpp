#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

using namespace std;

struct Natjecatelj {
    string sifra;
    int bodovi[5];
    string ime_i_prezime;
};

void ucitajNatjecatelje(const string &datoteka, unordered_map<string, Natjecatelj> &natjecatelji) {
    ifstream ulaz(datoteka);

    if (!ulaz) {
        cerr << "Ne moze se otvoriti datoteka: " << datoteka << endl;
        exit(1);
    }

    Natjecatelj temp;
    while (ulaz >> temp.sifra >> temp.bodovi[0] >> temp.bodovi[1] >> temp.bodovi[2] >> temp.bodovi[3] >> temp.bodovi[4]) {
        ulaz.ignore();
        getline(ulaz, temp.ime_i_prezime);
        natjecatelji[temp.sifra] = temp;

    }

    ulaz.close();
}

void ispisiPretince(const unordered_map<string, Natjecatelj> &natjecatelji) {
    for (const auto &par : natjecatelji) {
        cout << "Pretinac: " << par.first << endl;
        cout << "Natjecatelj: " << par.second.ime_i_prezime << endl;
    }
}

int main() {
    unordered_map<string, Natjecatelj> natjecatelji;
    ucitajNatjecatelje("rezultati.txt", natjecatelji);
    ispisiPretince(natjecatelji);

    string sifra;
    cout << "Unesite sifru natjecatelja: ";
    cin >> sifra;

    if (natjecatelji.find(sifra) != natjecatelji.end()) {
        Natjecatelj &natjecatelj = natjecatelji[sifra];
        for (int i = 0; i < 5; ++i) {
            cout << "Bodovi na " << i + 1 << ". zadatku: " << natjecatelj.bodovi[i] << endl;
        }
        cout << "Ime i prezime: " << natjecatelj.ime_i_prezime << endl;
    } else {
        cout << "Nema natjecatelja s tom sifrom." << endl;
    }

    return 0;
}

//pitati treba li defnirati vlastitu hash funckiju ili se pod to da
// sami odaberemo koju cemo fukciju koristiti misli da mozemo odabrati 
//internu hash funkciju za unordered map
