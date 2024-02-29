from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 0)]
        while queue:
            current_node, level = queue.pop(0)
            neighbour, nei_level = queue[0] if queue else (None, -1)

            if level & 1:
                if current_node.val & 1 or (level == nei_level and current_node.val <= neighbour.val):
                    return False
            elif not current_node.val & 1 or (level == nei_level and current_node.val >= neighbour.val):
                return False

            queue += [(current_node.left, level + 1)] if current_node.left else []
            queue += [(current_node.right, level + 1)] if current_node.right else []
            # if current_node.left:
            #     queue.append((current_node.left, level + 1))
            #
            # if current_node.right:
            #     queue.append((current_node.right, level + 1))

        return True


def creatBTree(data, index=0):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)
        pNode.right = creatBTree(data, 2 * index + 2)
    return pNode


if __name__ == '__main__':
    test = creatBTree([5, 4, 2, 3, 3, 7])
    print(Solution().isEvenOddTree(test))
