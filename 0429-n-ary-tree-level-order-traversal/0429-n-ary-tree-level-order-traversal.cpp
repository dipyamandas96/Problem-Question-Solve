/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {// TC : O(N)+O(N)+O(N) = O(N) & SC : O(N)+O(N) = O(N)
        vector<vector<int>>ans;

        if(!root){
            return ans;
        }

        queue<Node*>q;
        q.push(root);

        while(!q.empty()){
            int sz = q.size();
            vector<int>temp;

            for(int i=1;i<=sz;i++){
                Node* curr = q.front();
                q.pop();

                for(auto child : curr->children){
                    if(!child){
                        continue;
                    }
                    q.push(child);
                }

                temp.push_back(curr->val);
            }

            ans.push_back(temp);
        }

        return ans;

    }
};