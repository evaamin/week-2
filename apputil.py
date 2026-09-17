import numpy as np


# update/add code below ...

def coin_combos(n):
    # generator: outputs each valid penny & nickel pair for n cents
    nickels = 0
    while nickels * 5 <= n:
        pennies = n - nickels * 5
        yield (pennies, nickels)
        nickels += 1


def ways(n):
    # count how many pairs the generator outputs for # of ways
    count = 0
    for combo in coin_combos(n):
        count += 1
    return count


def lowest_score(names, scores):
    # convert first, so plain lists work the same as arrays
    names = np.array(names)
    # argmin gives the index of the lowest score so you can look up the name
    return names[np.argmin(scores)]


def sort_names(names, scores):
    names = np.array(names)
    # argsort gives indices low-to-high so you can reverse them for descending order
    sorted_names = names[np.argsort(scores)[::-1]]
    # give back plain list of names
    return sorted_names.tolist()
