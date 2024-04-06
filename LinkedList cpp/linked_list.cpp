#include <stdio.h>
#include <iostream>
#include <cassert>
#include <sstream>
#include <stack>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int data) {
        /* Time - O(1)
        Space - O(1) */
        this->data = data;
        this->next = nullptr;
    }
};

class LinkedList {
public:
    Node* head;

    LinkedList() {
        /* Time - O(1)
        Space - O(1) */
        head = nullptr;
    }

    void insert(int data) {
        /* Time - O()
        Space - O() */
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
        /* Time - O(N)
        Space - O(1) */
        Node* current = head;
        while (current != nullptr) {
            cout<<current->data;
            cout<<" --> ";
            current = current->next;
        }
        cout<<"None"<<endl;
    }

    void delete_node(int data) {
        /* Time - O(N)
        Space - O(1) */
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
        /* Time - O(N)
        Space - O(1) */
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
        /* Time - O(1)
        Space - O(1) */
        if (head == nullptr) {
            return true;
        }
        else {
            return false;
        }
    }

    int size() {
        /* Time - O(N)
        Space - O(1) */
        Node* current = head;
        int count = 0;
        while (current != nullptr) {
            count += 1;
            current = current->next;
        }
        return count;
    }

    int index(int data) {
        /* Time - O(N)
        Space - O(1) */
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
        /* Time - O(N)
        Space - O(1) */
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
        /* Time - O(N)
        Space - O(1) */
        Node* new_node = new Node(data);
        new_node->next = head;
        head = new_node;
    }

    int middle_element() {
        /* Time - O(N)
        Space - O(1) */
        Node* current = head;
        int count = 0;

        while (current != nullptr) {
            count += 1;
            current = current->next;
        }
        
        int middle = count / 2;
        current = head;

        for (int i = 0; i < middle; i++)
        {
            current = current->next;
        }
        int data = current->data;
        return data;       
    }

    LinkedList* copy() {
        /* Time - O(N)
        Space - O(1) */
        LinkedList* copy_llist = new LinkedList();
        Node* current = head;

        while (current != nullptr) {
            copy_llist->insert(current->data);
            current = current->next;
        }
        return copy_llist;
    }

    void remove_duplicate() {
        /* Time - O(N)
        Space - O(1) */
        Node* current = head;
        while (current != nullptr) {
            Node* next_node = current;
            next_node = current->next;
            while (next_node != nullptr && next_node->data == current->data) {
                next_node = next_node->next;
            }
            current->next = next_node;
            current = next_node;
        }
    }

    void swap_nodes(int x, int y) {
        /* Time - O(N)
        Space - O(1) */
        Node* current = head;
        while (current != nullptr) {
            if (current->data == x) {
                current->data = y;
            } else if (current->data == y)
            {
                current->data = x;
            }
            current = current->next;
        }
    }

    void move_head_to_tail() {
        /* Time - O(N)
        Space - O(1) */
        Node* current = head;
        Node* previous = nullptr;
        while (current->next != nullptr) {
            previous = current;
            current = current->next;
        }
        previous->next = nullptr;
        current->next = head;
        head = current;

        return;
    }

    void reverse() {
        /* Time - O(N)
        Space - O(N) */
        std::stack<int> stack;
        Node* current = head;

        while (current != nullptr) {
            stack.push(current->data);
            current = current->next;
        }

        current = head;
        
        while (current != nullptr) {
            current->data = stack.top();
            stack.pop();
            current = current->next;
        }
    }

    bool is_plaindrome() {
        /* Time - O(N)
        Space - O(N) */
        LinkedList* reversedList = copy();
        reversedList->reverse();

        if (reversedList->head->data == head->data) {
            return true;
        } else {
            return false;
        }
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

void test_middle_element() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);

    assert(llist.middle_element() == 2);
    cout << "10: test_middle_element() passed!" << endl; 
}

void test_copy() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);
    LinkedList* llist1 = llist.copy();
    assert(llist1->head->data == llist.head->data);
    cout << "11: test_copy() passed!" << endl; 
}

void test_remove_duplicate() {
    LinkedList llist;
    llist.insert(2);
    llist.insert(2);
    llist.insert(3);
    llist.remove_duplicate();
    assert(llist.head->next->data == 3);
    cout << "12: test_remove_duplicate() passed!" << endl; 
}

void test_swap_nodes() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);
    llist.swap_nodes(1,2);
    assert(llist.head->data == 2);
    cout << "13: test_swap_nodes() passed!" << endl; 
}

void test_move_head_to_tail() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);
    llist.move_head_to_tail();
    assert(llist.head->data == 3);
    cout << "14: test_move_head_to_tail() passed!" << endl; 
}

void test_reverse() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(4);
    llist.reverse();
    assert(llist.head->data == 4);
    cout << "15: test_reverse() passed!" << endl; 
}

void test_is_palindrome() {
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(4);
    assert(llist.is_plaindrome() == false);
    cout << "16: test_is_palindrome() passed!" << endl; 
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
    test_middle_element();
    test_copy();
    test_remove_duplicate();
    test_swap_nodes();
    test_move_head_to_tail();
    test_reverse();
    test_is_palindrome();

    // Just printing the LinkedList
    LinkedList llist;
    llist.insert(1);
    llist.insert(2);
    llist.insert(3);
    llist.print();
    return 0;
}