#include <list>
#include <iostream>

using namespace std;


int main() {
    list<int> mylist;
    mylist.push_back(1);
    mylist.push_back(2);
    mylist.push_back(3);
    mylist.push_back(4);
    mylist.push_back(5);

    cout << "first " << mylist.front() << endl;
    cout << "last " << mylist.back() << endl;

    for (list<int>::iterator i = mylist.begin();
         i != mylist.end(); i++)
        cout << *i << endl;
}
