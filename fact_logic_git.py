def fact(q):
    f = 1
    while q != 0:
        f *= q
        q -= 1
    return f


if __name__ == "__main__":
    print(fact(5))
