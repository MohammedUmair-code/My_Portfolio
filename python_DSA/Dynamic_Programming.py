#Fibonacci Sequence


# def fib(n):
#     # global counter
#     # counter += 1 
#     if n==0 or n==1:
#         return n
#     return fib(n-1) + fib(n-2)



# print("\nFib of", n, "=", fib(n))
# print("\nCounter: ", counter)

# memo = [None] * 100
# counter = 0
# def fib_memo(n):
#     global counter 
#     counter += 1 

#     if memo[n] is not None:
#         return memo[n]
    
#     if n ==0 or n== 1:
#         return n
#     memo[n] = fib_memo(n-1) + fib_memo(n-2)
#     return memo[n]

# n = 99  #69 [(2*35)-1]
# # fib_memo(n) Why this is giving a extra counter????
# print("\nFib of", n, "=", fib_memo(n))
# print("\nCounter: ", counter)


#BottomUp
counter = 0
def fib_bottom_up(n):
    fib_list = [0, 1]
    global counter 

    for index in range(2, n+1):
        counter += 1
        next_fib = fib_list[index-1] + fib_list[index-2]
        fib_list.append(next_fib)
    return fib_list[n]

n = 35
print("Fib of", n, "=", fib_bottom_up(n))
print("Counter:", counter)