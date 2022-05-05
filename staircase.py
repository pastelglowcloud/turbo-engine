# def staircase(n):
#     x = 1
#     return_string = ""
#     while x <= n:
#         for i in range(n+1):
#             return_string += " "*(n-i)
#             return_string += "#"*i
#         print(return_string)
#         x+=1

# def staircase(n):
#     x = 1
#     return_string = ""
#     while x <= n:
#         for i in range(1,n+1):
#             for f in range(1,n-i):
#                 return_string += " "
#             for f in range(i,n):
#                 return_string += "#"
#         print(return_string)
#         x+=1
        
# def staircase(n):
#     # Write your code here
#     x = 1
#     return_string = ""
#     while x <= n:
#         #print n-i spaces and i #
#         for i in range(1,n+1):
#             for f in range(1,n-i):
#                 return_string += " "
#             for f in range(i,n):
#                 return_string += "#"
#             #     i+=1
#             # elif i >= n:
#             #     return_string += "#"
#         print(return_string)
#         x+=1

# def staircase(n):
#     # Write your code here
#     x = 1
#     return_string = ""
#     while x <= n:
#         #print n-i spaces and i #
#         for i in range(1,n+1):
#             if i < n:
#                 return_string += " "
#                 i+=1
#             elif i >= n:
#                 return_string += "#"
#         print(return_string)
#         x+=1

# def staircase(n):
#     x = 1
#     numlist = [i for i in range(1, n+1)]
#     numlist = numlist[::-1]
#     return_string = ""
#     for i in numlist:
#         if i < n:
#             for m in range[1,i+1]:
#                 return_string += " "
#         elif i >= n:
#             for m in range[1,i+1]:
#                 return_string += "#"
#     print(return_string)

# def staircase(n):
#     x = 1
#     numlist = [i for i in range(1, n+1)]
#     numlist = numlist[::-1]
#     return_string = ""
#     while x <= n:
#         for i in numlist:
#             if i < n:
#                 for f in range(1,i+1):
#                     return_string += " "
#             elif i >= n:
#                 for f in range(1,i+1):
#                     return_string += "#"
#             i=i-1
#         print(return_string)
#         x+=1

def staircase(n):
    for i in range(1,n+1):
        print(' '*(n-i)+'#'*(i))


#this question is proof that i am a fucking idiot, i tried a million different ways for like an hour while the actual answer was so basic smh