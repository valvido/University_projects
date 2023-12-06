#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>

using namespace std;


int main() {
    string line;
    while (getline(cin, line)) {
        int hrk_index = line.find("HRK");
        if(isdigit(line[hrk_index - 1])){
            int price_end_pos = hrk_index - 1;
            int price_start_index = price_end_pos;
            while (price_end_pos >= 0 && (isdigit(line[price_end_pos]) || line[price_end_pos] == '.')) {
                --price_start_index;
            }
            
        }
    }

    return 0;
}
