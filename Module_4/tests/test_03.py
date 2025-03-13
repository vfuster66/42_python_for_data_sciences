import unittest
from ex03.new_student import Student
from printer import print_title, print_success, print_failure


class TestStudent(unittest.TestCase):

    def setUp(self):
        # Reset id counter before each test
        Student._id_counter = 0

    def test_auto_increment_id(self):
        print_title("Test Auto Increment ID")

        student1 = Student("Arya", "Stark")
        student2 = Student("Jon", "Snow")

        if student1.id == 1 and student2.id == 2:
            print_success(f"IDs OK: {student1.id}, {student2.id}")
        else:
            print_failure(f"IDs Wrong: {student1.id}, {student2.id}")

        self.assertEqual(student1.id, 1)
        self.assertEqual(student2.id, 2)

    def test_login_generation(self):
        print_title("Test Login Generation")

        student = Student("Bran", "Stark")
        expected_login = "bran1"

        if student.login == expected_login:
            print_success(f"Login OK: {student.login}")
        else:
            print_failure(f"Login wrong: {student.login}")

        self.assertEqual(student.login, expected_login)

    def test_login_case_insensitive(self):
        print_title("Test Login Lowercase")

        student = Student("DaEnErYs", "Targaryen")
        expected_login = "daenerys1"

        if student.login == expected_login:
            print_success(f"Login OK: {student.login}")
        else:
            print_failure(f"Login wrong: {student.login}")

        self.assertEqual(student.login, expected_login)

    def test_student_str_method(self):
        print_title("Test __str__ Method")

        student = Student("Sansa", "Stark")
        expected_str = ("Student(id=1, first_name='Sansa', "
                        "last_name='Stark', login='sansa1')")

        if str(student) == expected_str:
            print_success("Str method OK")
        else:
            print_failure(f"Str method wrong: {str(student)}")

        self.assertEqual(str(student), expected_str)


if __name__ == "__main__":
    unittest.main(verbosity=2)
