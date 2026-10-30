from abc import ABCMeta, abstractmethod
class Champ:
    def attack(self):
        print('기본 공격')
class MagicChamp(Champ):
    def attack(self):
        super().attack()
        print('추가 마법')
class BasicChamp(Champ):
    pass
for champ in [MagicChamp(), BasicChamp()]:
    champ.attack()
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    @abstractmethod
    def go_to_school(self):
        pass
class CourseStudent(StudentBase):
    def study(self):
        print('공부하기')
    def go_to_school(self):
        print('학교가기')
student = CourseStudent()
student.study()
student.go_to_school()
