#include <stack>
#include <iostream>

using namespace std;

void sortedInsert(stack<int>& myStack, int value) {
    if (myStack.empty() || value <= myStack.top() ) {
        myStack.push(value);
        return;
    }

    int tmp = myStack.top();
    myStack.pop();
    sortedInsert(myStack, value);
    myStack.push(tmp);
}

void sort(stack<int>& myStack) {
    if (myStack.empty())
        return;

    int value = myStack.top();
    myStack.pop();
    sort(myStack);
    sortedInsert(myStack, value);
}

void sortWithTemp(stack<int>& myStack) {
    stack<int> tmpStack;

    while (!myStack.empty()) {
        int value = myStack.top();
        myStack.pop();

        while (!tmpStack.empty() && tmpStack.top() >= value) {
            myStack.push(tmpStack.top());
            tmpStack.pop();
        }

        tmpStack.push(value);
    }


    while (!tmpStack.empty()) {
        myStack.push(tmpStack.top());
        tmpStack.pop();
    }
}

// Function to insert at bottom, recursive
void insertAtBottom(stack<int>& myStack, int value) {
    if (myStack.empty()) {
        myStack.push(value);
        return;
    }

    int tmp = myStack.top();
    myStack.pop();
    insertAtBottom(myStack, value);
    myStack.push(tmp);
}

// Function to invert, uses "insertAtBottom"
void invert(stack<int>& myStack) {
    int value = myStack.top();
    myStack.pop();

    if (!myStack.empty()) {
        invert(myStack);
    }
    insertAtBottom(myStack, value);
}

void print(stack<int>& myStack) {
    while (!myStack.empty()) {
        cout << myStack.top() << endl;
        myStack.pop();
    }
}

int main() {
    stack<int> myStack;
    myStack.push(9);
    myStack.push(3);
    myStack.push(13);
    myStack.push(2);
    myStack.push(1);
    myStack.push(4);
    myStack.push(6);

//    invert(myStack);
//    sortedInsert(myStack, 0);
    sortWithTemp(myStack);

    print(myStack);
}
