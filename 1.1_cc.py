def caesar_encrypt(text, shift):
  result = ""
  for char in text:
    if char.isalpha():
    base = ord('A') if char.isupper() else ord('a')
    result += chr((ord(char) - base + shift) % 26 + base)
    else:
    result += char
  return result
def caesar_decrypt(cipher, shift):
  return caesar_encrypt(cipher, -shift)
plain_text = "Hello, World!"
shift_key = 3
encrypted = caesar_encrypt(plain_text, shift_key)
decrypted = caesar_decrypt(encrypted, shift_key)
print("Plain Text :", plain_text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
