while True:
    try:
        a = input()
        print(a)
        exit()
    except EOFError:
        break
