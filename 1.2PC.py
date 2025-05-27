def create_matrix(key):
   key = key.lower().replace('j','i')
   s = "".join(dict.fromkeys([c for c in key if c.isalpha()]))
   alphabet = "abcdefghiklmnopqrstuvwxyz"
   matrix = (s + "".join([c for c in alphabet if c not in s]))
   return [list(matrix[i*5:(i+1)*5]) for i in range(5)]
def find_pos(matrix, c):
   for i in range(5):
     for j in range(5):
       if matrix[i][j] == c:
   return i,j
def prepare(text):
   text = text.lower().replace('j','i')
   text = "".join([c for c in text if c.isalpha()])
   i, res = 0, ""
   while i < len(text):
     a = text[i]
     b = text[i+1] if i+1 < len(text) and text[i+1] != a else 'x'
     res += a + b
     i += 2 if b != 'x' else 1
   if len(res) % 2: res += 'x'
   return res
def playfair(text, matrix, enc=True):
   text = prepare(text) if enc else text
   res = ""
   step = 1 if enc else -1
   for i in range(0, len(text), 2):
     r1,c1 = find_pos(matrix, text[i])
     r2,c2 = find_pos(matrix, text[i+1])
     if r1 == r2:
       res += matrix[r1][(c1+step)%5] + matrix[r2][(c2+step)%5]
     elif c1 == c2:
       res += matrix[(r1+step)%5][c1] + matrix[(r2+step)%5][c2]
     else:
       res += matrix[r1][c2] + matrix[r2][c1]
   return res
key = input("Key: ")
text = input("Text: ")
m = create_matrix(key)
print("Matrix:")
for row in m: print(" ".join(row))
enc = playfair(text, m)
dec = playfair(enc, m, False)
print("Encrypted:", enc)
print("Decrypted:", dec)
