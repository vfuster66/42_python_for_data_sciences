from printer import print_title, print_info, print_failure


def callLimit(limit):
    """
    Décorateur qui limite le nombre d'appels d'une fonction.
    """
    print_title(f"Creating callLimit decorator with limit = {limit}")

    def decorator(func):
        counter = {"count": 0}

        def wrapper(*args, **kwargs):
            if counter["count"] >= limit:
                print_failure(
                    f"Error: function call limit reached ({func.__name__})"
                )
                return None
            counter["count"] += 1
            print_info(
                f"{func.__name__} called {counter['count']}/{limit} times"
            )
            return func(*args, **kwargs)

        return wrapper

    return decorator
