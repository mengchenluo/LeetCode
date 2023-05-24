#21
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        temp = []
        while l1:
            temp.append(l1.val)
            l1 = l1.next
        while l2:
            temp.append(l2.val)
            l2 = l2.next
        temp = sorted(temp)
        if temp:
            head = ListNode(temp[0])
            sol = head
            for i in range(1,len(temp)):
                head.next = ListNode(temp[i])
                head = head.next
        else:
            sol = None
        return sol

#94
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        sol = []
        self.Add(root, sol)
        return sol
    
    def Add(self, node, ans):
        if node is None:
            return
        if node.left:
            self.Add(node.left, ans)
        ans.append(node.val)
        if node.right:
            self.Add(node.right, ans)

        return ans

#167
def twoSum(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]

# 347
L = [-1, -1]
k = 1

def get_key(value, ans):
    for key, val in D.items():
        if val==value and key not in ans:
            return key

D = dict()
for i in L:
    if i not in D:
        D[i] = 1
    else:
        D[i] += 1
max_val = sorted(list(D.values()), reverse=True)
ans = []
for i in range(k):
    ans.append(get_key(max_val[i], ans))

print(ans)