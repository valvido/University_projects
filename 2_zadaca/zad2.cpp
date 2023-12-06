#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

map<string, vector<double> > ucitajKolegij(const string &ime_datoteke) {
    map<string, vector<double> > rezultati;
    ifstream ulaz(ime_datoteke + ".txt");
    string JMBAG;
    double ocjena;

    if (ulaz) {
        while (ulaz >> JMBAG) {
            vector<double> ocjene;
            while (ulaz.peek() != '\n' && ulaz >> ocjena) {
                ocjene.push_back(ocjena);
            }
            rezultati[JMBAG] = ocjene;
        }
        ulaz.close();
    }

    return rezultati;
}

double izracunajProsjek(const vector<double> &ocjene) {
    if (ocjene.empty()) {
        return -1.0;
    }
    double suma = 0;
    for (double ocjena : ocjene) {
        suma += ocjena;
    }
    return suma / ocjene.size();
}

int main(int argc, char *argv[]) {
    map<string, map<string, vector<double> > > sveOcjene;
    map<string, vector<string> > JMBAGovi;

    for (int i = 1; i < argc; ++i) {
        string kolegij(argv[i]);
        auto rezultati = ucitajKolegij(kolegij);
        for (const auto &[JMBAG, ocjene] : rezultati) {
            sveOcjene[kolegij][JMBAG] = ocjene;
            JMBAGovi[JMBAG].push_back(kolegij);
        }
    }

    ofstream izvjestaj("izvjestaj.txt");

    izvjestaj << setw(15) << "";
    for (int i = 1; i < argc; ++i) {
        izvjestaj << setw(10) << argv[i];
    }
    izvjestaj << endl;

    for (const auto &[JMBAG, kolegiji] : JMBAGovi) {
        izvjestaj << setw(15) << JMBAG;
        for (int i = 1; i < argc; ++i) {
            string kolegij(argv[i]);
            double prosjek = izracunajProsjek(sveOcjene[kolegij][JMBAG]);
            if (prosjek < 0) {
                izvjestaj << setw(10) << "-";
            } else {
                izvjestaj << setw(10) << fixed << setprecision(2) << prosjek;
            }
        }
        izvjestaj << endl;
    }

    izvjestaj.close();

    return 0;
}
