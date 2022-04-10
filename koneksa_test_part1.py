from collections import Counter


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


def matrixOps(myList, point):
    myList[point.x][point.y] = 1 if myList[point.x][point.y] == 0 else myList[point.x][point.y] + 1
    point.value = myList[point.x][point.y]
    counter[myList[point.x][point.y]] += 1
    return point


if __name__ == '__main__':
    with open("PizzaDeliveryInput.txt") as file:
        mystr = file.readline()
    # mystr = '^^<<v<<v><v^^<><>^^<v<v^>>^^^><^>v^>v><><><<vv^^'

    myList = [[0 for x in range(len(mystr))] for y in range(len(mystr))]
    start_row = len(mystr) // 2
    start_col = len(mystr) // 2
    counter = Counter()
    startPoint = matrixOps(myList, Point(x=start_row, y=start_col))
    myLinkedL = LinkedList()
    myLinkedL.insert(startPoint)

    while len(mystr) != 0:
        if mystr[0] == '^':  # North: ^
            newPoint = matrixOps(myList, Point(startPoint.x + 1, startPoint.y))
            myLinkedL.insert(newPoint)
        elif mystr[0] == 'v':  # South: v
            newPoint = matrixOps(myList, Point(startPoint.x - 1, startPoint.y))
            myLinkedL.insert(newPoint)
        elif mystr[0] == '<':  # West: <
            newPoint = matrixOps(myList, Point(startPoint.x, startPoint.y + 1))
            myLinkedL.insert(newPoint)
        else:  # East: >
            newPoint = matrixOps(myList, Point(startPoint.x, startPoint.y - 1))
            myLinkedL.insert(newPoint)
        startPoint = newPoint
        mystr = mystr[1:]

    # for i in range(len(myList)):
    #     for j in range(len(myList)):
    #         counter[myList[i][j]] += 1

    # for i in myList:
    #     print(i, end='\n')
    print(counter)

    print(f"The number of houses receives at least one pizza: {counter[1]}")
