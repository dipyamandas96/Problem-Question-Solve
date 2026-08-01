/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int idx;
    HashMap<Integer, Integer> map = new HashMap<>();

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int l = 0;
        int r = inorder.length - 1;

    
        for (int i = 0; i <= r; i++) {
            map.put(inorder[i], i);
        }

        idx = postorder.length - 1;

        return helper(inorder, postorder, l, r);
    }

    public TreeNode helper(int[] inorder, int[] postorder, int left, int right) {
     
        if (left > right) return null;

      
        int rootVal = postorder[idx--];
        TreeNode nn = new TreeNode(rootVal);

      
        int mid = map.get(rootVal);

    
        nn.right = helper(inorder, postorder, mid + 1, right);
        nn.left = helper(inorder, postorder, left, mid - 1);

        return nn;
    }
}