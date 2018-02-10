#include <map>
#include <iostream>

using namespace std;

int main() {
    map<string, int> table;
    table["one"] = 1;
    table["two"] = 2;
    table["three"] = 3;
    table["four"] = 4;

    for (map<string, int>::iterator i = table.begin(); i != table.end(); i++) {
        cout << i->first << ":" << i->second << endl;
    }

    table["ten"] = 10;
    cout << table["ten"] << endl;
}
