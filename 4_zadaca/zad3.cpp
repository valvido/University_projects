#include <iostream>
#include <string>
#include <deque>
#include <map>

using namespace std;

int main() {
    deque<string> words;
    map<string, int> freq;

    string word;
    while (cin >> word) {
        words.push_front(word);
        freq[word]++;
    }

    for (auto it = words.begin(); it != words.end(); ++it) {
        cout << *it << " " << freq[*it] << endl;
    }

    return 0;
}
