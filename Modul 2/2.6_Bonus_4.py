a = 1
b = -2
c = -5


def main(a, b, c):
    # delta
    d = (b ** 2) - ((a * c) * 4)

    if d > 0:
        f = ((-b) - (d ** 0.5)) / (2 * a)
        s = ((-b) + (d ** 0.5)) / (2 * a)
        return f, s

    elif d == 0:
        n = -(b / (2 * a))
        return n
    else:
        return "Brak rozwiązań"
