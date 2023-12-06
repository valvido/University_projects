#include "Graf.h"

Graf::Graf() : br_vrhova(0), bridovi(nullptr) {}

Graf::Graf(int n) : br_vrhova(n), bridovi(new int*[n]) {
    for (int i = 0; i < n; ++i) {
        bridovi[i] = new int[n];
        for (int j = 0; j < n; ++j) {
            bridovi[i][j] = (i == j) ? 0 : std::numeric_limits<int>::max();
        }
    }
}

Graf::Graf(std::ifstream& datoteka) {
    ucitaj_graf_iz_datoteke(datoteka);
}

Graf::Graf(const Graf& drugi) {
    kopiraj_graf(drugi);
}

Graf::Graf(Graf&& drugi) noexcept {
    premjesti_graf(drugi);
}

Graf::~Graf() {
    obrisi_graf();
}

Graf& Graf::operator=(const Graf& drugi) {
    if (this != &drugi) {
        obrisi_graf();
        kopiraj_graf(drugi);
    }
    return *this;
}

Graf& Graf::operator=(Graf&& drugi) noexcept {
    if (this != &drugi) {
        obrisi_graf();
        premjesti_graf(drugi);
    }
    return *this;
}

Graf& Graf::ispis() {
    for (int i = 0; i < br_vrhova; ++i) {
        for (int j = 0; j < br_vrhova; ++j) {
            if (bridovi[i][j] != std::numeric_limits<int>::max() && bridovi[i][j]!=0) {
                std::cout << "(" << i << "," << j << ") = " << bridovi[i][j] << std::endl;
            }
        }
    }
    return *this;
}

bool Graf::ima_vrh(int a) const {
    return (a >= 0 && a < br_vrhova);
}

Graf& Graf::optimalni(int a, int b) {
    std::vector<int> put;
    int cijena;
    if (bellman_ford(a, b, put, cijena)) {
        std::cout << "Cijena optimalanog puta od vrha "<< a << " do vrha "<< b <<" je "<< cijena << std::endl;
        std::cout<<"Ispis optimalnog puta (unatrag):"<<std::endl;
        for (const auto& vrh : put) {
            std::cout<<" " << vrh << " ";
        }
        std::cout << std::endl;
    } else {
        std::cout << "Nema puta od vrha "<< a <<" do vrha "<< b << std::endl;
    }
    return *this;
}

void Graf::ucitaj_graf_iz_datoteke(std::ifstream& datoteka) {
    if (datoteka) {
        int n;
        datoteka >> n;
        br_vrhova = n;
        bridovi = new int*[n];
        for (int i = 0; i < n; ++i) {
            bridovi[i] = new int[n];
            for (int j = 0; j < n; ++j) {
                bridovi[i][j] = (i == j) ? 0 : std::numeric_limits<int>::max();
            }
        }

        int a, b, cijena;
        while (datoteka >> a >> b >> cijena) {
            bridovi[a][b] = cijena;
        }
    }
}

void Graf::kopiraj_graf(const Graf& drugi) {
    br_vrhova = drugi.br_vrhova;
    bridovi = new int*[br_vrhova];
    for (int i = 0; i < br_vrhova; ++i) {
        bridovi[i] = new int[br_vrhova];
        for (int j = 0; j < br_vrhova; ++j) {
            bridovi[i][j] = drugi.bridovi[i][j];
        }
    }
}

void Graf::premjesti_graf(Graf& drugi) noexcept {
    br_vrhova = drugi.br_vrhova;
    bridovi = drugi.bridovi;
    drugi.br_vrhova = 0;
    drugi.bridovi = nullptr;
}

void Graf::obrisi_graf() {
    for (int i = 0; i < br_vrhova; ++i) {
        delete[] 
        bridovi[i];
    }
    delete[] 
    bridovi;
    br_vrhova = 0;
    bridovi = nullptr;
}

bool Graf::bellman_ford(int a, int b, std::vector<int>& put, int& cijena) const {
std::vector<int> udaljenost(br_vrhova, std::numeric_limits<int>::max());
std::vector<int> prethodnik(br_vrhova, -1);
udaljenost[a] = 0;

for (int i = 0; i < br_vrhova - 1; ++i) {
    for (int j = 0; j < br_vrhova; ++j) {
        for (int k = 0; k < br_vrhova; ++k) {
            if (bridovi[j][k] != std::numeric_limits<int>::max() &&
                udaljenost[j] != std::numeric_limits<int>::max() &&
                udaljenost[j] + bridovi[j][k] < udaljenost[k]) {
                udaljenost[k] = udaljenost[j] + bridovi[j][k];
                prethodnik[k] = j;
            }
        }
    }
}

for (int j = 0; j < br_vrhova; ++j) {
    for (int k = 0; k < br_vrhova; ++k) {
        if (bridovi[j][k] != std::numeric_limits<int>::max() &&
            udaljenost[j] != std::numeric_limits<int>::max() &&
            udaljenost[j] + bridovi[j][k] < udaljenost[k]) {
            std::cout << "Postoji negativan ciklus!" << std::endl;
            return false;
        }
    }
}

if (udaljenost[b] != std::numeric_limits<int>::max()) {
    cijena = udaljenost[b];
    int trenutni = b;
    while (trenutni != a) {
        put.push_back(trenutni);
        trenutni = prethodnik[trenutni];
    }
    put.push_back(a);
    return true;
} else {
    return false;
}

}
