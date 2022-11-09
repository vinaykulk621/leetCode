/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {
    if(root==null){return []}
    
    let number=[]

    number.push(root.val)
    if(root.left!=null){ number.push(...preorderTraversal(root.left)) }
    if(root.right!=null){ number.push(...preorderTraversal(root.right)) }
    return number
};
