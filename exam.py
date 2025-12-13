# mod = 10**9 + 7
# def solve():
#     import sys, math
#     n, m = map(int, sys.stdin.read().split())
#     divs = []
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             divs.append(i)
#             if i*i != n:
#                 divs.append(n//i)
#     def phi(x):
#         r = x
#         i = 2
#         while i*i <= x:
#             if x % i == 0:
#                 while x % i == 0:
#                     x //= i
#                 r -= r // i
#             i += 1
#         if x > 1:
#             r -= r // x
#         return r
#     total = 0
#     for d in divs:
#         total = (total + phi(n//d) * pow(m, d,mod)) %mod
#     ans = total * pow(n,mod-2,mod) %mod
#     print(ans)
# solve()


# MOD = 10**9 + 7
# def solve():
#     import sys
#     n, m = map(int, sys.stdin.read().split())
#     divs = []
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             divs.append(i)
#             if i * i != n:
#                 divs.append(n // i)
#     def phi(x):
#         r = x
#         i = 2
#         while i * i <= x:
#             if x % i == 0:
#                 while x % i == 0:
#                     x //= i
#                 r -= r // i
#             i += 1
#         if x > 1:
#             r -= r // x
#         return r
#     total = 0
#     for d in divs:
#         total = (total + phi(n // d) * pow(m, d, MOD)) % MOD

#     ans = total * pow(n, MOD - 2, MOD) % MOD
#     print(ans)
# solve()


# MOD = 10**9 + 7
# def grid():
#     import sys
#     n=int(input())
#     n2 = n*n
#     f0 = pow(2, n2, MOD)
#     if n % 2 == 0:
#         f180 = pow(2, n2 // 2, MOD)
#     else:
#         f180 = pow(2, (n2 + 1) // 2, MOD)
#     if n % 2 == 0:
#         f90 = pow(2, n2 // 4, MOD)
#     else:
#         f90 = pow(2, (n2 + 3) // 4, MOD)
#     total = (f0 + f180 + 2 * f90) % MOD
#     inv4 = pow(4, MOD - 2, MOD)
#     print(total * inv4 % MOD)
# grid()


