# 链表节点类，用于创建链表中的单个节点
class Node:
    # 初始化节点，data为节点存储的数据，next初始为None表示没有后继节点
    def __init__(self,data):
        self.data = data  # 节点存储的数据
        self.next = None  # 指向下一个节点的引用

# 链表类，实现链表的各种操作
class LinkedList:
    # 初始化空链表
    def __init__(self):
        self.head_node = None  # 头节点初始为None，表示空链表
        self.length = 0  # 链表长度初始为0
    
    # 尾部插入节点方法
    def insert(self,data):
        self.length += 1  # 插入节点后链表长度加1
        new_node = Node(data)  # 创建新节点
        
        # 没有头节点的情况（空链表）
        if self.head_node is None:
            self.head_node = new_node  # 将新节点设为头节点
            return new_node  # 返回新插入的节点
        
        # 有头节点的情况
        else:
            current_node = self.head_node  # 从头部开始遍历
            while current_node.next is not None:  # 找到最后一个节点
                current_node = current_node.next
            current_node.next = new_node  # 在尾部添加新节点
            return new_node  # 返回新插入的节点
    
    # 获取第n个节点
    def get(self,n):
        # 检测n的合法性
        if n < 1 or n > self.length:
            return None  # 索引越界返回None
        
        current_node = self.head_node  # 从头部开始遍历
        i = 1  # 当前节点位置计数
        while current_node is not None:
            if i == n:  # 找到目标位置的节点
                return current_node  # 返回该节点
            else:
                i += 1  # 位置计数加1
                current_node = current_node.next  # 移动到下一个节点
        return None  # 遍历结束仍未找到（理论上不会执行到这里）
    
    # 在位置n插入数据为data的节点
    def insert_n(self,n,data):
        new_node = Node(data)  # 创建新节点
        
        # 在头部插入（位置1）
        if n == 1:
            new_node.next = self.head_node  # 新节点的next指向原头节点
            self.head_node = new_node  # 更新头节点为新节点
            self.length += 1  # 链表长度加1
            return new_node  # 返回新插入的节点
        
        # 在其他位置插入
        else:
            pre_node = self.get(n-1)  # 获取插入位置的前一个节点
            if pre_node is not None:  # 如果前一个节点存在
                new_node.next = pre_node.next  # 新节点的next指向前一个节点的next
                pre_node.next = new_node  # 前一个节点的next指向新节点
                self.length += 1  # 链表长度加1
                return new_node  # 返回新插入的节点
        return None  # 插入位置无效返回None
    
    # 删除第n个节点
    def delete(self,n):
        # 空链表情况
        if self.head_node is None:
            return None  # 空链表无法删除，返回None
        
        # 删除头节点（位置1）
        if n == 1:
            delete_node = self.head_node  # 保存要删除的头节点
            self.head_node = self.head_node.next  # 更新头节点为下一个节点
            self.length -= 1  # 链表长度减1
            return delete_node  # 返回被删除的节点
        
        # 删除尾节点（最后一个位置）
        if n == self.length:
            delete_node = self.get(n-1)  # 获取倒数第二个节点
            delete_node.next = None  # 将倒数第二个节点的next设为None
            self.length -= 1  # 链表长度减1
            return delete_node  # 返回被删除的节点（注意：这里实际上返回的是倒数第二个节点，可能是个bug）
        
        # 删除中间节点
        else:
            pre_node = self.get(n-1)  # 获取删除位置的前一个节点
            # 确保前一个节点存在且有下一个节点
            if pre_node is not None and pre_node.next is not None:
                delete_node = pre_node.next  # 保存要删除的节点
                pre_node.next = pre_node.next.next  # 前一个节点直接指向下下个节点
                self.length -= 1  # 链表长度减1
                return delete_node  # 返回被删除的节点
        return None  # 删除位置无效返回None
    
    # 打印链表所有节点的数据
    def print_link_list(self):
        current_node = self.head_node  # 从链表的头节点开始遍历
        while current_node is not None:  # 当当前节点不为空时继续遍历
            if current_node.next is not None:  # 如果当前节点不是最后一个节点
                print(current_node.data, end=' ')  # 打印数据后添加空格
            else:  # 如果当前节点是最后一个节点
                print(current_node.data)  # 只打印数据不添加空格
            current_node = current_node.next  # 移动到下一个节点继续遍历

# 获取链表长度（虽然这个输入在后续代码中没有被使用）
k = int(input())
# 建立链表实例
link_list = LinkedList()
# 获取链表节点信息，并填入链表
elements = list(map(int,input().split()))  # 将输入的数字转换为整数列表
for data in elements:
    link_list.insert(data)  # 遍历列表，将每个数据插入到链表尾部

# 执行插入操作
insert_count = int(input())  # 获取要执行的插入操作次数
for _ in range(insert_count):
    position, value = map(int,input().split())  # 获取插入位置和值
    node = link_list.insert_n(position, value)  # 执行插入操作
    if node is not None:  # 如果插入成功
        link_list.print_link_list()  # 打印插入后的链表
    else:  # 如果插入失败
        print("Insertion position is invalid.")  # 输出错误信息

# 执行删除操作
delete_count = int(input())  # 获取要执行的删除操作次数
for _ in range(delete_count):
    position = int(input())  # 获取删除位置
    delete_node = link_list.delete(position)  # 执行删除操作
    if delete_node is not None:  # 如果删除成功
        link_list.print_link_list()  # 打印删除后的链表
    else:  # 如果删除失败
        print("Deletion position is invalid.")  # 输出错误信息