import bsc
import numpy as np


def file_to_string(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def string_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_string(binary_string):
    return "".join([chr(int("".join(binary_string[i:i + 8]), 2)) for i in range(0, len(binary_string), 8)])


def repetition_code_coder(text):
    binary_string = string_to_binary(text)
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


def repetition_code(text, p):
    coded = repetition_code_coder(text)

    transmitted_string = bsc.bsc(coded, p)

    decoded = repetition_code_decoder(transmitted_string)
    toReturn = binary_to_string(decoded)
    print("The value of BER is", BER(text, toReturn))
    return decoded


def hamming_code(text, p):
    coded = hamming_coder(text)
    transmitted_string = bsc.bsc(coded, p)

    decoded = hamming_decoder(transmitted_string)

    toReturn = binary_to_string(decoded)
    print("The value of BER is", BER(text, toReturn))
    return toReturn


def hamming_coder(text):
    binary_string = string_to_binary(text)
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
        e = error_pattern(code_word)
        temp = str(code_word)
        if e != 0:
            temp = ""
            for j in range(len(code_word)):
                temp += str(int(code_word[j]) ^ int(e[j]))
        decoded_string += temp[:7 - 3]
    return decoded_string


def error_pattern(a):
    h = [[0, 1, 1],
         [1, 1, 0],
         [1, 0, 1],
         [1, 1, 1],
         [1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]
    array = [0, 0, 0]
    for i in range(3):
        temp = 0
        for j in range(len(a)):
            if h[j][i] * int(a[j]) == 1:
                temp ^= 1
        array[i] = temp
    if array == [0, 0, 0]:
        return 0
    index = h.index(array)
    to_return = ""
    for i in range(len(a)):
        if i == index:
            to_return += "1"
        else:
            to_return += "0"
    return to_return


def exercise_1a():
    for j in range(1, 5):
        file_name = "file" + str(j) + ".txt"
        text = file_to_string(file_name)
        for i in range(1, 6):
            print("\n\nFile: " + file_name + " with BER: 10^" + str(-i) + " without interleaving\n\n")
            print("- BER1, entre a entrada e a saída do BSC, sem controlo de erros:")
            bsc.bsc(string_to_binary(text), pow(10, -i))
            print("\n- BER2, após a aplicação de código de repetição (3, 1) sobre o BSC, em modo de correção:")
            repetition_code(text, pow(10, -i))
            print("\n- BER3, após a aplicação de código de Hamming (7, 4) sobre o BSC, em modo de correção:")
            hamming_code(text, pow(10, -i))


def exercise_1b():
    for j in range(1, 5):
        file_name = "file" + str(j) + ".txt"
        text = file_to_string(file_name)
        string_length = len(file_name)
        sqrt_length = int(string_length ** 0.5)
        num_lines = 0
        num_columns = 0
        for i in range(sqrt_length, 0, -1):
            if string_length % i == 0:
                num_lines = i
                num_columns = string_length // i
                break

        for i in range(1, 6):
            print("\n\nFile: " + file_name + " with BER: 10^" + str(-i) + " with interleaving\n\n")
            print("- BER1, entre a entrada e a saída do BSC, sem controlo de erros:")
            bsc.interleaving(text, num_lines, num_columns)
            bsc.bsc(string_to_binary(text), pow(10, -i))
            bsc.interleaving(text, num_columns, num_lines)
            print("\n- BER2, após a aplicação de código de repetição (3, 1) sobre o BSC, em modo de correção:")
            bsc.interleaving(text, num_lines, num_columns)
            repetition_code(text, pow(10, -i))
            bsc.interleaving(text, num_columns, num_lines)
            print("\n- BER3, após a aplicação de código de Hamming (7, 4) sobre o BSC, em modo de correção:")
            bsc.interleaving(text, num_lines, num_columns)
            hamming_code(text, pow(10, -i))
            bsc.interleaving(text, num_columns, num_lines)


def BER(original, received):
    errors = 0
    o = string_to_binary(original)
    r = string_to_binary(received)
    for i in range(len(o)):
        if o[i] != r[i]:
            errors += 1
    return errors / len(o)


def main():
    exercise_1b()


if __name__ == '__main__':
    main()
