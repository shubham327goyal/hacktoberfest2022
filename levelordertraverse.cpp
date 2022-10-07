#include <bits/stdc++.h>

using namespace std;

class node{
    public:
    int data;
    node* left;
    node* right;
    
    node(int data){
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

node* buildTree(node* root){
    cout<<"Enter data : "<<endl;
    int data;
    cin>> data;
    
    root = new node(data);
    
    if(data == -1)
        return NULL;
        
    cout<<"Enter left child of "<<data<<endl;
    root->left = buildTree(root->left);
    
    cout<<"Enter right child of "<<data<<endl;
    root->right = buildTree(root->right);
    
    return root;
}
//this is the code for level order traversal
void levelOrderTraversal(node* root)
{
    queue<node*> q;
    q.push(root);
    q.push(NULL);

    while(!q.empty())
    {
        node* temp = q.front();
        q.pop();

        if(temp==NULL)
        {
            cout<<endl;
            if(!q.empty())
            {
                q.push(NULL);
            }
        }
        else{
            cout<<temp->data<<" ";
            if(temp->left)
                q.push(temp->left); 
            if(temp->right)
                q.push(temp->right);
        }
    }
}

int main()
{
    node* root = NULL;
    root = buildTree(root);

    cout<<"Level Order Traversal : "<<endl;    
    levelOrderTraversal(root);
    return 0;
}


// Sample Input : 1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1
// Sample Output : 1
//                 3 5
//                 7 11 17

