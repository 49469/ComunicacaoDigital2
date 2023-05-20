import numpy as np


def bsc(text, p):
    transmitted_string = text
    binary_string = ''.join(format(ord(c), '08b') for c in transmitted_string)
    random_sequence = np.random.random(size=len(binary_string))
    received_bits = []
    for i, bit in enumerate(binary_string):
        if random_sequence[i] < p:
            flipped_bit = str(1 - int(bit))
            received_bits.append(flipped_bit)
        else:
            received_bits.append(bit)
    received_string = "".join([chr(int("".join(received_bits[i:i + 8]), 2)) for i in range(0, len(received_bits), 8)])
    total = len(received_string)
    flipped_bits = p * total
    BER = flipped_bits / total
    print("The p value is", p)
    print("The BER value is", BER)
    print("Transmitted string: ", transmitted_string)
    print("Received string: ", received_string)
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


def exercise5b2(string, p, l, c):
    if l * c != len(string):
        return "error: lines*col must be equal to the size of text"
    text_a = interleaving(string, l, c)
    message = bsc(text_a, p)
    text_b = interleaving(message, c, l)
    return text_b


def main():
    print(bsc("Alices", 0.1))
    print(exercise5b2("Alices", 0.1, 2, 3))


if __name__ == '__main__':
    main()
