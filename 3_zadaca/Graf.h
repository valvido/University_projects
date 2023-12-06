#ifndef GRAF_H
#define GRAF_H

#include <iostream>
#include <map>
#include <vector>
#include <limits>
#include <fstream>

class Graf {
public:
    typedef int vrh;
    Graf();
    Graf(int n);
    Graf(std::ifstream& datoteka);
    Graf(const Graf& drugi);
    Graf(Graf&& drugi) noexcept;
    ~Graf();

    Graf& operator=(const Graf& drugi);
    Graf& operator=(Graf&& drugi) noexcept;

    Graf& ispis();
    bool ima_vrh(int a) const;
    Graf& optimalni(int a, int b);

private:
    int br_vrhova;
    int** bridovi;

    void ucitaj_graf_iz_datoteke(std::ifstream& datoteka);
    void kopiraj_graf(const Graf& drugi);
    void premjesti_graf(Graf& drugi) noexcept;
    void obrisi_graf();
    bool bellman_ford(int a, int b, std::vector<int>& put, int& cijena) const;
};

#endif
