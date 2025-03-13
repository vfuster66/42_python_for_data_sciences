from printer import print_success, print_failure


def mean(data):
    return sum(data) / len(data)


def median(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]


def quartile(data):
    data = sorted(data)
    q1 = data[len(data) // 4]
    q3 = data[(len(data) * 3) // 4]
    return [q1, q3]


def var(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def std(data):
    return var(data) ** 0.5


def ft_statistics(*args, **kwargs):
    """
    Fonction pour calculer des statistiques basiques
    (mean, median, quartile, var, std)
    """
    if len(args) == 0:
        print_failure("ERROR : No arguments provided")
        return

    stats_funcs = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "var": var,
        "std": std,
    }

    for key in kwargs:
        func_name = kwargs[key]
        if func_name not in stats_funcs:
            print_failure(f"ERROR : '{func_name}' is not a valid statistic")
        else:
            result = stats_funcs[func_name](args)
            print_success(f"{func_name} : {result}")
