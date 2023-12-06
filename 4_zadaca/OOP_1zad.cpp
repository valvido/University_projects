#include <iostream>
#include <stack>
#include <string>

using namespace std;

bool is_valid_expression(string expr) {
    stack<char> s;

    for (int i = 0; i < expr.length(); i++) {
        char c = expr[i];

        if (c == '(' || c == '[' || c == '{') {
            s.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            if (s.empty()) {
                return false;
            } else if (c == ')' && s.top() == '(') {
                s.pop();
            } else if (c == ']' && s.top() == '[') {
                s.pop();
            } else if (c == '}' && s.top() == '{') {
                s.pop();
            } else {
                return false;
            }
        }
    }

    return s.empty();
}

int main(){
    string expr;
    cout<<"Upisite aritmeticki izraz:"<<endl;
    getline(cin, expr);

    if (is_valid_expression(expr)) {
        cout << "ISPRAVNO" << endl;
    } else {
        cout << "NIJE ISPRAVNO" << endl;
    }

    return 0;
}
