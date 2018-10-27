class Student:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')
    
    def __str__(self):
        return str(type(self)) + str(self.__dict__)


class StudentList:
    def __init__(self, students, **kwargs):
        self._students = students

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i == len(self._students):
            raise StopIteration()
        ret = self._students[self._i]
        self._i += 1
        return ret


def main():
    students = []
    students.append(Student(name='山田', age=12))
    students.append(Student(name='花子', age=13))

    student_list = StudentList(students)
    for student in student_list:
        print(student)

if __name__ == '__main__':
    main()
