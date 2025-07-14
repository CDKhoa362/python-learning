def is_balanced_parentheses(string_parentheses):
    if len(string_parentheses) == 0:
        return True

    stack = []
    for char in string_parentheses:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0