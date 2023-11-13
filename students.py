class Student:
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade

    
class Grade:
    def __init__(self, assignments: list, score: float):
        self.assignments = assignments
        self.score = score

    def calculate_score(self):
        if len(self.assignments) == 0:
            self.score = 0
        
        else:
            total = 0
            for assignment in self.assignments:
                total = total + assignment.score

                self.score = total / len(self.assignments)

class Assignment:
    def __init__(self, name, score):
        self.name = name
        self.score = score
