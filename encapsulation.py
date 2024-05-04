### ENCAPSULATION
# POLYMORPHISM --> poly = many , MORPHISM --> forms
# var = 10
# var = int(10)
# st = str("HELLO")
# lst = list([1,2,3])
# tpl = tuple((1,2,3))
# print(len(st))
# print(len(lst))
# print(len(tpl))
# min(lst)
# min(tpl)

# def add(num1,num2,num3=0):
#     return num1+num2+num3

# print(add(10,20,25))

# def len(ob):
#     temp = 0
#     for i in ob:
#         temp+=1
#     return temp 
# print(len('hall'))

### ENCAPSULATION(

# variable types 
# public, private, protected (variables,methods)
# public -> accessible everywhere
# private -> with in class access, not outside 
# protected -> with in class access and in subclass

class Faculty(object):
    
    __portal_id = 'hekll@gmail.com' # private
    __portal_password = "123456"  # protected
    student_id = 'rohit@jecrc.in'
    student_pass = "852"

    # def __init__(self,portal_id,port_pass,stud_id,stu_pass):
    #     self.__portal_id = portal_id # private
    #     self.__portal_password =  port_pass # protected
    #     self.student_id = stud_id
    #     self.student_pass = stu_pass

    def __display(self):
        print(self.__portal_id," private variable")
        print(self._portal_password," protected variable")
        print(self.student_id," Public variable")

    def hello(self):
        self.__display()

# obj = Faculty('portal@gmail.com',1254,'stuid','6352')
# print(obj.__dict__)
# print(obj._Faculty__portal_id)

class Student(Faculty):
    pass

## NAME MANGLING
obj = Student()
print(obj.__dict__)


