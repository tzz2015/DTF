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


class BST:
    def __init__(self, data_list):
        # 设置根节点
        self.root = Node(data_list[0])
        # 生成二叉树
        for data in data_list[1:]:
            self.insert(self.root, data)

    # 对二叉树进行排序
    def insert(self, node, value):
        # 插入右节点
        if value > node.data:
            if node.right:
                self.insert(node.right, value)
            else:
                node.insert_right(value)
        # 插入左节点
        else:
            if node.left:
                self.insert(node.left, value)
            else:
                node.insert_left(value)

    # 中序排序 从小到大 左根右
    def mid_order(self, node):
        if node.data:
            # 左
            if node.left:
                self.mid_order(node.left)
            # 根
            node.show()
            # 右
            if node.right:
                self.mid_order(node.right)

    # 遍历从大到小排序 右根左
    def big_to_small_order(self, node):
        # 右
        if node.right:
            self.big_to_small_order(node.right)
        # 根
        node.show()
        # 左
        if node.left:
            self.big_to_small_order(node.left)

    # 搜索
    def do_search(self, node, parent, data):
        # 如果节点为空 搜索不到
        if node is None:
            return False, node, parent
        # 如果节点数据跟搜索的数据相同 则返回到相应的数据
        if node.data == data:
            return True, node, parent
        # 如果搜索的数据大于节点数据 则向右查询 否则向左查询
        if data > node.data:
            return self.do_search(node.right, node, data)
        else:
            return self.do_search(node.left, node, data)

    # 插入数据
    def add_node(self, data):
        flag, node, parent = self.do_search(self.root, self.root, data)
        # 如果数据不存在 则需要进行插入操作
        if not flag:
            new_node = Node(data)
            # 如果当前数据大于最后一个节点的数据 则盖数据为父节点的右节点
            if data > parent.data:
                parent.right = new_node
            else:
                parent.left = new_node


if __name__ == '__main__':
    L = [4, 2, 9, 1, 7, 6, 5, 3, 8]
    bst = BST(L)
    # 输出排序后的二叉树json
    print(json.dumps(bst, default=lambda obj: obj.__dict__))
    print('--------------小到大----------------')
    # 输出中序排序 从小到大
    bst.mid_order(bst.root)
    print('--------------大到小----------------')
    # 输出中序排序 从大到小
    bst.big_to_small_order(bst.root)
    print('--------------查询----------------')
    so, node, parent = bst.do_search(bst.root, None, 2)
    print('查询到结果：%s 当前节点：%s 父节点：%s' % (so, node.data, parent.data))
    print('--------------插入数据----------------')
    bst.add_node(11)
    print(json.dumps(bst, default=lambda obj: obj.__dict__))


"""
1.先序遍历：先访问跟节点 后左节点 最后右节点
2.中序遍历：先访问左节点 后跟节点 最后右节点
3.后序遍历：先访问左节点 后右节点 最后跟节点
"""
