class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for i in range(3):
           sum+=self.marks[i]
        print(sum/3)   


s1=student("Anmol",[25,65,75])
s1.average()        