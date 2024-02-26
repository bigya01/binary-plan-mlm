#include<iostream>
using namespace std;

template <class T>
class Treee{
    private:
    struct Node{
        T data;
        Node *left;
        Node *right;
    };
    Node *root;
     Node *get_new_node(T data)
    {
        Node *n1 = new Node();
        n1->data = data;
        n1->left = NULL;
        n1->right= NULL;
        return n1;
    }
    public:
    Treee()
    {
        root = NULL;
    }
    Node *search(Node* root,T name){
        if (root == NULL || root->data == name){
            return root;
        }
        Node* left_search = search(root->left, name);
        if(left_search != NULL)
            return left_search;
        return search(root->right, name);
    };
    void insert(string side, T parent, T data){
        if(root == nullptr){
            root = get_new_node(parent);
            return;
        }
        Node *parentnode = search(root, parent);
        if(parentnode != NULL){
            if(side == "left" && parentnode->left == NULL)
                parentnode->left = get_new_node(data);
            else if(side == "right" && parentnode->right == NULL)
                parentnode->right = get_new_node(data);
            else
                cout << "Invalid side or node already exists!" << endl;
        }
        else
            cout << "Parent node not found!" << endl;
    }
    void preorder_traversal(Node* root) {
        if (root != nullptr) {
            cout << root->data << " ";
            preorder_traversal(root->left);
            preorder_traversal(root->right);
        }
    }
    void display(){
        preorder_traversal(root);
    }
};

int main(){
    string parent, side;
    Treee<string> t1;
    cout << "Name of the node after which new node is to be inserted: ";
    cin >> parent;
    cout << "Value to be added left or right: ";
    cin >> side;
    t1.insert(side, "krish", "bindu");
    t1.display();
    return 0;
}
