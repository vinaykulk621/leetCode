/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    // if both are null
    if(p==null && q==null){
        return true
    }

    // if either of them are null
    if(p==null || q==null){
        return false
    }

    // reccursively comparing left and right part of the tree consecutively
    return p.val==q.val && isSameTree(p.left,q.left) && isSameTree(p.right,q.right)
};
