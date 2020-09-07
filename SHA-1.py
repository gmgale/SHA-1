import math, binascii, random

# Read in .txt file and convert to hex
in_file = open("fileToBeHashed.txt", "r")

binary_file = int(''.join(format(ord(x), 'b') for x in in_file.read()))
hex_file = hex(binary_file)
#print(binary_file)
#print(hex_file)

# Generate 5x 8-char hex values for later
H = []
for i in range(5):
    x = hex(random.randint(0, 4294967295))
    H.append(x[2:])
#print(H)

# Pad binary file until 448bits long
bin_file_str = str(binary_file)
bin_file_str += "1"

while len(bin_file_str) < 448:
    bin_file_str += "0"
#print(bin_file_str)

# Add the length of the message in 64 bits to the end, totaling 512 bits.
# '{:064b}'.format(binary_file)
bin_file_length = str(binary_file)
while len(bin_file_length) < 64:
    bin_file_length = "0" + bin_file_length

# M = 512 bits. Message + 1 + Padding 0's + 64 bits of message length
# padded with 0's on left
M = bin_file_str + bin_file_length
#print(M)


# The input above is then split into 512 bit chunks (only 1 512 bit in this instance) - 
# Skipping that...
# Each chunk is then split into 16x 32 bit words.
W = []
start = 0
end = 31

while end <= 512:
    
    W.append(M[start:end])
    start += 32
    end += 32


# Let the hash begin.......

