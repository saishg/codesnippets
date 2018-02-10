// Write a c++ function that takes a string and returns true if the string can
// be converted into palindrome by just shuffling the positions of the chars in
// the string. Otherwise it should return false

#include <iostream>
#include <map>

using namespace std;

bool is_anagram_of_palindrome(string str) {
    map<char, int> myMap;

    for (string::const_iterator it = str.begin(); it != str.end(); ++it) {
        myMap[*it] = (myMap[*it] + 1) % 2;
    }

    int count = 0;

    for (map<char, int>::const_iterator it = myMap.begin(); it != myMap.end(); ++it) {
        count += it->second;
    }

    return (count < 2);
}

int main() {
    cout << is_anagram_of_palindrome("abcba") << endl;
    cout << is_anagram_of_palindrome("aabcbaa") << endl;
    cout << is_anagram_of_palindrome("aabbaa") << endl;
    cout << is_anagram_of_palindrome("aaaabbcccdef") << endl;
}

