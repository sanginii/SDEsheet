def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insert_sorted(stack, temp)

def insert_sorted(stack, element):
    if not stack or element >= stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        insert_sorted(stack, element)
        stack.append(temp)

# Example usage:
stack = [3, 1, 4, 2]
sort_stack(stack)
print(stack)  # Output: [1, 2, 3, 4]
