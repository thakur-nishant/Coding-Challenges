import sys

def is_balanced(input):
    # Write your solution here
    stack = []
    opening = set(['(', '[', '{', '"', "'"])
    closing = set([')', ']', '}'])
    dic = {'(': ')', '[': ']', '{': '}'}
    i = 0
    while i < len(input):
        print(i, input[i])
        if input[i] == "\\":
            i += 2
            continue
        if input[i] in opening:
            if input[i] == '"':
                end = input[i+1:].find('"')
                if end == -1:
                    return False
                i = end + i + 2
            elif input[i] == "'":
                end = input[i+1:].find("'")
                if end == -1:
                    return False
                i = end + i + 2
            else:
                stack.append(input[i])
                i += 1
        else:
            if input[i] not in closing:
                i += 1
                continue
            if not stack:
                return False
            elif input[i] == dic[stack[-1]]:
                stack.pop()
            else:
                return False
            i += 1

    return stack == []


def main(ip):
    for input in ip:
        balanced = "true" if is_balanced(input) else "false"
        print(input, balanced)


if __name__ == "__main__":
    ip = ['()', '{[]}', '{}[]', '{}(',"", '"abc"', "'([]'", '[]{"abc["', '[]{"abc["}()', '"', '\\"abc"', '\\}{()}', '{{{"abcd}}}"}}}']
    main(ip)
