class student:
    def __init__(self):
        self.SchoolName=input("Enter School Name :")
        self.Stuname=input("Enter Student Name :")
        self.StuRoolNo=int(input("Enter Roll Number :"))
        self.TotalMarks=0
        self.Percentage=0.0
        self.Grade="Fail"

    def totalmarks(self):
        self.Mark1=int(input("Enter Mark 1 :"))
        self.Mark2=int(input("Enter Mark2 :"))
        self.Mark3=int(input("Enter Mark3 :"))
        self.TotalMarks=self.Mark1+self.Mark2+self.Mark3
    def percentage(self):
        self.Percentage=(self.TotalMarks/3)*100
    def grade(self):
        if self.Percentage >90:
            print("A")
        elif 80<= self.percentage >=90:
            print("B")
        elif 70<= self.Percentage >80:
            print("C")
        elif 60<= self.Percentage >70:
            print("D")
        else: print("FAIL")

    def displaydetails(self):
        print(self.SchoolName)
        print(self.Stuname)
        print(self.StuRoolNo)
        print(self.TotalMarks)
        print(self.Percentage)
        print(self.Grade)

Report=student()
Report.totalmarks()
Report.percentage()
Report.grade()
Report.displaydetails()
