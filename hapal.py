import heapq
import pickle
import os
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    [(_freq, _count, root)] = h
    code = {}
    root.walk(code, "")
    return code


def action(name, ty):
    if ty == "-e":
        with open(name, "r", encoding="utf-8") as F:
            text = F.read()
            code = huffman_encode(text)
            encoded = "".join(code[ch] for ch in text)
        overhead = (8 - len(encoded) % 8)
        encoded += overhead * '0'
        binary = []
        for i in range(len(encoded) // 8):
            binary += [int(encoded[8 * i: (i + 1) * 8], 2)]

        with open(os.path.splitext(name)[0] + ".par", "wb") as F:
            F.write(pickle.dumps(code))
            F.write("\r\n\r\n".encode())
            # F.write(bytes(overhead))
            F.write(bytes([overhead]) + bytes(binary))
    else:
        with open(name, "rb") as F:
            data, binary = F.read().split("\r\n\r\n".encode())
            data = pickle.loads(data)
            data = {b: a for a, b in data.items()}
            overhead = binary[0]
            # print(overhead)
            binary = ''.join([bin(i)[2:].rjust(8, '0') for i in binary[1:]])
            current = ""
            decoded = ""

            for i in binary[0: -overhead]:
                if current in data:
                    decoded += data[current]
                    current = i
                else:
                    current += i
            decoded += data[current]

        with open(os.path.splitext(name)[0] + ".txt", "w", encoding="utf-8") as F:
            F.write(decoded)
