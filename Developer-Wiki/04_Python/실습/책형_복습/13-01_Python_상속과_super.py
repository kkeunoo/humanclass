class Person:
    def __init__(self, name):
        print('부모 초기화', name)
        self.name = name
    def greeting(self):
        print('안녕하세요', self.name)
class Student(Person):
    def __init__(self, name, grade):
        print('자식 초기화 시작')
        super().__init__(name)
        self.grade = grade
        print('자식 초기화 끝')
    def study(self):
        self.greeting()
        print(self.grade, '학년 공부')
class InheritedStudent(Person):
    pass
a = Student('민지', 3)
a.study()
b = InheritedStudent('준호')
b.greeting()
