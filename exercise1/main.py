
# Authors: Daniel Bolivar and Jeremy Astaiza
# Solution of problem: "Tree: Huffman Decoding" HackerRank https://www.hackerrank.com/challenges/tree-huffman-decoding/problem
from encode.encode import init

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

def decodeHuff(root, s):
    current = root
    decoded = ""

    for bit in s:

        if bit == '0':
            current = current.left
        else:
            current = current.right

        # Si es una hoja
        if current.left is None and current.right is None:
            decoded += current.data
            current = root

    return decoded

''' 
===========================================
Pruebas HackerRank
Test #1: input: 1001011 expected: ABACA
Test #2: input 001000001010111001110111011110010111111001001000110 expected: Rumpelstiltskin
Test #3: input 0100001110101110011101001100001101011001001011111011011001100001101111010100111110011101010011111001010101010011011001100001101111010100111110011100100101111101111010100111110001100001101101000 expected:  howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?
===========================================
'''

root1, s1 = init('ABACA')
root2, s2 = init('Rumpelstiltskin')
root3, s3 = init('howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?')

test1 = decodeHuff(root1, s1)
test2 = decodeHuff(root2, s2)
test3 = decodeHuff(root3, s3)

print("Test 1")
print("Result:", test1)
print()

print("Test 2")
print("Result:", test2)
print()

print("Test 3")
print("Result:", test3)


