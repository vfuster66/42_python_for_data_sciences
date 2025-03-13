from ex01.format_ft_time import display_current_time
from printer import print_title, print_success


def main():
    print_title("=== EX01 ➜ Tester format_ft_time ===")
    timestamp, date = display_current_time()

    print_success(
        f"✅ Fonction exécutée : Timestamp = {timestamp:.4f}, Date = {date}"
    )


if __name__ == "__main__":
    main()
