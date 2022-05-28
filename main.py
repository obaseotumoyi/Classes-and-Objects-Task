# Classes and Objects

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    # Create methods for student class

    def change_name(self, name):
      print("My name is " + self.name)

    def change_age(self, age):
      print(int(self.age))

    def add_track(self, tracks):
      print(self.tracks)

    def get_score(self):
      print(self.score)

# Object

Bob = Student("Bob", 26, ["Full Time","Part Time"], 20.90)



# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

