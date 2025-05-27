def mod_exp(base, exp, mod):
   res = 1
   base %= mod
   while exp:
     if exp & 1:
       res = (res * base) % mod
     base = (base * base) % mod
     exp >>= 1
   return res
p = int(input("Prime p: "))
g = int(input("Primitive root g: "))
a = int(input("Alice private key a: "))
b = int(input("Bob private key b: "))
A = mod_exp(g, a, p)
B = mod_exp(g, b, p)
print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")
s_a = mod_exp(B, a, p)
s_b = mod_exp(A, b, p)
print(f"Alice's shared secret: {s_a}")
print(f"Bob's shared secret: {s_b}")
print("\nSuccess!" if s_a == s_b else "\nFailure.")
