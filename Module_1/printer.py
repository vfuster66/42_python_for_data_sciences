from colorama import init, Fore, Style

init(autoreset=True)


def print_success(message):
    print(Fore.GREEN + "✅ " + message)


def print_failure(message):
    print(Fore.RED + "❌ " + message)


def print_info(message):
    print(Fore.YELLOW + "🔎 " + message)


def print_title(title):
    print(Style.BRIGHT + Fore.CYAN + "\n=== " + title + " ===")
