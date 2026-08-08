//recursive approach


class Solution {

    public List<Integer> preorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<>();

        preorder(root, result);

        return result;
    }

    private void preorder(TreeNode root, List<Integer> result) {

        if (root == null) {
            return;
        }

        // 1. Visit root
        result.add(root.val);

        // 2. Visit left
        preorder(root.left, result);

        // 3. Visit right
        preorder(root.right, result);
    }
}

//iterative approach

public class Solution {

    public List<Integer> preorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            result.add(node.val);

            // Push right child first so that left child is processed first
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }

        return result;
    }
}