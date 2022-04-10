from collections import Counter
import concurrent.futures


class Point:
    def __init__(self, x=None, y=None, value=0):
        self.x = x
        self.y = y
        self.value = value


class Node:
    def __init__(self, point=Point, next_=None):
        self.point = point
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, point):
        newNode = Node(point)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode


class runDeliveries:
    def __init__(self, point=Point):
        self.point = point

    def deliverypath(self, myList, mystr):
        myLinkedL = LinkedList()
        myLinkedL.insert(self.point)
        while len(mystr) != 0:
            if mystr[0] == '^':  # North: ^
                newPoint = matrixOps(myList, Point(self.point.x + 1, self.point.y))
                myLinkedL.insert(newPoint)
            elif mystr[0] == 'v':  # South: v
                newPoint = matrixOps(myList, Point(self.point.x - 1, self.point.y))
                myLinkedL.insert(newPoint)
            elif mystr[0] == '<':  # West: <
                newPoint = matrixOps(myList, Point(self.point.x, self.point.y + 1))
                myLinkedL.insert(newPoint)
            else:  # East: >
                newPoint = matrixOps(myList, Point(self.point.x, self.point.y - 1))
                myLinkedL.insert(newPoint)
            self.point = newPoint
            mystr = mystr[1:]


def matrixOps(myList, point):
    myList[point.x][point.y] = 1 if myList[point.x][point.y] == 0 else myList[point.x][point.y] + 1
    point.value = myList[point.x][point.y]
    counter[myList[point.x][point.y]] += 1
    return point


if __name__ == '__main__':
    with open("PizzaDeliveryInput.txt") as file:
        mystr = file.readline()

    # Cleaning the string from unwanted characters
    mystr = ''.join(i for i in mystr if i in ['^', 'v', '<', '>'])

    print(mystr)
    deliveryList = [[0 for x in range(len(mystr))] for y in range(len(mystr))]
    start_row = len(mystr) // 2
    start_col = len(mystr) // 2
    counter = Counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        dguyPath = runDeliveries(Point(start_row, start_col))
        executor.submit(dguyPath.deliverypath, deliveryList, mystr)

    print(f"The number of houses receives at least one pizza: {counter[1]}")
