import serial
import exercise1


def exercise_2a():
    portName = "COM4"
    ser = serial.Serial(portName, 9600)
    receive_data(ser)
    ser.close()


def get_fletcher16(data: str):
    """
    Accepts a string as input.
    Returns the Fletcher16 checksum value in decimal and hexadecimal format.
    8-bit implementation (16-bit checksum)
    """
    sum1, sum2 = int(), int()
    data = data.encode()
    for index in range(len(data)):
        sum1 = (sum1 + (data[index])) % 255
        sum2 = (sum2 + sum1) % 255
    result = (sum2 << 8) | sum1
    return {"Fletcher16_dec": result, "Fletcher16_hex": hex(result)}


def receive_data(ser):
    size = int(ser.readline().decode('utf-8').strip())
    with open('data1.txt', 'w') as f:
        for i in range(size):
            data = ser.readline().decode('utf-8').strip()
            print(data)
            f.write(data)
    f.close()


def exercise_2b():
    portName = "COM4"
    ser = serial.Serial(portName, 9600)
    receive_data(ser)
    checkSum = ser.readline().decode('utf-8').strip()
    ser.close()
    text = exercise1.file_to_string('data1.txt')
    binary = exercise1.string_to_binary(text)

    binary_list = list(binary)
    for i in range(0, len(binary_list), 10):
        if binary_list[i] == "1":
            binary_list[i] = "0"
        else:
            binary_list[i] = "1"

    binary_modified = ''.join(binary_list)

    decoded = exercise1.binary_to_string(binary_modified)

    fletcher32 = get_fletcher16(decoded)
    print("checkSum Arduino: " + checkSum)
    print(fletcher32)


def s():
    a = 123
    b = 0
    while a > 0:
        b 


def main():
    exercise_2b()


if __name__ == '__main__':
    main()
