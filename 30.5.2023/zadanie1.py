def main():
    x = [13, "string", 2.45, 0, True, False, (1, 2)]

    for i in x:
        try:
            a = 10/i
            print(a)
        except (TypeError ,ZeroDivisionError ) as te:
            print(te)


if __name__ == "__main__":
    main()