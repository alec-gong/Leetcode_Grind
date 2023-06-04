def validparen(s):
    openclose = { "}":"{", ")":"(", "]":"[" }
    stack = []

    for c in s:
        if c in openclose:
            if stack and stack[-1] == openclose[c]:
                stack.pop()
            else:
                return False
        elif c in openclose.values():
            stack.append(c)
    return not stack