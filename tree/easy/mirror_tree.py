class Node:
    def __init__(self,val):
        self.right = None
        self.data = val
        self.left = None
def inorderTraversalUtil(root):
    # Code here
    if root is None:
        return
    inorderTraversalUtil(root.left)
    print(root.data, end=' ')    
    inorderTraversalUtil(root.right)

def inorderTraversal(root):
    # Code here
    inorderTraversalUtil(root)
    print()

def mirror(root):
    # print(root.left, root.right)
    if root.right is not None or root.left is not None:
        if root.right is not None and root.left is not None:
            root.right, root.left = root.left, root.right
            mirror(root.right)
            mirror(root.left)    
        elif root.right is None and root.left is not None:
            root.right, root.left = root.left, None
            mirror(root.right)
        elif root.right is not None and root.left is None:
            root.right, root.left = None, root.right
            mirror(root.left)
        
    


if __name__ == '__main__':
    t = int(input())
    
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(0)
            continue
        
        root = None
        dictTree = dict()
        
        for j in range(n):
            if arr[3*j] not in dictTree:
                dictTree[arr[3*j]] = Node(int(arr[3*j]))
                parent = dictTree[arr[3*j]]
                
                if j is 0:
                    root = parent
            else:
                parent = dictTree[arr[3*j]]
            
            child = Node(int(arr[3*j+1]))
                
            if(arr[3*j+2] == 'L'):
                parent.left = child
            else:
                parent.right = child
            dictTree[arr[3*j+1]] = child
        # print(root.data, root.left, root.right)             
        mirror(root)
        
        inorderTraversal(root)

        


# def set_ans(tree_arranged, node_num, ans):
#     R_child = tree_arranged[node_num]["R"]
#     L_child = tree_arranged[node_num]["L"]
#     if R_child not in tree_arranged.keys():
#         ans.append(R_child)
#     else:
#         set_ans(tree_arranged, R_child, ans)
#     ans.append(node_num)
#     if L_child not in tree_arranged.keys():
#         ans.append(L_child)
#     else:
#         set_ans(tree_arranged, L_child, ans)


# t = int(input())

# for i in range(t):
#     n = int(input())
    
#     arr = list(input().split())
#     node_num = arr[0]
#     tree_arranged = {}
#     for j in range(n):
#         tmp_list = arr[3 * j:3 * (j + 1)]
#         if tmp_list[0] not in tree_arranged.keys():
#             tree_arranged[tmp_list[0]] = {"L": -1, "R": -1}
#         tree_arranged[tmp_list[0]][tmp_list[2]] = tmp_list[1]
    
#     ans = []
#     set_ans(tree_arranged, node_num, ans)
            
#     print(*ans)
