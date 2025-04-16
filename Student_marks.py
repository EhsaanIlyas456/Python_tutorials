class student:
    def __init__(self,name, eng_marks, urdu_marks,Chem_marks):
        self.name=name;
        self.eng_marks=eng_marks;
        self.__urdu_marks=urdu_marks;
        self.Chem_marks=Chem_marks;
    def average(self):
        print("The average marks are", self.eng_marks + self.urdu_marks + self.Chem_marks / 3);

p1=student("Ehsan",45,45,67);
p1.average();


