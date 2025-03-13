from ex03.new_student import Student
from printer import print_title, print_success


def main():
    print_title("Ex03 ➜ Tester Student Dataclass")

    student1 = Student("Arya", "Stark")
    print_success(str(student1))

    student2 = Student("Jon", "Snow")
    print_success(str(student2))

    student3 = Student("Tyrion", "Lannister")
    print_success(str(student3))


if __name__ == "__main__":
    main()
