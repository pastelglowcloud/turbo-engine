def multiplication_table(start, stop):
    end = stop + 1
    for x in range (start, end):
        for y in range (start, end):
            print(str(x*y), end=" ")
        print()