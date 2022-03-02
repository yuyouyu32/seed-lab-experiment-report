#!/usr/bin/python3

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

MSG   = "4e6f0e0e0e0e0e0e0e0e0e0e0e0e0e0e" # No
IV1 = "ac96070668fc275a557f0f725c0c9174"
IV2 = "aaac907868fc275a557f0f725c0c9174"

# Convert ascii string to bytearray
# D1 = bytes(MSG, 'ascii')
D1 = bytearray.fromhex(MSG)
# Convert hex string to bytearray
D2 = bytearray.fromhex(IV1)
D3 = bytearray.fromhex(IV2)

r1 = xor(D1, D2)
r2 = xor(r1, D3)
print(r2)
print(r2.hex())
# print(r2.decode('ascii'))