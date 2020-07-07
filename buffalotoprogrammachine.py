import sys

from buffaloparse import parse, parses
from programmachine import Register, Instructions
import re

def buf_to_binary(string):
    if string == "Buffalo":
        return 1
    elif string == "buffalo":
        return 0
    else:
        raise TypeError('must be Buffalo or buffalo')

def reverse_binary_to_decimal(bin_list):
    decimal = 0
    for i, val in enumerate(bin_list):
        decimal += int(val)*2**(i)
    return decimal

def buf_list_to_binary(buf_list):
    decimal_list = [buf_to_binary(buf) for i, buf in enumerate(buf_list) if i%2==0]
    return reverse_binary_to_decimal(decimal_list)

def interpret(program):
    # remove comments
    program = re.split(r'(🐃[\S\s]*?🐃)', program)
    program = ''.join(map(lambda x: '' if '🐃' in x else x, program))
    # Separate sentencesedm 
    program = program.split('.')
    program = list(filter(lambda x: x not in ['','\n'], program))
    # check that each sentence parses. If not, just add more trailing buffalos
    for i, statement in enumerate(program):
        if not parses(statement):
            raise RuntimeError(f'Line {i+1}: "{statement}" does not parse')
    interpreted = []
    # The first two sentences are interpreted as a binary number
    # (except for the first two words, fixed as "Buffalo buffalo")
    # initialising the registers with a value.
    interpreted.append(f'buffalo {buf_list_to_binary(program[0].split()[2:])}')
    interpreted.append(f'Buffalo {buf_list_to_binary(program[1].split()[2:])}')
    interpreted.append('')
    for statement in program[2:]:
        statement = statement.split()
        # If the first variable token is Buffalo, instruction is JZ
        if statement[2] == 'Buffalo':
            instruction = 'JZ'
            # register to check for zero is second variable token
            register = statement[4]
            # rest of variable tokens binary encode line number to jump to
            Z = buf_list_to_binary(statement[6:])
            interpreted.append(' '.join([instruction, register, str(Z)]))
        else:
            # If first variable token not buffalo, second variable token
            # tells us whether instruction is INC or DEC
            if statement[4] == 'Buffalo':
                instruction = 'INC'
            elif statement[4] == 'buffalo':
                instruction = 'DEC'
            # register to act on is third variable token
            register = statement[6]
            interpreted.append(' '.join([instruction, register]))
    return '\n'.join(interpreted)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1][-4:] != '.buf':
            filepath = str(sys.argv[1]) + '.buf'
        else:
            filepath = str(sys.argv[1])

        with open(filepath, 'r') as f:
            string = f.read()

    elif len(sys.argv) == 1:
        string = sys.stdin.read()
    else:
        print(f'usage: {sys.argv[0]} <src>\nor cat <src.buf> | {sys.argv[0]}')
        sys.exit(1)

    instructions = Instructions(interpret(string))
    print(f'Initial Register Values\n-----------------------')
    registers = instructions.registers
    for key, val in zip(registers.keys(),
                        [str(register.value) for register in registers.values()]):
                    print(f'{key}: {val}')
    print()
    instructions_with_linenumbers = [f'{i+1}: {" ".join(instructions.instruction_list[i])}' for i in range(len((instructions.instruction_list)))]
    instruction_print = '\n'.join(instructions_with_linenumbers)
    print(f"""Instructions
------------
{instruction_print}
    """)
    print("Run program\n-----------")
    instructions.interpret()
    

