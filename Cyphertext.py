def encodeString(s):

    az_lower = []
    az_upper = []
    string = s
    encoded_string = ""+s[0]
    for i in range(26):
        az_lower.append(chr(97+i))
        az_upper.append(chr(65+i))
    prev_char_val = 0
    prev_num_val = 0
    if s[0].isalpha():
        prev_char_val = az_lower.index(string[0].lower())
    num_flag = True

    for i in range(1,len(s)):
        if s[i].isalnum():
            if s[i].isupper():
                curr_val = az_upper.index(s[i])
                encoded_val = encode(curr_val,prev_char_val)
                encoded_string += az_upper[encoded_val]
                prev_char_val = encoded_val
            elif s[i].islower():
                curr_val = az_lower.index(s[i])
                encoded_val = encode(curr_val, prev_char_val)
                encoded_string += az_lower[encoded_val]
                prev_char_val = encoded_val
            else:
                curr_val = int(s[i])
                if num_flag:
                    encoded_string += str(curr_val)
                    num_flag = False
                else:
                    encoded_string += str((prev_num_val + curr_val)%10)
                prev_num_val = 9 - curr_val
        else:
            encoded_string += str(s[i])

    return encoded_string

def encode(curr, prev):
    sum = curr + prev
    return sum % 26


s = 'Hello World!'
# s = 'x1 = y2'
x = encodeString(s)
print(x)
