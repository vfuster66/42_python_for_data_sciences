import unittest
import io
import sys
from ex00.ft_statistics import ft_statistics

# Importer printer
from printer import print_success, print_failure, print_info, print_title


def capture_output(func, *args, **kwargs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func(*args, **kwargs)
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


class TestFtStatistics(unittest.TestCase):

    def test_mean(self):
        print_title("Test Mean")
        expected = "mean : 20.0"
        print_info("Appel de ft_statistics(10, 20, 30, mean='mean')")
        output = capture_output(ft_statistics, 10, 20, 30, mean="mean")
        if expected in output:
            print_success(f"Attendu : {expected} / Obtenu : {output.strip()}")
        else:
            print_failure(f"Attendu : {expected} / Obtenu : {output.strip()}")
        self.assertIn(expected, output)

    def test_median(self):
        print_title("Test Median")
        expected = "median : 3"
        print_info("Appel de ft_statistics(1, 3, 5, median='median')")
        output = capture_output(ft_statistics, 1, 3, 5, median="median")
        if expected in output:
            print_success(f"Attendu : {expected} / Obtenu : {output.strip()}")
        else:
            print_failure(f"Attendu : {expected} / Obtenu : {output.strip()}")
        self.assertIn(expected, output)

    def test_quartile(self):
        print_title("Test Quartile")
        expected = "quartile : [2, 4]"
        print_info(
            "Appel de ft_statistics(1, 2, 3, 4, 5, quartile='quartile')"
        )
        output = capture_output(
            ft_statistics, 1, 2, 3, 4, 5, quartile="quartile"
        )
        if expected in output:
            print_success(f"Attendu : {expected} / Obtenu : {output.strip()}")
        else:
            print_failure(f"Attendu : {expected} / Obtenu : {output.strip()}")
        self.assertIn(expected, output)

    def test_var(self):
        print_title("Test Variance")
        expected = "var : 125.0"
        print_info("Appel de ft_statistics(10, 20, 30, 40, var='var')")
        output = capture_output(ft_statistics, 10, 20, 30, 40, var="var")
        if expected in output:
            print_success(f"Attendu : {expected} / Obtenu : {output.strip()}")
        else:
            print_failure(f"Attendu : {expected} / Obtenu : {output.strip()}")
        self.assertIn(expected, output)

    def test_std(self):
        print_title("Test Standard Deviation")
        expected = "std : 8.16496580927726"
        print_info("Appel de ft_statistics(10, 20, 30, std='std')")
        output = capture_output(ft_statistics, 10, 20, 30, std="std")
        if expected in output:
            print_success(f"Attendu : {expected} / Obtenu : {output.strip()}")
        else:
            print_failure(f"Attendu : {expected} / Obtenu : {output.strip()}")
        self.assertIn(expected, output)

    def test_error_no_args(self):
        print_title("Test ERROR si aucun argument n'est donné")
        expected = "ERROR"
        print_info("Appel de ft_statistics(mean='mean')")
        output = capture_output(ft_statistics, mean="mean")
        if expected in output:
            print_success(f"Attendu : {expected} / Obtenu : {output.strip()}")
        else:
            print_failure(f"Attendu : {expected} / Obtenu : {output.strip()}")
        self.assertIn(expected, output)

    def test_unknown_stat(self):
        print_title("Test Unknown Stat")
        expected = "ERROR"
        print_info(
            "Appel de ft_statistics(1, 2, 3, wrong='non_existing_stat')"
        )
        output = capture_output(
            ft_statistics, 1, 2, 3, wrong="non_existing_stat"
        )
        if expected in output:
            print_success(f"Attendu : {expected} / Obtenu : {output.strip()}")
        else:
            print_failure(f"Attendu : {expected} / Obtenu : {output.strip()}")
        self.assertIn(expected, output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
