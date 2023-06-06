class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    #def

    def isEmpty(self):
        return self.root is None
    #def

    def clear(self):
        self.root = None
    #def

    def search(self, x):
        return self._search_helper(self.root, x)
    #def

    def _search_helper(self, node, x):
        if node is None or node.val == x:
            return node
        if x < node.val:
            return self._search_helper(node.left, x)
        else:
            return self._search_helper(node.right, x)
    #def

    def insert(self, x):
        if self.search(x):
            return  # Node already exists
        self.root = self._insert_helper(self.root, x)
    #def

    def _insert_helper(self, node, x):
        if node is None:
            return TreeNode(x)
        if x < node.val:
            node.left = self._insert_helper(node.left, x)
        else:
            node.right = self._insert_helper(node.right, x)
        return node
    #def

    def breadth(self):
        if self.isEmpty():
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    #def

    def preorder(self):
        result = []
        self._preorder_helper(self.root, result)
        return result
    #def

    def _preorder_helper(self, node, result):
        if node is None:
            return
        result.append(node.val)
        self._preorder_helper(node.left, result)
        self._preorder_helper(node.right, result)
    #def

    def inorder(self):
        result = []
        self._inorder_helper(self.root, result)
        return result
    #def

    def _inorder_helper(self, node, result):
        if node is None:
            return
        self._inorder_helper(node.left, result)
        result.append(node.val)
        self._inorder_helper(node.right, result)
    #def

    def postorder(self):
        result = []
        self._postorder_helper(self.root, result)
        return result
    #def

    def _postorder_helper(self, node, result):
        if node is None:
            return
        self._postorder_helper(node.left, result)
        self._postorder_helper(node.right, result)
        result.append(node.val)
    #def

    def count(self):
        return self._count_helper(self.root)
    #def

    def _count_helper(self, node):
        if node is None:
            return 0
        return 1 + self._count_helper(node.left) + self._count_helper(node.right)
    #def

    def dele(self, x):
        if not self.search(x):
            return  # Node does not exist
        self.root = self._delete_helper(self.root, x)
    #def

    def _delete_helper(self, node, x):
        if node is None:
            return None
        if x < node.val:
            node.left = self._delete_helper(node.left, x)
        elif x > node.val:
            node.right = self._delete_helper(node.right, x)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_right = self._find_min(node.right)
                node.val = min_right.val
                node.right = self._delete_helper(node.right, min_right.val)
        return node
    #def

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    #def

    def find_min(self):
        if self.isEmpty():
            return None
        return self._find_min(self.root).val
    #def

    def find_max(self):
        if self.isEmpty():
            return None
        return self._find_max(self.root).val
    #def

    def _find_max(self, node):
        while node.right:
            node = node.right
        return node
    #def

    def _sum_helper(self, node):
        if node is None:
            return 0
        return node.val + self._sum_helper(node.left) + self._sum_helper(node.right)
    #def

    def sum(self):
        return self._sum_helper(self.root)
    #def

    def avg(self):
        total = self.sum()
        count = self.count()
        return total / count if count > 0 else 0
    #def

    def height(self):
        return self._height_helper(self.root)
    #def

    def _height_helper(self, node):
        if node is None:
            return -1
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        return 1 + max(left_height, right_height)
    #def

    def _cost_helper(self, node):
        if node is None:
            return 0
        return node.val + max(self._cost_helper(node.left), self._cost_helper(node.right))
    #def

    def max_cost_path(self):
        return self._cost_helper(self.root)
    #def

    def is_avl(self):
        return self._is_avl_helper(self.root)
    #def

    def _is_avl_helper(self, node):
        if node is None:
            return True
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self._is_avl_helper(node.left) and self._is_avl_helper(node.right)
    #def

    def is_heap(self):
        return self._is_heap_helper(self.root)
    #def

    def _is_heap_helper(self, node):
        if node is None:
            return True
        if node.left is not None and node.left.val > node.val:
            return False
        if node.right is not None and node.right.val > node.val:
            return False
        return self._is_heap_helper(node.left) and self._is_heap_helper(node.right)
    #def

# Example usage:

# Create a binary search tree
bst = BST()

# Insert elements into the tree
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Check if the tree is empty
print("Is the tree empty?", bst.isEmpty())

# Search for a node
print("Search for 60:", bst.search(60))
print("Search for 90:", bst.search(90))

# Traverse the tree
print("Breadth-first traversal:", bst.breadth())
print("Preorder traversal:", bst.preorder())
print("Inorder traversal:", bst.inorder())
print("Postorder traversal:", bst.postorder())

# Count the number of nodes
print("Number of nodes:", bst.count())

# Delete a node
bst.dele(60)
print("Inorder traversal after deleting 60:", bst.inorder())

# Find the minimum and maximum values
print("Minimum value:", bst.find_min())
print("Maximum value:", bst.find_max())

# Calculate the sum and average of all values
print("Sum of all values:", bst.sum())
print("Average of all values:", bst.avg())

# Calculate the height of the tree
print("Height of the tree:", bst.height())

# Calculate the cost of the most expensive path
print("Cost of the most expensive path:", bst.max_cost_path())

# Check if the tree is AVL
print("Is the tree AVL?", bst.is_avl())

# Check if the tree is a heap
print("Is the tree a heap?", bst.is_heap())

# Clear the tree
bst.clear()
print("Is the tree empty after clearing?", bst.isEmpty())
