# Analisis y diseño de algoritmos
Intergrantes: 
- Daniel Bolivar
- Jeremy Astaiza

## Ejecutar ejercicios:
```
# para ejecutar el ejercicio 1 correr:
python3 exercise1/main.py 

# para ejecutar el ejercicio 2 correr:
python3 exercise2/main.py 

```

# Soluciones
En las carpetas contenidas en este repositorio se encuentra cada una de las soluciones de los ejercicios.

## Enunciados ejercicios

### Ejercicio 1
Link: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies. More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords. All edges along the path to a character contain a code digit. If they are on the left side of the tree, they will be a 0 (zero). If on the right, they'll be a 1 (one). Only the leaves will contain a letter and its frequency count. All other nodes will contain a null instead of a character, and the count of the frequency of all of it and its descendant characters.

For instance, consider the string ABRACADABRA. There are a total of 11 characters in the string. This number should match the count in the ultimately determined root of the tree. Our frequencies are A=5, B=2, R=2, C=1 and D=1. The two smallest frequencies are for C and D, both equal to 1, so we'll create a tree with them. The root node will contain the sum of the counts of its descendants, in this case 1+1=2. The left node will be the first character encountered, C, and the right will contain D. Next we have 3 items with a character count of 2: the tree we just created, the character B and the character R. The tree came first, so it will go on the left of our new root node. B will go on the right. Repeat until the tree is complete, then fill in the 1's and 0's for the edges. The finished graph looks like:

```
                φ,11
               /    \
             0/      \1
             /        \
           A,5        φ,6
                      /    \
                    0/      \1
                    /        \
                  R,2        φ,4
                             /    \
                           0/      \1
                           /        \
                         φ,2        B,2
                        /    \
                      0/      \1
                      /        \
                    C,1        D,1
```

Input characters are only present in the leaves. Internal nodes have a character value of φ (NULL). We can determine that our values for characters are:

```
A - 0
B - 111
C - 1100
D - 1101
R - 10
```

Our Huffman encoded string is:

```
A B     R A C    A D   A B   R A
0 111 10 0 1100 0 1101 0 111 10 0
or
0111100110001101011110100
```

To avoid ambiguity, Huffman encoding is a prefix free encoding technique. No codeword appears as a prefix of any other codeword.

To decode the encoded string, follow the zeros and ones to a leaf and return the character there.

You are given pointer to the root of the Huffman tree and a binary coded string to decode. You need to print the decoded string.

**Function Description**

Complete the function decode_huff in the editor below. It must return the decoded string.

decode_huff has the following parameters:
- root: a reference to the root node of the Huffman tree
- s: a Huffman encoded string

**Input Format**

There is one line of input containing the plain string, s. Background code creates the Huffman tree then passes the head node and the encoded string to the function.

**Constraints**
```
  1 <= |s| <= 25
```

**Output Format**

Output the decoded string on a single line.

**Sample Input**
```
Binary Tree:
              φ,5
             /    \
           0/      \1
           /        \
         φ,2        A,3
        /    \
      0/      \1
      /        \
    B,1        C,1

s = "1001011"
```

**Sample Output**
```
ABACA
```

**Explanation**

```
S="1001011"
Processing the string from left to right.
S[0]='1' : we move to the right child of the root. We encounter a leaf node with value 'A'. We add 'A' to the decoded string.
We move back to the root.

S[1]='0' : we move to the left child.
S[2]='0' : we move to the left child. We encounter a leaf node with value 'B'. We add 'B' to the decoded string.
We move back to the root.

S[3] = '1' : we move to the right child of the root. We encounter a leaf node with value 'A'. We add 'A' to the decoded string.
We move back to the root.

S[4]='0' : we move to the left child.
S[5]='1' : we move to the right child. We encounter a leaf node with value 'C'. We add 'C' to the decoded string.
We move back to the root.

S[6] = '1' : we move to the right child of the root. We encounter a leaf node with value 'A'. We add 'A' to the decoded string.
We move back to the root.

Decoded String = "ABACA"
```

### Ejercicio 2
Link: https://www.hackerrank.com/challenges/is-binary-search-tree/problem

For the purposes of this challenge, we define a binary tree to be a binary search tree with the following ordering requirements:

- The data value of every node in a node's left subtree is less than the data value of that node.
- The data value of every node in a node's right subtree is greater than the data value of that node.

Given the root node of a binary tree, can you determine if it's also a binary search tree?

**Function Description**

Complete the function in your editor below, which has 1 parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete the challenge.

**Input Format**

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

**Constraints**
```
  0 <= data <= 10^4
```

**Output Format**

You are not responsible for printing any output to stdout. Your function must return true if the tree is a binary search tree; otherwise, it must return false. Hidden code stubs will print this result as a Yes or No answer on a new line.

**Sample Input**
```
Binary Tree:
        3
       / \
      5   2
     / \   \
    1   4   6
```

**Sample Output**
```
No
```
</document_content></document>