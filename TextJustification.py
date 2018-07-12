"""
For this problem, we would like you to think of a single line of text, and justify that text into a buffer.
"""

def justify(line, length):
    """
    :param line: String(the string to be justified)
    :param length: Integer(Size of Buffer)
    :return: String(the justified output of the given line according to the Buffer size)
    """

    # Assuming the given line will always be less than of equal to the buffer size.
    # If the given line is greater than or equal to the buffer size, I will return the line as it is.
    if len(line) >= length:
        return line
    temp = line.replace(" ", "")
    diff = length - len(temp)
    tokenize = line.split()
    min_space = diff // (len(tokenize) - 1)
    extra_space = diff % (len(tokenize) - 1)
    result = ""+ tokenize[0]
    for word in tokenize[1:]:
        result += (" " * min_space) + word

    # print(len(line),len(tokenize), diff, min_space, extra_space)
    start = 0
    if extra_space:
        while extra_space > 0:
            i = result.find(" ", start)
            result = result[:i] + " " + result[i:]
            start = i + min_space + 1
            extra_space -= 1

    return result

def run_tests():
    print('Testcases running: ')
    # test if larger than buffer size string returns the original string
    assert(justify('I am a bird', 8) == 'I am a bird')
    print('Assertion 1 succeeded.')
    # test if smaller than buffer size string get's formatted correctly
    assert(justify('I am a bird', 14) == 'I  am  a  bird')
    assert(justify('I am a bird', 15) == 'I   am  a  bird')
    print('Assertion 2 succeeded.')
    # test is a string the same size as the buffer gets printed as is
    assert(justify('I am a bird', 11) == 'I am a bird')
    print('Assertion 3 succeeded.')
    return

run_tests()