"""
顺序查找又称为线性查找，
是一种最简单的查找方法。
适用于线性表的顺序存储结构和链式存储结构。
该算法的时间复杂度为O(n)。
"""


def sequential_search(lis, key):
    exit_index = -1
    for i in range(len(lis)):
        if lis[i] == key:
            exit_index = i
            break
    return exit_index


if __name__ == '__main__':
    LIST = [14, 45, 68, 23, 22, 52, 71, 99, 30, 62]
    result = sequential_search(LIST, 22)
    print(result)
