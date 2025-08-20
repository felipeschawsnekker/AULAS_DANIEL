#include <iostream>
#include <string>
using namespace std;

int main() {
    string nome;
    getline(cin, nome);

    bool primeira = true;

    for (int i = 0; i < nome.length(); i++) {
        if ((i == 0 || nome[i-1] == ' ') && nome[i] != ' ') {
            if (!primeira) cout << ".";
            cout << (char)toupper(nome[i]);
            primeira = false;
        }
    }

    cout << endl;
    return 0;
}
