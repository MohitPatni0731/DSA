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
};

void test_insert() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    assert(llist.head->data == 1); 
    cout<<"Test case passed!"<<endl; 
}

int main() {
    test_insert();
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);
    llist.print();
    return 0;
}