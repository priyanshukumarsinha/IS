import struct
def rotr(x, n): return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF
def generate_constants():
   k, n = [], 2
   while len(k) < 64:
     if all(n % d for d in range(2, int(n**0.5)+1)):
       k.append(int((n ** (1/3)) * (1 << 32)) & 0xFFFFFFFF)
     n += 1
   return k
def pad_message(msg):
   ml = len(msg) * 8
   msg += b'\x80'
   pad_len = (56 - len(msg) % 64) % 64
   msg += b'\x00' * pad_len + ml.to_bytes(8, 'big')
   return msg
def sha256_block(chunk, h, k):
   w = list(struct.unpack('>16L', chunk)) + [0]*48
   for i in range(16, 64):
     s0 = rotr(w[i-15], 7) ^ rotr(w[i-15], 18) ^ (w[i-15] >> 3)
     s1 = rotr(w[i-2], 17) ^ rotr(w[i-2], 19) ^ (w[i-2] >> 10)
     w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF
   a, b, c, d, e, f, g, h1 = h
   for i in range(64):
     S1 = rotr(e,6) ^ rotr(e,11) ^ rotr(e,25)
     ch = (e & f) ^ (~e & g)
     temp1 = (h1 + S1 + ch + k[i] + w[i]) & 0xFFFFFFFF
     S0 = rotr(a,2) ^ rotr(a,13) ^ rotr(a,22)
     maj = (a & b) ^ (a & c) ^ (b & c)
     temp2 = (S0 + maj) & 0xFFFFFFFF
     a, b, c, d, e, f, g, h1 = (
     (temp1 + temp2) & 0xFFFFFFFF, a, b, c, (d + temp1) & 0xFFFFFFFF, e, f, g
     )
   for i, val in enumerate([a, b, c, d, e, f, g, h1]):
     h[i] = (h[i] + val) & 0xFFFFFFFF
def sha256(msg):
   k = generate_constants()
   h = [
   0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
   0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
   ]
   msg = pad_message(msg)
   for i in range(0, len(msg), 64):
     sha256_block(msg[i:i+64], h, k)
   return b''.join(x.to_bytes(4, 'big') for x in h)
if __name__ == '__main__':
   msg = input("Enter message: ").encode()
   print("SHA-256 Hash:", sha256(msg).hex())
