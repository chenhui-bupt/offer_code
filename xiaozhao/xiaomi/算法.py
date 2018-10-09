n, m = list(map(int, input().split()))
nums = list(range(1, n+1))
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.next = None


root = TreeNode(nums[-1])
node = root
for i in range(len(nums)-2, -1, -1):
    tmp = TreeNode(nums[i])
    node.next = tmp
    node = tmp

print(root.val, root.next.val, root.next.next.val)
def dfs(root, path, algo, expected, tsum, last, res):
    if root:
        print(last[0], tsum, algo, path)
        if not root.next and tsum[0]+last[0] == expected:
            res.append(path[::])
            print('hh')
        path.append(algo)
        if algo == '+':
            tsum[0] += last[0]
            last[0] = root.val
        elif algo == '-':
            tsum[0] -= last[0]
            last[0] = root.val
        elif algo == ' ':
            print(last[0])
            last[0] = last[0] + root.val * (10 ** len(str(last[0])))
            print(last[0])
        dfs(root.next, path, '+', expected, tsum, last, res)
        dfs(root.next, path, '-', expected, tsum, last, res)
        dfs(root.next, path, ' ', expected, tsum, last, res)
        path.pop()
path = []
res = []
tsum = [0]
last = [0]
dfs(root, path, '+', m, tsum, last, res)
print(res)