n = int(input())

tree = {}

while True:
    try:
        parent, lchild, rchild = input().split()
        tree[parent] = [lchild, rchild]
    except:
        break

def pre_travel(tree, root):
    answer = []
    if root != '.':
        answer.append(root)
    lnode = pre_travel(tree, tree[root][0]) if tree[root][0] != '.' else []
    rnode = pre_travel(tree, tree[root][1]) if tree[root][1] != '.' else []
    return answer + lnode + rnode    

def in_travel(tree, root):
    answer = []
    if root != '.':
        answer.append(root)
    lnode = in_travel(tree, tree[root][0]) if tree[root][0] != '.' else []
    rnode = in_travel(tree, tree[root][1]) if tree[root][1] != '.' else []
    return lnode + answer + rnode

def post_travel(tree, root):
    answer = []
    if root != '.':
        answer.append(root)
    lnode = post_travel(tree, tree[root][0]) if tree[root][0] != '.' else []
    rnode = post_travel(tree, tree[root][1]) if tree[root][1] != '.' else []
    return lnode + rnode + answer

print(''.join(pre_travel(tree, 'A')))
print(''.join(in_travel(tree, 'A')))
print(''.join(post_travel(tree, 'A')))