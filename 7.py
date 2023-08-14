valide = '[]{{{([](()))}}(())}'
not_valid = '[)]'
not_valid_2 = ')'


def check(s):
    stack = []
    inverser = {')':'(','}':'{',']':'['}

    for ch in s:
        if ch not in ['(','{','[',')','}',']']:
            return False

        if ch in ['(','{','[']:
            stack.append(ch)
        elif len(stack)>0:
            if stack[-1] != inverser[ch]:
                return False
            stack = stack[:-1]
        else:
            return False
    return len(stack) == 0

print(check(valide))
print(check(not_valid))
print(check(not_valid_2))