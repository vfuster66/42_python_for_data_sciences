import subprocess
from printer import print_title, print_success


def test_ex05_argument():
    print_title("Test ➜ Texte fourni en argument")

    text = "Python 3.0, released in 2008."
    result = subprocess.run(
        ['python3', 'ex05/tester.py', text],
        capture_output=True, text=True
    )

    assert "upper letters" in result.stdout
    assert "lower letters" in result.stdout
    assert "punctuation marks" in result.stdout
    assert "spaces" in result.stdout
    assert "digits" in result.stdout
    print_success("✅ Test avec argument OK")


def test_ex05_input():
    print_title("Test ➜ Texte fourni en input()")

    text = "Python 3.0"
    result = subprocess.run(
        ['python3', 'ex05/tester.py'],
        input=text,
        capture_output=True, text=True
    )

    assert "upper letters" in result.stdout
    print_success("✅ Test avec input OK")


def test_ex05_multiple_arguments():
    print_title("Test ➜ Trop d'arguments fournis")

    result = subprocess.run(
        ['python3', 'ex05/tester.py', 'arg1', 'arg2'],
        capture_output=True, text=True
    )

    assert "more than one argument is provided" in result.stdout
    print_success("✅ Test trop d'arguments OK")
