#include <iostream>

using namespace std;

#define DEBUG


template <class T>
class Vector {
    private:
        T* array;
        int array_capacity;
        int array_size;
        static const int initial_size = 1;
        void resize(int new_capacity);

    public:
        Vector();
        Vector(const Vector& other);
        ~Vector();
        void print();
        int size(); // number of items
        int capacity(); // number of items it can hold
        bool is_empty();
        T at(int index); // returns item at index, blows up if index out of bounds
        void push(T item);
        T pop(); // pops last item
};

template <class T>
Vector<T>::Vector() :
        array_capacity(initial_size), array_size(0) {
    array = new T[array_capacity];
}

template <class T>
Vector<T>::Vector(const Vector& other) :
        array_capacity(other.array_capacity), array_size(other.array_size) {

    if (&other != this) {
        array = new T[array_capacity];
        memcpy(array, other.array, sizeof(T) * array_capacity);
    }
}

template <class T>
Vector<T>::~Vector() {
    delete[] array;
}

template <class T>
void
Vector<T>::print() {
    cout << "Array of size " << array_size << ", and capacity " << array_capacity << endl;
    for (int i = 0; i < array_size; i++) {
        cout << array[i] << endl;
    }
}

template <class T>
int
Vector<T>::size() {
    return array_size;
}


template <class T>
int
Vector<T>::capacity() {
    return array_capacity;
}

template <class T>
bool
Vector<T>::is_empty() {
    if (NULL == array)
        return true;
    return (NULL == array_size);
}

template <class T>
T
Vector<T>::at(int index) {
    if (index >= array_size)
        throw "out of bounds";
    else
        return array[index];
}

template <class T>
void
Vector<T>::resize(int new_capacity) {
    T* temp_array = new T[array_capacity];
#ifdef DEBUG
    cout << "resizing to size "  << new_capacity << endl;
#endif
    memcpy(temp_array, array, sizeof(T) * array_capacity);
    delete[] array;
    array = temp_array;
    array_capacity = new_capacity;
}

template <class T>
void
Vector<T>::push(T item) {
    if (array_capacity <= array_size)
        resize(array_capacity * 2);

    array[array_size++] = item;
}

template <class T>
T
Vector<T>::pop() {
    if (array_size > 0) {
        T result = array[--array_size];

        if (array_size <= array_capacity/4)
            resize(array_capacity / 2);

        return result;
    }
    else
        throw "out of bounds";
}



int main() {
    Vector<int> test;
    test.push(1);
    test.push(2);
    test.push(3);
    test.push(4);
    test.push(5);
    test.push(6);
    test.push(7);
    test.push(8);
    test.push(9);
    test.print();
    cout << test.pop() << " popped" << endl;
    Vector<int> test2 = test;
    test2.print();
    cout << test.pop() << " popped" << endl;
    cout << test.pop() << " popped" << endl;
    cout << test.pop() << " popped" << endl;
    cout << test.pop() << " popped" << endl;
    cout << test.pop() << " popped" << endl;
    cout << test.pop() << " popped" << endl;
    cout << test.pop() << " popped" << endl;
    cout << test.pop() << " popped" << endl;
}
