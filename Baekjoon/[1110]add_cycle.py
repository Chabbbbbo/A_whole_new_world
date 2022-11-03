origin = input()
sep = list(origin)
if len(sep) == '1':
    sep[0] = '0'

cycle = 1
while True:
    print(f'cycle{cycle}, origin{origin}')
    a,b = map(int, sep)
    print(a,b)
    num = a+b
    if origin == str(num):
        print(cycle)
        break
    else:
        if num < 10:
            sep = [b, num]
        else:
            sep = list(str(num))
        print(f'num{num}, sep{sep}')
        cycle += 1
    if cycle > 5:
        break