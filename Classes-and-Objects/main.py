class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float): # specify the type of attributes to create
        # with the if clauses i decided to make sure that the attributes types are respected. The program will raise an error if not.
        
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.name = name
        
        
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        self.age = age

        
        if not isinstance(tracks, list):
            raise TypeError("Tracks must be a list")
        self.tracks = tracks

        
        if not isinstance(score, float):
            raise TypeError("Score must be a floating point")
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        

    def change_age(self, new_age):
        if type(new_age) == int:
            self.age = new_age
        else:
            return TypeError("Age must be an integer.") # make sure that age remains an integer

    def add_track(self, new_track):
        self.tracks.append(new_track)

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
print(Bob.name)

Bob.change_age(34)
print(Bob.age)

Bob.add_track("UI/UX")
print(Bob.tracks)

Bob.get_score()
print(Bob.score)
