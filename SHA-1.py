########################
#   To do:
#         Addition needs to be 2 mod 32
#
########################


import math, binascii, random



# Some bitwise logical functions for later.
def ROTL(x, n, w):
  return((x << n & (2 ** w - 1)) | (x >> w - n))

def Ch(x, y, z):
  return((x & y) ^ (~x & z))

def Parity(x, y, z):
  return(x ^ y ^ z)

def Maj(x, y, z):
  return((x & y) ^ (x & z) ^ (y & z))







# Spec defines consts in hex to fill list k of length 80 split as below.
K = []

for t in range(80):
    if  t <= 19:
        K.append(0x5a827999)
    elif    t <= 39:
        K.append(0x6ed9eba1)
    elif    t <= 59:
        K.append(0x8f1bbcdc)
    else:
        K.append(0xca62c1d6)

# Spec defines values for H.
H = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]





# Read in .txt file and convert to hex.
in_file = open("small.txt", "r")
binary_file = str(''.join(format(ord(x), 'b') for x in in_file.read()))
#print(binary_file)
#print(hex_file)





# Add the length of the message in binary up to 64 bits to the end, totaling 512 bits.
bin_file_length = bin(len(binary_file))
bin_pad = str(bin_file_length[2:]) # Remove the "0b" from binary conversion.


while len(bin_pad) <= 63:
    bin_pad = "0" + bin_pad



# Pad binary file until its a multiple of 512 bits including padding. "1" will be added below.
while (len(binary_file) + 1 + len(bin_pad)) % 512 != 0:
    bin_pad = "0" + bin_pad

# Padding starts with a "1".
bin_pad = "1" + bin_pad
# Add the padding to the file
binary_file = binary_file + bin_pad

# The input above is then split into M - 512 bit chunks.
M = []
i = 0

while i + 512 <= len(binary_file):
    M.append(binary_file[i : i + 512])
    i += 512


# Process each m 512 bit block.
for m in M:
  i = 0
  messageBlock = []
  # Split the message M into 16x 32bit blocks.
  while i <= 511:
    messageBlock.append(m[i:i+32])
    i += 32



# Prepare the message schedule
  W = []
  for j in range(80):
    if j <= 15:
      W.append(int(messageBlock[j]))
      print(W)
    else:
      W.append(ROTL(W[j-3] + W[j-8] + W[j-14] + W[j-16], 1, 32))
  
  print("W: " + str(W)) # Is this correct?

#init the working variables
  a = H[0]
  b = H[1]
  c = H[2]
  d = H[3]
  e = H[4]
