def reverse_string(s):
    s = list(s)
    a = []
    i = 0
    while i < len(s): 
        # list is getting shorter so pay attention
        a.append(s.pop())

    return  "".join(a)

# print(reverse_string('denem'))

'''Problem
You're given a list of operations — either "push X" or "pop". Return the final stack.

Input Example
["push 1", "push 2", "pop", "push 3"]

Expected Output
[1, 3]
'''

def push_pop(arr):
    l = len(arr)
    stack = []
    for command in arr:
        msg = command.split(" ")[0]
        if msg == 'push':
            stack.append(command.split(" ")[1])
        elif msg == 'pop':
            stack.pop()
        else:
            print('incorrect input')
            break
        print(stack)
    return stack

# print(push_pop(["push 1", "push 2", "pop", "push 3"]))

'''Stack Problem: Track the Max Item
Problem (Easy-Medium)
You're given a list of operations — "push X" or "pop".
Return a list of the maximum item in the stack after each operation.

Input Example
["push 1", "push 5", "push 3", "pop", "push 6"]

Expected Output (Max after each op)
[1, 5, 5, 5, 6]

Use your regular stack to hold the numbers.
Also keep a second stack to track the max so far.
Every time you push:
Add the item to the main stack.
Compare with the current max, and push the new max to the max stack.
Every time you pop:
Pop from both stacks.
After each operation, the top of the max stack gives you the current maximum.'''

def track_max_stack(arr):
    stack = []
    max_stack = []
    top = []

    for command in arr:
        parts = command.split()
        if parts[0] == 'push':
            number = int(parts[1])
            stack.append(number)
            if not max_stack:
                max_stack.append(number)
            else:
                max_stack.append(max(number, max_stack[-1]))
        elif parts[0] == 'pop':
            if stack and max_stack:
                stack.pop()
                max_stack.pop()
        else:
            print('Incorrect command:', command)
            break

        if max_stack:
            top.append(max_stack[-1])

    return top

# track_max_stack(["push 1", "push 5", "push 3", "pop", "push 6"])

# track_max_stack(["pop", "push 1", "push 5", "push 3", "pop", "push 6"])

# track_max_stack(["push 1", "push 5", "push 3", "push 6"])


track_max_stack(["push 5", "pop", "push 3", "pop", "push 7", "push 0"])




