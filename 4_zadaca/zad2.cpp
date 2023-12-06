#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> numbers;
    int num;

    while (cin >> num) {
        if (num >= 0 && num <= 1000) {
            numbers.insert(lower_bound(numbers.begin(), numbers.end(), num, greater<int>()), num);
        }
    }


    vector<int>::reverse_iterator it = numbers.rbegin();
    int start = 0, end = 1000;
    bool interval_found = false;

    it=numbers.rbegin();
    if (it != numbers.rend() && *it < 1000) {
        if(*it>1)
            cout<<"[0,"<<(*it)-1<<"]"<<endl;
        start = (*it) + 1;
        it++;
    }

    while (it != numbers.rend()) {
        if (start < *it) {
            interval_found = true;
            end = (*it) - 1;
            cout << "[" << start << "," << end << "]" << endl;
        }
        start = *it + 1;
        it++;
    }

    if (*(it--) < 999) {
        cout << "["<< *it+1 <<",1000]"<< endl;
    }

    return 0;
}
