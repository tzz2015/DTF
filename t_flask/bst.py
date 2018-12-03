import json

"""
1.二叉树排序
2.二叉树查找
3.二叉树插入
4.二叉树删除
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    # 插入左节点
    def insert_left(self, value):
        self.left = Node(value)
        return self.left

    # 插入右节点
    def insert_right(self, value):
        self.right = Node(value)
        return self.right

    # 输出节点数据
    def show(self):
        print(self.data)


# 对二叉树进行排序
def insert(node, value):
    # 插入右节点
    if value > node.data:
        if node.right:
            insert(node.right, value)
        else:
            node.insert_right(value)
    # 插入左节点
    else:
        if node.left:
            insert(node.left, value)
        else:
            node.insert_left(value)


# 中序排序 从小到大 左根右
def mid_order(node):
    if node.data:
        # 左
        if node.left:
            mid_order(node.left)
        # 根
        node.show()
        # 右
        if node.right:
            mid_order(node.right)


# 遍历从大到小排序 右根左
def big_to_small_order(node):
    # 右
    if node.right:
        big_to_small_order(node.right)
    # 根
    node.show()
    # 左
    if node.left:
        big_to_small_order(node.left)


if __name__ == '__main__':
    L = [4, 2, 9, 1, 7, 6, 5, 3, 8]
    # 设置根节点
    Root = Node(L[0])
    # 生成二叉树
    for i in range(len(L) - 1):
        insert(Root, L[i + 1])
    # 输出排序后的二叉树json
    print(json.dumps(Root, default=lambda obj: obj.__dict__))
    print('--------------小到大----------------')
    # 输出中序排序 从小到大
    mid_order(Root)
    print('--------------大到小----------------')
    # 输出中序排序 从大到小
    big_to_small_order(Root)


"""
1.先序遍历：先访问跟节点 后左节点 最后右节点
2.中序遍历：先访问左节点 后跟节点 最后右节点
3.后序遍历：先访问左节点 后右节点 最后跟节点
"""
