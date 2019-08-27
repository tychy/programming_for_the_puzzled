# Run Length Encoding

input_str = 'BWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWBWWWW'


def runlengthencoder(input):
    if len(input) < 1:
        return input
    input = input + 'A'
    encoded = ''
    length = 1
    start = 0
    for i in range(1, len(input)):
        if input[i] != input[start]:
            encoded = encoded + str(length) + input[start]
            start = i
            length = 1
        else:
            length += 1
    return encoded


def runlengthdecoder(input):
    if len(input) < 2:
        return input
    
    length = 0
    decoded = ''
    for i in range(len(input)):
        if not input[i].isalpha():
            length = length * 10 + int(input[i])
            continue
        else:
            decoded = decoded + input[i] * length
            length = 0
    return decoded

encoded = runlengthencoder(input_str)
print(encoded)

decoded = runlengthdecoder(encoded)
print(decoded)