IP = [
 58, 50, 42, 34, 26, 18, 10, 2,
 60, 52, 44, 36, 28, 20, 12, 4,
 62, 54, 46, 38, 30, 22, 14, 6,
 64, 56, 48, 40, 32, 24, 16, 8,
 57, 49, 41, 33, 25, 17, 9, 1,
 59, 51, 43, 35, 27, 19, 11, 3,
 61, 53, 45, 37, 29, 21, 13, 5,
 63, 55, 47, 39, 31, 23, 15, 7
]
DES_ROUNDS = 16
def permute(block: int, table: list) -> int:
   result = 0
   for i, pos in enumerate(table):
     bit = (block >> (64 - pos)) & 1
     result |= bit << (63 - i)
   return result
def feistel_function(half_block: int, key: int) -> int:
   return half_block ^ key
def key_schedule(key: int) -> list:
   return [key ^ (i + 1) for i in range(DES_ROUNDS)]
def des_round(block: int, key: int) -> int:
   left = (block >> 32) & 0xFFFFFFFF
   right = block & 0xFFFFFFFF
   new_right = feistel_function(right, key)
   return (new_right << 32) | left # Swap halves
def des_encrypt(block: int, key: int) -> int:
   round_keys = key_schedule(key)
   block = permute(block, IP)
   for rk in round_keys:
     block = des_round(block, rk)
   return block
def string_to_uint64(text: str) -> int:
   bytes_text = text.encode('utf-8')
   padded = bytes_text[:8].ljust(8, b'\x00')
   return int.from_bytes(padded, byteorder='little')
def uint64_to_hex_string(value: int) -> str:
   return f"0x{value:016X}"
plaintext = input("Enter 8-character plaintext: ")[:8]
key_text = input("Enter 8-character key: ")[:8]
pt_block = string_to_uint64(plaintext)
key_block = string_to_uint64(key_text) & 0xFFFFFFFFFFFFFF00 # Mimic C behavior
print(f"\nOriginal: {uint64_to_hex_string(pt_block)}")
encrypted = des_encrypt(pt_block, key_block)
print(f"Encrypted: {uint64_to_hex_string(encrypted)}")
