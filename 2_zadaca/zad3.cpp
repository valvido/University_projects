#include <iostream>
#include <vector>
#include <tuple>
#include <string>
#include <sstream>
#include <limits>
#include<fstream>

using namespace std;

typedef tuple<string, int, string, double> proizvod;

proizvod najjeftiniji(vector<proizvod> &unos, const string &naziv){
    proizvod najjeftiniji_proizvod;
    double min_cijena=get<3>(*(unos.cbegin()))/ (get<1>(*(unos.cbegin())) / 1000.0);
    for (const auto &p : unos) {
        if (get<0>(p) == naziv) {
            double cijena_po_kg = get<3>(p) / (get<1>(p) / 1000.0);
            if (cijena_po_kg < min_cijena) {
                min_cijena = cijena_po_kg;
                najjeftiniji_proizvod = p;
            }
        }
    }
    return najjeftiniji_proizvod;
}


int main(){
    ifstream file("proizvodi.txt");
    vector<proizvod> proizvodi;
    
    if (!file.is_open()) {
        cout << "Datoteka 'proizvodi.txt' nije pronađena!" << endl;
        return 1;
    }
    string line;
    while(getline(file, line)){
        stringstream ss(line);
        string naziv_proizvoda, proizvodjac, gramaza_str, cijena_str;
        int gramaza;
        double cijena;
        proizvod temp;

        getline(ss, naziv_proizvoda, ';');
        getline(ss, gramaza_str, 'g');
        ss.ignore(2, ';');
        getline(ss, proizvodjac, ';');
        getline(ss, cijena_str, 'E');

        gramaza=stoi(gramaza_str);
        cijena=stod(cijena_str);

        
        proizvodi.push_back(make_tuple(naziv_proizvoda, gramaza, proizvodjac,cijena));

    }

    string trazeni_naziv;
    cout << "Unesite naziv proizvoda: ";
    cin>>trazeni_naziv;
    int postoji=0;

    for(auto it=proizvodi.cbegin(); it!=proizvodi.cend();it++){
        if(trazeni_naziv==get<0>(*it))
            postoji = 1;

    }
    proizvod rezultat = najjeftiniji(proizvodi, trazeni_naziv);

    if (!postoji) {
        cout << "Ne postoji proizvod s tim nazivom." << endl;
    } else {
        cout << "Naziv: " << get<0>(rezultat) << endl;
        cout << "Gramaza: " << get<1>(rezultat) << " g" << endl;
        cout << "Proizvodi: " << get<2>(rezultat) << endl;
        cout << "Cijena: " << get<3>(rezultat) << " EUR" << endl;
    }

    file.close();

}