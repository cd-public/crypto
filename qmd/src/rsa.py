def find_large_prime(k):
    is_prime = lambda n : any([n % i for i in range(2, int(n **.5))])
    candidate = 6 * k + 1
    # you need a prime tester
    while not is_prime(candidate):
        candidate += 6
    return candidate

def lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return a * b // gcd(a, b)

s = "C" # a random string
m = ord(s) # to number

hide_p = lambda: find_large_prime(10)
hide_q = lambda: find_large_prime(15)
n = hide_p() * hide_q()

hide_λ = lambda: lcm(hide_p() - 1,  hide_q() - 1)

e = 65537 # encryptor

def find_d():
    d = 1
    while 1 != (d * e % hide_λ()):
        d += 1
    return d

def modexp(m, e, n):
    if e == 0:
        return 1
    if e == 1:
        return m % n
    if e % 2:
        return (m * modexp(m*m % n, e//2, n)) % n
    return  modexp(m*m % n, e//2, n) % n

c = modexp(m, e, n) # ciphertext

new_m = modexp(c % n, find_d(), n)

print(chr(modexp(modexp(ord("C"), e, n), find_d(), n)))