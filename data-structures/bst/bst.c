#include <stdio.h>
#include <stdlib.h>

typedef struct _Node {
    int value;
    struct _Node *left;
    struct _Node *right;
} Node;

Node * add(Node *node, int value) {
    if (node == NULL) {
        Node *newNode = malloc(sizeof(Node));
        newNode->value = value;
        newNode->left = NULL;
        newNode->right = NULL;
        return newNode;
    }

    if (value < node->value) {
        node->left = add(node->left, value);
        return node;
    }
    else {
        node->right = add(node->right, value);
        return node;
    }
}

void print(Node *node) {
    if (node == NULL)
        return;
    print(node->left);
    printf("%d\n", node->value);
    print(node->right);
}

void delete(Node *node) {
    if (node == NULL)
        return;

    delete(node->left);
    delete(node->right);
    free(node);
}


int main() {
    Node *root = add(NULL, 50);
    add(root, 25);
    add(root, 75);
    add(root, 12);
    add(root, 49);
    add(root, 51);
    add(root, 100);
    add(root, 82);
    add(root, 37);
    add(root, 60);
    print(root);
    delete(root);
}
