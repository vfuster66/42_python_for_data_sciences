import unittest
from ex02.callLimit import callLimit
from printer import print_success, print_failure, print_title


class TestCallLimit(unittest.TestCase):

    def test_limit_reached(self):
        print_title("Test Function Limit Reached")

        calls = []

        @callLimit(2)
        def my_func():
            calls.append("called")
            print_success("my_func executed")

        my_func()  # 1
        my_func()  # 2
        result = my_func()  # 3 ➔ limite dépassée

        if len(calls) == 2 and result is None:
            print_success("Limit correctly applied, function not called "
                          "after limit.")
        else:
            print_failure("Limit NOT correctly applied.")

        self.assertEqual(len(calls), 2)
        self.assertIsNone(result)

    def test_zero_limit(self):
        print_title("Test Zero Limit")

        calls = []

        @callLimit(0)
        def my_func():
            calls.append("called")
            print_success("my_func executed")

        result = my_func()

        if len(calls) == 0 and result is None:
            print_success("Zero limit correctly blocks all calls.")
        else:
            print_failure("Zero limit NOT applied correctly.")

        self.assertEqual(len(calls), 0)
        self.assertIsNone(result)

    def test_multiple_functions(self):
        print_title("Test Multiple Functions with Different Limits")

        calls1 = []
        calls2 = []

        @callLimit(1)
        def func1():
            calls1.append("called")
            print_success("func1 executed")

        @callLimit(3)
        def func2():
            calls2.append("called")
            print_success("func2 executed")

        func1()  # OK
        func1()  # STOP
        func2()
        func2()
        func2()
        func2()  # STOP

        if len(calls1) == 1 and len(calls2) == 3:
            print_success("Both functions respect their own call limits.")
        else:
            print_failure("Functions do not respect call limits.")

        self.assertEqual(len(calls1), 1)
        self.assertEqual(len(calls2), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
