class Student:
    def __init__(self,nume,note):
        self.nume=nume
        self.note=note
    def Adauga(self,nota):
        self.note.append(nota)
    def media(self):
        return sum(self.note)/len(self.note)
    def __str__(self):
        if self.media()>4.5:
            return f"promovat cu media {self.media()}"
        else:
            return f"nepromovat cu media {self.media()}"

stud1=Student("Marian",[5,5,5,6])
stud1.Adauga(10)
print(stud1)