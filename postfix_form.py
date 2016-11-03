f1 = open('input.txt', 'rt')
st = f1.read()
f1.close()
st += ' '
nb = 0
stack = []
ch = ''
ind = 0
while ind < len(st):
    while st[ind] != ' ' and ind < len(st):
        ch += st[ind]
        ind += 1
    if ch in '-+*/':
        x1 = stack[nb - 2]
        x2 = stack[nb - 1]
        stack = stack[:-2]
        nb -= 1
        if ch == '-':
            res = x1 - x2
        elif ch == '+':
            res = x1 + x2
        elif ch == '*':
            res = x1 * x2
        elif ch == '/':
            res = x1 / x2
        stack += [res]
    else:
        nb += 1
        stack += [float(ch)]
    ch = ''
    ind += 1
f2 = open('output.txt', 'w')
f2.write(str(stack[0]))
f2.close()
