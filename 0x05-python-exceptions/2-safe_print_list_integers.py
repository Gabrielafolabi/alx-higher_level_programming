def safe_print_list_integers(my_list[], x=0)
    real = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end="")
            real += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (real)
