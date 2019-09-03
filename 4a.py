class Student:
    def __init__(self,age,marks):
        self.age=age
        self.marks=marks

    
    def validate1(self):
        if(self.age<=20):
            print("Not Eligible")
            return 0
        while True:
            if self.marks<0 or self.marks>100:
                self.marks=int(input("Enter the valid Marks"))
            else:
               break

    def validate(self):
        if self.age<=20 or self.marks<65 :
            print("Not Eligible")
            
        else:
            print("Eligible")
b=int(input("Enter age"))
a=int(input("Enter the marks"))


c1=Student(b,a)
c1.validate1()
c1.validate()


            
