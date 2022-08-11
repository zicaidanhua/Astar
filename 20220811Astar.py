# -*- coding:utf-8 -*-
# @Time    :2022/8/11 10:14
# @Author  :紫菜蛋花汤
# @File    :20220811Astar.py
# @Software:PyCharm



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):#函数重载判断两个坐标是否一致
        if((self.x == other.x) and (self.y == other.y)):
            return True
        else:
            return False

    def __ne__(self, other):
        pass

class Astar:
    class Node:
        def __init__(self, point, end_point, g): #节点信息初始化
            '''
            :param point:当前节点信息
            :param end_point: 终点节点信息
            :param g: 从起点到当前节点移动的代价
            '''
            self.point = point#当前位置
            self.end_point = end_point#终点位置
            self.father = None #设置父节点
            self.g = g
            #曼哈顿算法计算当前点到终点之间的估算代价
            self.h = (abs(end_point.x - point.x) + abs(end_point.y-point.y)) * 10
            self.f = self.g + self.h

        def near_Node(self, ur, ul): #附近节点与当前节点之间的关系
            '''
            :param ur: 左右移动
            :param ul: 上下移动
            :return: 返回附近节点的信息
            '''
            nearpoint = Point(self.point.x + ur, self.point.y + ul) #调用Point类实现节点的索引
            if abs(ur) == 2 and abs(ul) == 2:#向对角线移动
                self.g = 14 #对角线的移动代价是14
            else:
                self.g = 10

            nearnode = Astar.Node(nearpoint, self.end_point, self.g) #临近节点信息
            return nearnode

    def __init__(self, start_point, end_point, map):
        '''
        :param start_point:起始点的坐标位置
        :param end_point: 结束点的坐标位置
        :param map: 地图
        '''
        self.start_point = start_point #起点位置
        self.end_point = end_point     #终点位置
        self.map = map                 #地图信息
        self.current = start_point               #当前节点是否需要设置在start_point
        self.openlist = []             #打开节点
        self.closelist = []            #已经测试过的节点
        self.path = []                 #存储每次选择的路径信息

    def select_node(self):
        '''
        在openlist中选择代价最小的点,存进closelist中
        :return:当前节点的信息
        '''
        f_min = 10000000000  # 初始设置  代价为1000
        node_temp = 0  # 缓存节点
        for each in self.openlist:  # 在openlist 中遍历 找出最小的代价节点
            if each.f < f_min:
                f_min = each.f
                node_temp = each
        self.path.append(node_temp)  # 路径信息中存入这个路径
        self.openlist.remove(node_temp)  # 将节点从待测试节点中删除
        self.closelist.append(node_temp)  # 将节点加入到closelist中 表示已测试过
        return node_temp  # 返回当前选择的节点   下一步开始寻找附近节点

    def isin_openlist(self, node):
        '''
        判断节点是否存在于openlist中 存在返回openlist中的原来的节点信息   不存在返回0
        :节点 node:
        :return:存在返回openlist中的原来的节点信息   不存在0
        '''
        for opennode in self.openlist:
            if opennode.point == node.point:
                return opennode
        return 0

    def isin_closelist(self, node):
        '''
        判断节点是否存在于closelist中 存在返回1   不存在返回0
        :节点 node:
        :return:存在返回1   不存在0
        '''
        for closenode in self.closelist:
            if closenode.point == node.point:
                return 1
        return 0

    def is_obstacle(self, node):  # 判断是否是障碍物
        if self.map[node.point.x][node.point.y] == 1:
            return 1
        return 0

    def search_nextnode(self, node):#搜索周围8个点
        ud = 2 #向上
        rl = 0
        node_temp = node.near_Node(ud, rl)  # 在调用另一个类的方法时（不论是子类还是在类外定义的类），都要进行实例化才能调用函数
        if node_temp.point == self.end_point:#如果当前点到达终点时
            return 1
        elif self.isin_closelist(node_temp):
            pass
        elif self.is_obstacle(node_temp):
            pass
        elif self.isin_openlist(node_temp) == 0:
            node_temp.father = node
            self.openlist.append(node_temp)
        else:
            if node_temp.f < (self.isin_openlist(node_temp)).f:
                self.openlist.remove(self.isin_openlist(node_temp))
                node_temp.father = node
                self.openlist.append(node_temp)

        ud = -2 #向下
        rl = 0
        node_temp = node.near_Node(ud, rl)  # 在调用另一个类的方法时（不论是子类还是在类外定义的类），都要进行实例化才能调用函数
        if node_temp.point == self.end_point:
            return 1
        elif self.isin_closelist(node_temp):
            pass
        elif self.is_obstacle(node_temp):
            pass
        elif self.isin_openlist(node_temp) == 0:
            node_temp.father = node
            self.openlist.append(node_temp)
        else:
            if node_temp.f < (self.isin_openlist(node_temp)).f:
                self.openlist.remove(self.isin_openlist(node_temp))
                node_temp.father = node
                self.openlist.append(node_temp)

        ud = 0 #向右
        rl = 2
        node_temp = node.near_Node(ud, rl)  # 在调用另一个类的方法时（不论是子类还是在类外定义的类），都要进行实例化才能调用函数
        if node_temp.point == self.end_point:
            return 1
        elif self.isin_closelist(node_temp):
            pass
        elif self.is_obstacle(node_temp):
            pass
        elif self.isin_openlist(node_temp) == 0:
            node_temp.father = node
            self.openlist.append(node_temp)
        else:
            if node_temp.f < (self.isin_openlist(node_temp)).f:
                self.openlist.remove(self.isin_openlist(node_temp))
                node_temp.father = node
                self.openlist.append(node_temp)

        ud = 0  #向左
        rl = -2
        node_temp = node.near_Node(ud, rl)  # 在调用另一个类的方法时（不论是子类还是在类外定义的类），都要进行实例化才能调用函数
        if node_temp.point == self.end_point:
            return 1
        elif self.isin_closelist(node_temp):
            pass
        elif self.is_obstacle(node_temp):
            pass
        elif self.isin_openlist(node_temp) == 0:
            node_temp.father = node
            self.openlist.append(node_temp)
        else:
            if node_temp.f < (self.isin_openlist(node_temp)).f:
                self.openlist.remove(self.isin_openlist(node_temp))
                node_temp.father = node
                self.openlist.append(node_temp)

        ud = 2 #向右上
        rl = 2
        node_temp = node.near_Node(ud, rl)  # 在调用另一个类的方法时（不论是子类还是在类外定义的类），都要进行实例化才能调用函数
        if node_temp.point == self.end_point:
            return 1
        elif self.isin_closelist(node_temp):
            pass
        elif self.is_obstacle(node_temp):
            pass
        elif self.isin_openlist(node_temp) == 0:
            node_temp.father = node
            self.openlist.append(node_temp)
        else:
            if node_temp.f < (self.isin_openlist(node_temp)).f:
                self.openlist.remove(self.isin_openlist(node_temp))
                node_temp.father = node
                self.openlist.append(node_temp)

        ud = 2 #向左上
        rl = -2
        node_temp = node.near_Node(ud, rl)  # 在调用另一个类的方法时（不论是子类还是在类外定义的类），都要进行实例化才能调用函数
        if node_temp.point == self.end_point:
            return 1
        elif self.isin_closelist(node_temp):
            pass
        elif self.is_obstacle(node_temp):
            pass
        elif self.isin_openlist(node_temp) == 0:
            node_temp.father = node
            self.openlist.append(node_temp)
        else:
            if node_temp.f < (self.isin_openlist(node_temp)).f:
                self.openlist.remove(self.isin_openlist(node_temp))
                node_temp.father = node
                self.openlist.append(node_temp)

        ud = -2 #向右下
        rl = 2
        node_temp = node.near_Node(ud, rl)  # 在调用另一个类的方法时（不论是子类还是在类外定义的类），都要进行实例化才能调用函数
        if node_temp.point == self.end_point:
            return 1
        elif self.isin_closelist(node_temp):
            pass
        elif self.is_obstacle(node_temp):
            pass
        elif self.isin_openlist(node_temp) == 0:
            node_temp.father = node
            self.openlist.append(node_temp)
        else:
            if node_temp.f < (self.isin_openlist(node_temp)).f:
                self.openlist.remove(self.isin_openlist(node_temp))
                node_temp.father = node
                self.openlist.append(node_temp)

        ud = -2#向左下
        rl = -2
        node_temp = node.near_Node(ud, rl)  # 在调用另一个类的方法时（不论是子类还是在类外定义的类），都要进行实例化才能调用函数
        if node_temp.point == self.end_point:
            return 1
        elif self.isin_closelist(node_temp):
            pass
        elif self.is_obstacle(node_temp):
            pass
        elif self.isin_openlist(node_temp) == 0:
            node_temp.father = node
            self.openlist.append(node_temp)
        else:
            if node_temp.f < (self.isin_openlist(node_temp)).f:
                self.openlist.remove(self.isin_openlist(node_temp))
                node_temp.father = node
                self.openlist.append(node_temp)

        return 0
if __name__ == '__main__':
    from Map import MapCreat
    import cv2
    import numpy as np
    globalmap = MapCreat()
    img = cv2.imread('3.jpg')
    start = globalmap.StratAndEnd(img)[0]
    end = globalmap.StratAndEnd(img)[1]
    map = globalmap.obstacle(img)
    start_point = Point(start[1],start[0])
    end_point = Point(end[1], end[0])
    #初始化设置
    astar = Astar(start_point, end_point, map)
    start_node = astar.Node(start_point, end_point, 0)
    astar.openlist.append(start_node) #将起始点添加到openlist中

    flag = 0
    while flag != 1:
        astar.current = astar.select_node()#openlist中选取一个代价最下的node节点作为当前节点
        flag = astar.search_nextnode(astar.current)
    path = []
    #画出地图的路径
    for node_path in astar.closelist:
        path.append([node_path.point.x, node_path.point.y])
        cv2.circle(img,(node_path.point.y,node_path.point.x), 1, (255 , 0, 0), 1)
    cv2.imshow('1', img)
    cv2.waitKey()
    print(path)




