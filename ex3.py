class Student():
    def __init__(self):
        self.items=[]
    def insert(self):
        n=int(input("enter the number of student:"))
        for i in range(n):
            sname=input("enter the student name:")
            regno=(input("enter the register number :"))
            branch=input("entre the name of the branch :")
            result=float(input("entre the result :"))
            self.items.append([sname,regno,branch,result])
    def delete(self):
        for row in self.items:
            for i in row:
                if i==row:
                    self.items.remove(row)
    def display(self):
        for i in self.items:
            print(i)
s=Student()
s.insert()
s.display()
s.delete()
s.display()
