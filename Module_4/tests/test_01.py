import unittest
from ex01.in_out import outer
from printer import print_success, print_failure, print_title


class TestOuterInner(unittest.TestCase):

    def test_closure_positive_number(self):
        print_title("Closure Positive Number (10)")
        inner_fn = outer(10)
        result = inner_fn()
        if result == 20:
            print_success(f"Expected 20, got {result}")
        else:
            print_failure(f"Expected 20, got {result}")
        self.assertEqual(result, 20)

    def test_closure_negative_number(self):
        print_title("Closure Negative Number (-5)")
        inner_fn = outer(-5)
        result = inner_fn()
        if result == -10:
            print_success(f"Expected -10, got {result}")
        else:
            print_failure(f"Expected -10, got {result}")
        self.assertEqual(result, -10)

    def test_closure_zero(self):
        print_title("Closure Zero (0)")
        inner_fn = outer(0)
        result = inner_fn()
        if result == 0:
            print_success(f"Expected 0, got {result}")
        else:
            print_failure(f"Expected 0, got {result}")
        self.assertEqual(result, 0)

    def test_closure_float(self):
        print_title("Closure Float (3.5)")
        inner_fn = outer(3.5)
        result = inner_fn()
        if result == 7.0:
            print_success(f"Expected 7.0, got {result}")
        else:
            print_failure(f"Expected 7.0, got {result}")
        self.assertEqual(result, 7.0)

    def test_closure_string(self):
        print_title("Closure String ('Hello')")
        inner_fn = outer("Hello")
        result = inner_fn()
        if result == "HelloHello":
            print_success(f"Expected 'HelloHello', got {result}")
        else:
            print_failure(f"Expected 'HelloHello', got {result}")
        self.assertEqual(result, "HelloHello")

    def test_closure_multiple_instances(self):
        print_title("Closure Multiple Instances (2 and 4)")
        inner_fn1 = outer(2)
        inner_fn2 = outer(4)
        res1 = inner_fn1()
        res2 = inner_fn2()
        if res1 == 4 and res2 == 8:
            print_success(f"Expected 4 and 8, got {res1} and {res2}")
        else:
            print_failure(f"Expected 4 and 8, got {res1} and {res2}")
        self.assertEqual(res1, 4)
        self.assertEqual(res2, 8)

    def test_inner_function_is_callable(self):
        print_title("Inner Function is Callable")
        inner_fn = outer(1)
        if callable(inner_fn):
            print_success("Inner function is callable")
        else:
            print_failure("Inner function is not callable")
        self.assertTrue(callable(inner_fn))

    def test_inner_function_return_type(self):
        print_title("Return Type Integer")
        inner_fn = outer(3)
        result = inner_fn()
        if isinstance(result, int):
            print_success(f"Expected int, got {type(result).__name__}")
        else:
            print_failure(f"Expected int, got {type(result).__name__}")
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main(verbosity=2)
