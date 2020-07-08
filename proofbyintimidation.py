from buffaloparse import parses

# Check that the first 10000 possible buffalo script sentences parse in English.

max_i = 0
max_j = 0

def translate(digit):
    return 'Buffalo' if digit == '1' else 'buffalo'
for i in range(10000):
    binary = '{0:b}'.format(i)
    string = 'Buffalo buffalo ' + ' '.join(f"{translate(digit)} buffalo" for digit in binary)
    j = 0
    while not parses(string):
        string += ' buffalo'
        j += 1
    if j > max_j:
        max_j = j
        max_i = i
    print(f'{i} needed {j} extra trailing buffaloes')

print(f'Maximum trailing buffaloes needed was {max_j}, by {max_i}')