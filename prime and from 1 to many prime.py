n=int(input("Enter a Number :"))
for i in range(2,n):
    if n%i==0:
        print(n,'is not prime')
        break
else:
    print('prime')






# def is_prime(n):
#     count=0
#     for i in range(2,n):
#         if n%i==0:
#             count=+1
#             break
#     if count ==0:
#         return n
#
# n=int(input("Enter how many wanted primes: "))
# for j in range(1,n):
#     res=is_prime(j)
#     if res is not None:
#         print(res,end=" ")
#     else:
#         continue
