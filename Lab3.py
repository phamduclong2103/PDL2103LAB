def sum(n):
    if n == 1:
        return 1
    else:
        return n +sum(n-1)
#def

def findmin(arr,n):
    if n == 1:
        return arr[0]
    else:
        min_ele = findmin(arr, n-1)
        return min(min_ele, arr[n-1])
#def

def findsum(arr,n):
    if n == 0:
        return 0
    else:
        return arr[n-1] + findsum(arr,n-1)
#def

def ispalindrome(arr,n):
    if n <= 1:
        return True

    if arr[0] != arr[n - 1]:
        return False

    return ispalindrome(arr[1:n-1], n - 2)
#def

def binary_search(arr, target, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)
#def

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
#def

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
#def

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
#def

def f(n):
    if n <= 1:
        return n
    else:
        return f(n - 1) + f(n - 2)
#def

def addReciprocals(n):
    if n == 1:
        return 1.0
    else:
        return 1.0 / n + addReciprocals(n - 1)
#def

def stirling_numbers_first(n, k):
    if k == 0 and n == 0:
        return 1
    elif n > 0 and k == 0:
        return 0
    else:
        return stirling_numbers_first(n - 1, k - 1) - n * stirling_numbers_first(n - 1, k)
#def

def tree_height(node):
    if node is None:
        return 0
    else:
        return 1 + max(tree_height(node.left), tree_height(node.right))
#def

def tree_size(node):
    if node is None:
        return 0
    else:
        return 1 + tree_size(node.left) + tree_size(node.right)
#def
