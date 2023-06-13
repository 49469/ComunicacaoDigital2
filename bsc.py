import numpy as np


def bsc(text, p):
    random_sequence = np.random.random(size=len(text))
    received_string = ""
    for i, bit in enumerate(text):
        if random_sequence[i] < p:
            flipped_bit = str(1 - int(bit))
            received_string += flipped_bit
        else:
            received_string += bit
    total = len(received_string)
    flipped_bits = p * total
    BER = flipped_bits / total
    print("BSC")
    print("The p value is", p)
    print("The BER value is", BER)
    print("BSC")
    return received_string


def interleaving(text, lines, col):
    if lines * col != len(text):
        return "error: lines*col must be equal to the size of text"
    matrix = []
    for i in range(lines):
        row = []
        for j in range(col):
            row.append(text[i * col + j])
        matrix.append(row)
    string = ""
    for c in range(col):
        for line in range(lines):
            a = matrix[line]
            string += (a[c])
    return string


def bsc_with_interleaving(string, p, l, c):
    if l * c != len(string):
        return "error: lines*col must be equal to the size of text"
    text_a = interleaving(string, l, c)
    a = ''.join(format(ord(c), '08b') for c in text_a)
    message = bsc(a, p)
    b = "".join([chr(int("".join(message[i:i + 8]), 2)) for i in range(0, len(message), 8)])
    text_b = interleaving(b, c, l)
    return text_b
