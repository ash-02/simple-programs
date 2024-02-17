# def isPossible(a,b,c,d):

#     x, y = a, b
#     flag = True
#     flagX = False
#     flagY = False

#     while(True):
#         #print(x)
#         # x = x + a
#         if(x < c):
#             if(x+b < c):
#                 x = x + b
#             elif(x+a < c):
#                 x = x + a
#         else:
#             if x == c:
#                 flagX = True
#                 a,b = x,b
#                 break
#             else:
#                 flagX = False
#                 break


#     while(True):
#         print(y)
#         # y = y + a
#         if(y < d):
#             if(y+b < d):
#                 y = y + b
#             elif(y+a < d):
#                 y = y + a
#         else:
#             if y == d:
#             # print("True since Y is:",y)
#                 flagY = True
#                 a,b = a,y
#                 break
#             else:
#                 flagY = False
#                 break
            
#     if flagX == True and flagY == True:
#         return "yes"
#     return "no"         
                
#         # x = x + a
#         # if(x > c):
#         #     x = 0
#         #     flag = False
#         #     break
#         # if(x == c):
#         #     flagX = True
#         #     break
    
#     # while(True):
#     #     y = y + b
#     #     if(y > d):
#     #         y = 0
#     #         flag = False
#     #         break
#     #     if(y == d):
#     #         flagY = True
#     #         break
    
#     # while(flagX == False):
#     #     x = x + b
#     #     if(x > c):
#     #         x = 0
#     #         flag = False
#     #         break
#     #     if(x == c):
#     #         flagX = True
#     #         break
    
#     # while(flagY == False):
#     #     y = y + a
#     #     if(y > d):
#     #         y = 0
#     #         flag = False
#     #         break
#     #     if(y == d):
#     #         flagY = True
#     #         break
    
#     # if flagX == True or flagY == True:
#     #     return "yes"
#     # else:
#     #     return "no"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def isPossible(a, b, c, d):
    return gcd(a, b) == gcd(c, d)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print("here")
    print(isPossible(a,b,c,d))