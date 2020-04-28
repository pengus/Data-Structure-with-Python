from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i+1))

        if next in ")]}":
            if len(opening_brackets_stack) > 0:
                temp = opening_brackets_stack.pop()
                if  not are_matching(temp.char, next):
                    return (i+1)
            else:
                return (i+1)
            # Process closing bracket, write your code here
            pass
    if opening_brackets_stack:
        return (opening_brackets_stack.pop().position)

    return ('Success')


def main():
    text = input()
    mismatch = find_mismatch(text)
    print (mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
