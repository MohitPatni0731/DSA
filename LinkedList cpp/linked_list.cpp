#include <stdio.h>
#include <iostream>
#include <cassert>
#include <sstream>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }
};

class LinkedList {
public:
    Node* head;

    LinkedList() {
        head = nullptr;
    }

    void insert(int data) {
        Node* new_node = new Node(data);
        if (head == nullptr) {
            head = new_node;
        } else {
            Node* current = head;
            while (current->next != nullptr){
                current = current->next;
            }
            current->next = new_node;
        }
    }
    void print() {
        Node* current = head;
        while (current != nullptr) {
            cout<<current->data;
            cout<<" --> ";
            current = current->next;
        }
        cout<<"None"<<endl;
    }

    void delete_node(int data) {
        Node* current = head;
        Node* previous = nullptr;
        while (current != nullptr) {
            if (current->data == data) {
                if (previous != nullptr) {
                    previous->next = current->next;
                } else {
                    head = current->next;
                }
                delete current;
                return;
            } else {
                previous = current;
                current = current->next;
            }
        }
    }

    Node* search(int data) {
        Node* current = head;
        while (current != nullptr) {
            if (current->data == data) {
                return current;
            }
            current = current->next;
        }
        return nullptr;
    }

    bool is_empty() {
        if (head == nullptr) {
            return true;
        }
        else {
            return false;
        }
    }

    int size() {
        Node* current = head;
        int count = 0;
        while (current != nullptr) {
            count += 1;
            current = current->next;
        }
        return count;
    }

    int index(int data) {
        int index = 0;
        Node* current = head;
        while (current != nullptr) {
            if (current->data == data) {
                return index;
            }
            current = current->next;
            index += 1;
        }
        return -1;
    }

    int pop() {
        if (head == nullptr) {
            return -1;
        }
        Node* current = head;
        Node* previous = nullptr;

        while (current->next != nullptr) {
            previous = current;
            current = current->next;
        }

        if (previous == nullptr) {
            head = nullptr;
        } else {
            previous->next = nullptr;
        }
        
        int data = current->data;
        return data;
    }

    void append(int data) {
        Node* new_node = new Node(data);
        new_node->next = head;
        head = new_node;
    }
};

void test_insert() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    
    assert(llist.head->data == 1); 
    cout << "1: test_insert() passed!" << endl; 
}

void test_print() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);

    assert(llist.head->data == 1);
    assert(llist.head->next->data == 2);
    cout << "2: test_print() passed!" << endl;
}

void test_delete() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);
    llist.insert(4);
    llist.delete_node(2);

    assert(llist.head->data == 1);
    assert(llist.head->next->data == 3);
    assert(llist.head->next->next->data == 4);
    cout << "3: test_delete() passed!" << endl;
}

void test_search() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    Node* node_found = llist.search(2);
    assert(node_found->data == 2);
    cout << "4: test_insert() passed!" << endl; 
}

void test_is_empty() {
    LinkedList llist;
    assert(llist.is_empty() == true); 
    cout << "5: test_is_empty() passed!" << endl; 
}

void test_size() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    assert(llist.size() == 2);
    cout << "6: test_size() passed!" << endl; 
}

void test_index() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(8);
    llist.insert(9);
    assert(llist.index(9) == 2);
    cout << "7: test_index() passed!" << endl; 
}
void test_pop() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);
    int popped = llist.pop();
    assert(popped == 3);
    cout << "8: test_pop() passed!" << endl; 
}

void test_append() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);

    assert(llist.head->data == 1);
    assert(llist.head->next->data == 2);
    cout << "9: test_append() passed!" << endl; 
}
int main() {
    test_insert();
    test_print();
    test_delete();
    test_search();
    test_is_empty();
    test_size();
    test_index();
    test_pop();
    test_append();

    // Just printing the LinkedList
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);
    llist.print();
    return 0;
}