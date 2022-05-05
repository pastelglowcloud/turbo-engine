def square_digits(num):

#     digits =[int(a) for a in str(num)]
#     squared =[a**2 for a in digits]
#     string = [str(a) for a in digits]
#     string = "".join(string)
#     print(string)

#     digits = [int(a) for a in str(num)]
#     squared = [a*a for a in digits)
#     string = [str(a) for a in squared]
#     answer = "".join(string)
#     print(answer)

    return int(("".join(str(pow(int(a),2)) for a in str(num))))