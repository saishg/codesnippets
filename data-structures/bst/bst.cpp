#include <iostream>
#include <sstream>

using namespace std;


class Node {
    private:
        int value;
        Node * left;
        Node * right;

    public:
        Node(int value);
        void add(int value);
        void print();
        virtual ~Node();
};

Node::Node(int value) : value(value), left(NULL), right(NULL) {
}

void
Node::add(int value) {
    if (value < this->value) {
        if (this->left)
            this->left->add(value);
        else
            this->left = new Node(value);
    }
    else {
        if (this->right)
            this->right->add(value);
        else
            this->right = new Node(value);
    }
}

void
Node::print() {
    if (left)
        left->print();

    cout << value << endl;

    if (right)
        right->print();
}

Node::~Node() {
    delete left;
    delete right;
    left = NULL;
    right = NULL;
}

int main() {
    Node * root = new Node(50);
    root->add(25);
    root->add(75);
    root->add(12);
    root->add(49);
    root->add(51);
    root->add(100);
    root->add(82);
    root->add(37);
    root->add(60);
    root->print();
    delete root;

}
