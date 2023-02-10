class Stringoperations:
   def getString(self):
      self.s = input()

   def printString(self):
      print(self.s.upper())

# strr = Stringoperations()
# strr.getString()
# strr.printString()


class Shape:
    def __init__(self):
        self.area = 0

    def area(self):
        return self.area

class Square(Shape): # subclass
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

# sq = Square(int(input()))
# print(sq.area())

class Rectangle(Shape):
   def __init__(self, width , length):
      self.length = length
      self.width = width
   
   def Area(self):
      print(self.length * self.width) 

# rec = Rectangle(int(input()) , int(input()))
# rec.Area()




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, movedX, movedY):
        self.x = movedX
        self.y = movedY

    def dist(self, another):
        return ((self.x - another.x)**2 + (self.y - another.y)**2)**0.5

# p1 = Point(int(input()), int(input()))
# p2 = Point(int(input()), int(input()))

# print("Point 1:")
# p1.show()
# print("Point 2:")
# p2.show()
# print("Distance between the points:", p1.dist(p2))



class Bank_Account:
   def __init__(self , owner , balance):
      self.owner = owner
      self.balance = balance
   
   def deposit(self, dep_money):
      self.balance += dep_money
      print("After transaction: ",self.balance)
   
   def withdraw(self, with_money):
      if with_money > self.balance:
         print("oppss")
      else:
         self.balance -= with_money
         print("After another transaction: ",self.balance)
   
# acc = Bank_Account("RK" , 100)
# acc.deposit(int(input()))
# acc.withdraw(int(input()))




def filter_prime(numbers):
    return filter(lambda x: all(x % i != 0 for i in range(2, x)), numbers) 

# numbers = list(map(int , input().split()))
# prime_numbers = list(filter_prime(numbers))
# print(prime_numbers)




