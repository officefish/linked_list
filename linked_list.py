from enum import Enum
import uuid
import datetime
import random
class Role(Enum):
    QUEST = 1
    MEMBER = 2
    ADMINISTRATOR = 3
    OWNER = 4


class Data():

    MAX_NAME_LENGTH = 24

    def __init__(self, name, role = Role.QUEST):
        self._name = name # 32 символа 256 бит 
        self.role = role
        self.id = uuid.uuid4()
        self.createdAt = datetime.datetime.now()
        self.payload = random.randint(0, 1000)

    @property 
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > Data.MAX_NAME_LENGTH:
            raise ValueError('to long name')
        self._name = name

    def serialize(self):
        byte_array = bytearray()
        
        b_name = bytearray(self.name.encode('utf-8'))

        numBytes = Data.MAX_NAME_LENGTH - len(b_name)
        if numBytes:
            b_name += bytes(numBytes)

        print (len(b_name))
        byte_array += b_name

        b_role =  bytearray(str(self.role).encode('utf-8'))
        byte_array += b_role

        b_id =  bytearray( str(self.id).encode('utf-8') )
        byte_array += b_id

        b_date = bytearray(str(self.createdAt.timestamp()).encode('utf-8'))
        byte_array += b_date

        return byte_array   

class Item():
    def __init__(self, name, role = Role.QUEST):
        self.data = Data(name, role)
        self.next = None

    def toString(self):
        return f'name: {self.data.name}, id: {self.data.id}, role: {self.data.role}, cratedAt: {self.data.createdAt}'
    
    def serialize(self):
        byte_array = self.data.serialize()
        return byte_array
    
    @staticmethod
    def newItemByData(data):
        item = Item(data.name, data.role)
        item.data.payload = data.payload
        item.data.createdAt = data.createdAt
        item.data.id = data.id
        return item


class LinkedList():
    def __init__(self):
        self.head = None

    def getLastItem(self, item):
        if not item:
            return None

        if item.next:
            return self.getLastItem(item.next)
        else:
            return item
        
    def AddElement(self, name, role):
        item = Item(name, role)
        tail = self.getLastItem(self.head)
        if tail:
            tail.next = item 
        else:
            self.head = item            


    def AddElementByData(self, data):
        item = Item.newItemByData(data)
        tail = self.getLastItem(self.head)
        
        if tail:
            tail.next = item 
        else:
            self.head = item   

    def insertElementByData(self, data):
        item = Item.newItemByData(data)
        if self.head:
            item.next = self.head
            self.head = item

    def toString(self):
        currentItem = self.head
        while True:
            if currentItem: 
                print(currentItem.toString())
            if currentItem.next:
                currentItem = currentItem.next
            else:
                break

    def deserialize(self, fileName):
        pass


    def serializeItem(self, item, bArray):
        if not item:
            return
        
        bArray += item.serialize()
        if item.next:
            self.serializeItem(item.next, bArray)


    def serialize(self):
        if not self.head:
            return None
        
        current = self.head 
        bArray = bytearray()

        self.serializeItem(current, bArray)

        return bArray

        # b_current = current.serialize()
        # bArray += b_current

        # if current.next:

    def bubble_sort(self):
        if not self.head:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current.next:
                if current.data.payload > current.next.data.payload:
                    current.data, current.next.data = current.next.data, current.data 
                    swapped = True
                current = current.next


    def printRatingRecursion(self, item):
        if not item:
            return

    
        # for i in range(len(data_sort)):
        #     for j in range(len(data_sort)-1):
        #         if data_sort[j] > data_sort[j+1]:
        #             data_sort[j], data_sort[j+1] = data_sort[j+1], data_sort[j]
        
        
        print(f'name: {item.data.name},  payload: {item.data.payload}')
        if item.next:
            self.printRatingRecursion(item.next)
        

    def printRating (self):
        item = self.head
        self.printRatingRecursion(item)
        




llist = LinkedList()

d1 = Data('Sergey', Role.MEMBER)
# print (d1.payload)
d1.payload = 200
# print(d1.payload)

# try: 
#     d1.name = "ckkfkfkfkf sshshsh shshshs hshshshhs"
# except ValueError:
#     print('Input name with max length no mor 24 symbols')
#     newName = input('> ')
#     d1.name = newName

llist.AddElementByData(d1)

llist.AddElement('Maxim', Role.MEMBER)
llist.AddElement('Igor', Role.QUEST)
llist.AddElement('Shakir', Role.ADMINISTRATOR)
llist.AddElement('Nikolay', Role.MEMBER)
llist.AddElement('Egor', Role.QUEST)
llist.AddElement('Nastya', Role.ADMINISTRATOR)

# llist.printRating()

llist.bubble_sort()

llist.printRating()

# import pickle
# filename = 'llist.pkl'

# with open(filename, 'wb') as file:
#     pickle.dump(llist, file)


# with open(filename, 'rb') as file:
#     data = pickle.load(file)
# print(data)


# byte_array = llist.serialize()
# print(byte_array)

# llist.toString()


# stack = list()
# stack.append(Data('Sergey', Role.MEMBER))
# stack.append(Data('Sergey', Role.MEMBER))


# print(len(stack))








































# from enum import Enum
# import uuid
# import datetime

# class Role(Enum):
#     QUEST = 1
#     MEMBER = 2
#     ADMINISTRATOR = 3
#     OWNER = 4

# class ListItem():

#     def __init__(self, name, role = Role.QUEST):
#         self.name = name
#         self.role = role
#         self.id = uuid.uuid4()
#         self.createdAt = datetime.datetime.now()

#         self.next = None


# class LinkedList():
    
#     def __init__(self):
#         self.head = None

#     def getLastItem(self, item):
#         if not self.head:
#             return None 

#         if item.next:
#             return self.getLastItem(item.next)
#         else:
#             return item


#     def addElement(self, name, role = Role.QUEST):
#         item = ListItem(name, role)

#         if not self.head:
#             self.head = item
#             return
        
#         lastItem = self.getLastItem(self.head)
#         lastItem.next = item

#     def getLength(self):

#         length = 0

#         if not self.head:
#             return length
        
#         currentItem = self.head
#         length += 1

#         while True:
#             if currentItem.next:
#                 currentItem = currentItem.next
#                 length += 1
#             else:
#                 break

#         return length






# llist = LinkedList()
# llist.addElement('Sergey', Role.ADMINISTRATOR)
# llist.addElement('Anton')
# llist.addElement('Vladimit', Role.ADMINISTRATOR)

# print(f'length: {llist.getLength()}')




















# import datetime, uuid
# from enum import Enum 


# class Role(Enum):
#     QUEST = 1,
#     MEMBER = 2,
#     ADMINISTRATOR = 3,
#     OWNER = 4,


# class Data(): 
#     def __init__(self):
#         self.id = uuid.uuid4()
#         self.role = Role.QUEST
#         self.createdAt = datetime.datetime.now()

#     def toString(self):
#         return f'id: {self.id}, role: {self.role}, createdAt: {self.createdAt}'   

# class LinkedListItem():
#     def __init__(self, data):
#         self.data = data 
#         self.next = None


# class LinkedList():
#     def __init__(self):
#         self.head = None
#         self.length = 0

#     def getLastItem(self, item):
#         if not item:
#             return None

#         if item.next:
#             return self.getLastItem(item.next)
#         else: 
#             return item
        
#     def getPreviousLastItem(self, item):

#         if not item:
#             return None
        
#         if item.next:
#             nextItem = item.next
#             if nextItem.next:
#                 return self.getPreviousLastItem(nextItem)
#             else:
#                 return item



#     def addElement(self, data):
#         # self.length += 1
        
#         newItem = LinkedListItem(data)
        
#         if not self.head:
#            self.head = newItem
#            return 

#         lastItem = self.getLastItem(self.head)
#         lastItem.next = newItem


#     def removeLastElement(self):
#         # if self.length:
#         #     self.length -= 1

#         previousLastItem = self.getPreviousLastItem(self.head)
#         previousLastItem.next = None

#     def getNextItem(self, item, length):
#         if not item:
#             return None
        
#         if not item.next:
#             return None
        
#         return item.next


#     def getLength(self):
        
#         length = 0
#         nextItem = self.getNextItem(self.head, length)
        
#         if nextItem:
#             length += 1
#             return self.getNextItem(nextItem, length)
            
#         return length


#     def getHeadData(self):
#         if self.head:
#             return self.head.data
#         else:
#             return None
        
#     def getTailData(self):
#         tail = self.getLastItem(self.head)
#         if not tail:
#             return None

#         return tail.data        



# llist = LinkedList()

# data1 = Data()
# data1.role = Role.MEMBER
# data2 = Data()
# data3 = Data()
# data3.role = Role.ADMINISTRATOR
# data4 = Data()


# llist.addElement(data1)
# llist.addElement(data2)
# llist.addElement(data3)
# llist.addElement(data4)

# # headData = llist.getHeadData()
# # headStr = headData.toString()
# # print(headStr)

# tailData = llist.getTailData()
# tailStr = tailData.toString()
# print(tailStr)
# print(llist.getLength())

# llist.removeLastElement()

# print(llist.getLength())


# # tailData = llist.getTailData()
# # tailStr = tailData.toString()
# # print(tailStr)











   
        
     