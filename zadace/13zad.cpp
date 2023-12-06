#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main (void){

    string amino = "ARNDCQEGHILKMFPSTWYV";
    string line;

    ifstream myfile ("proteom.txt");
    ofstream rezultat ("rezultat.txt");

    vector<int> temp;



    getline (myfile, line);
    if (myfile.is_open()){
        while ( getline (myfile,line)){
            for (int i = 0; i < amino.size(); i++){     //prolazimo po aminokiselinama
                for (int j = 0; j < line.size(); j++){//prolazimo po liniji proteoma
                    if (amino[i] == line[j])
                       temp.push_back (j+1);
                }
                rezultat << amino [i] << " ";
                for (int j = 0; j < temp.size(); j++)
                    rezultat << temp[j] << " ";
                temp.clear();
                rezultat << endl;
            }
        }
        myfile.close();
        rezultat.close();
    }

    else cout << "Unable to open file!" << endl;

    return 0;
}
