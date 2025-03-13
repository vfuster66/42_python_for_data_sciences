import unittest
from datetime import datetime
import time
from ex01.format_ft_time import display_current_time
from printer import print_title, print_info, print_success, print_failure


class TestFormatFtTime(unittest.TestCase):

    def setUp(self):
        print_title("=== Test ➜ Ex01 format_ft_time ===")

    def test_display_current_time(self):
        """
        Vérifie l'affichage des secondes et de la date actuelle.
        """
        timestamp, date = display_current_time()

        # Vérification de timestamp : il doit être proche de l'instant présent
        current_time = time.time()
        time_diff = abs(current_time - timestamp)

        print_info(f"Timestamp attendu proche de : {current_time:.4f}")
        print_info(f"Timestamp obtenu            : {timestamp:.4f}")

        try:
            self.assertLessEqual(
                time_diff, 1.0, "⏱️ Écart temporel trop grand"
            )
            print_success("✅ ✅ Timestamp OK")
        except AssertionError as e:
            print_failure(f"❌ ❌ {e}")
            raise

        # Vérification de la date actuelle
        expected_date = datetime.now().strftime("%b %d %Y")
        print_info(f"Date attendue : {expected_date}")
        print_info(f"Date obtenue  : {date}")

        try:
            self.assertEqual(
                date, expected_date, "📅 La date ne correspond pas"
            )
            print_success("✅ ✅ Date OK")
        except AssertionError as e:
            print_failure(f"❌ ❌ {e}")
            raise


if __name__ == "__main__":
    unittest.main(verbosity=2)
