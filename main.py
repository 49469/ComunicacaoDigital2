import bsc
import numpy as np


def file_to_string(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def repetition_code_coder(text):
    binary_string = ''.join(format(ord(c), '08b') for c in text)
    print(binary_string)
    coded_string = ""
    for i in binary_string:
        for j in range(3):
            coded_string += i
    return coded_string


def repetition_code_decoder(text):
    decoded_string = ""
    for i in range(0, len(text) - 1, 3):
        zero = 0
        for j in range(3):
            if text[i + j] == '0':
                zero += 1
        if zero >= 2:
            decoded_string += '0'
        else:
            decoded_string += '1'
    return decoded_string


def hamming_code(file_name, p):
    text = file_to_string(file_name)
    coded = hamming_coder(text)
    transmitted_string = bsc.bsc(coded, p)
    decoded = hamming_decoder(transmitted_string)
    toReturn = ""
    for i in range(0, len(decoded), 8):
        toReturn += chr(int(decoded[i:i + 8], 2))
    print("The value of BER is", BER(text, toReturn))
    print(decoded)
    return toReturn


def repetition_code(file_name, p):
    text = file_to_string(file_name)
    coded = repetition_code_coder(text)
    transmitted_string = bsc.bsc(coded, p)
    decoded = repetition_code_decoder(transmitted_string)
    return decoded


def hamming_coder(text):
    binary_string = ''.join(format(ord(c), '08b') for c in text)
    print(binary_string)
    coded_string = ""
    for i in range(0, len(binary_string), 4):
        b0 = int(binary_string[i + 1]) ^ int(binary_string[i + 2]) ^ int(binary_string[i + 3])
        b1 = int(binary_string[i + 0]) ^ int(binary_string[i + 1]) ^ int(binary_string[i + 3])
        b2 = int(binary_string[i + 0]) ^ int(binary_string[i + 2]) ^ int(binary_string[i + 3])
        for j in range(4):
            coded_string += binary_string[i + j]
        coded_string += str(b0) + str(b1) + str(b2)
    return coded_string


def hamming_decoder(text):
    decoded_string = ""
    for i in range(0, len(text), 7):
        code_word = text[i + 0] + text[i + 1] + text[i + 2] + text[i + 3] + text[i + 4] + text[i + 5] + text[i + 6]
        b2 = str(int(code_word[0]) ^ int(code_word[2]) ^ int(code_word[3]))
        b1 = str(int(code_word[0]) ^ int(code_word[1]) ^ int(code_word[3]))
        b0 = str(int(code_word[1]) ^ int(code_word[2]) ^ int(code_word[3]))
        if b0 != code_word[4] or b1 != code_word[5] or b2 != code_word[6]:
            a = [int(code_word[0]), int(code_word[1]), int(code_word[2]), int(code_word[3]),
                 int(code_word[4]), int(code_word[5]), int(code_word[6])]
            error = bin(error_pattern(a))
            error = error[len(error) - 2:]
            word = int(error) ^ int(code_word)
            size = len(str(word))
            decoded_string += str(word)[:size - 3]
        else:
            size = len(str(code_word))
            decoded_string += str(code_word)[:size - 3]
    return decoded_string


def error_pattern(a):
    h = [[0, 1, 1],
         [1, 1, 0],
         [1, 0, 1],
         [1, 1, 1],
         [1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]
    c = np.dot(a, h)
    c = np.array(c)
    array = [0, 0, 0]
    for i in range(len(c)):
        if c[i] > 1:
            array[i] = 1
    index = h.index(array)
    p = (len(h) - 1) - index
    to_return = pow(2, p)
    return to_return


def BER(original, received):
    errors = 0
    for i in range(len(original)):
        if original[i] != received[i]:
            o = ''.join(format(ord(c), '08b') for c in original)
            r = ''.join(format(ord(c), '08b') for c in received)
            for j in range(len(o)):
                if o[j] != r[j]:
                    errors += 1
    return errors / len(original)


def main():
    print(hamming_code("file1.txt", pow(10, -2)))


if __name__ == '__main__':
    main()
