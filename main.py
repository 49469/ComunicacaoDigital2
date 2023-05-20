import exercicio5


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


def repetition_code(file_name, p):
    text = file_to_string(file_name)
    coded = repetition_code_coder(text)
    transmitted_string = exercicio5.bsc(coded, p)
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
    print(coded_string)


def main():
    hamming_coder("oi")
    # print(repetition_code("file1.txt", pow(10, -5)))
    # a = repetition_code_coder("oi")
    # print(a)
    # b = repetition_code_decoder(a)
    # print(b)
    # print(file_to_string("file4.txt"))
    # exercicio5.bsc(file_to_string("file4.txt"), 0.1)


if __name__ == '__main__':
    main()
