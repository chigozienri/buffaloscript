#!/usr/bin/env python3

import sys

class Register():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

registers = dict()

class Instructions():
    def __init__(self, instruction_string):
        self.instruction_string = instruction_string
        self.registers = dict()
        init_code_split = instruction_string.split('\n\n')
        if len(init_code_split) > 2:
            raise RuntimeError('only one double line break allowed in input')
        if len(init_code_split) == 2:
            lines = init_code_split[0].split('\n')
            for line in lines:
                line = line.split()
                if len(line) != 2:
                    raise RuntimeError('register definition lines must have format "my_register 1"')
                self.registers[line[0]] = Register(int(line[1]))
            
            self.instruction_list = init_code_split[1].split('\n')
        else:
            self.instruction_list = init_code_split[0].split('\n')
            
        self.instruction_list = \
            [x for x in self.instruction_list if x is not '']
        for i, instruction in enumerate(self.instruction_list):
            self.instruction_list[i] = instruction.split()

    def __str__(self):
        printable = [' '.join(instruction) \
                     for instruction in self.instruction_list]
        return '\n'.join(printable)

    def interpret(self, instructions=None, i=0):
        if instructions == None:
            instructions = self

        registers = instructions.registers
        
        if int(i)+1 > len(self.instruction_list):
            print('line number out of range, halting\n')
            print('Final Register Values on Halt\n-----------------------------')
            for key, val in zip(registers.keys(),
                    [str(register.value) for register in registers.values()]):
                print(f'{key}: {val}')
            return registers
        
        else:
            instruction = self.instruction_list[i]

        if not instruction[1] in registers:
            registers[instruction[1]] = Register(0)
            print(f'creating register {instruction[1]}' + \
                  f', initial value {registers[instruction[1]]}')

        r = registers[instruction[1]]

        if instruction[0] == 'JZ':
            if r.value == 0:
                print(f'line {i+1}:',
                      f'register {instruction[1]} is empty, ' + \
                      f'moving to line {instruction[2]}')
                self.interpret(instructions, int(instruction[2])-1)
            else:
                print(f'line {i+1}:',
                      f'register {instruction[1]} is not empty, ' + \
                      'doing nothing')
                self.interpret(instructions, i+1)
                
        else:
            if instruction[0] == 'INC':
                print (f'line {i+1}:',
                       f'increasing register {instruction[1]}' + \
                       f' from {registers[instruction[1]]}' + \
                       f' to {str(registers[instruction[1]].value+1)}')
                r.inc()
            elif instruction[0] == 'DEC':
                print (f'line {i+1}:',
                       f'decreasing register {instruction[1]}' + \
                       f' from {registers[instruction[1]]}' + \
                       f' to {str(registers[instruction[1]].value-1)}')
                r.dec()
            self.interpret(instructions, i+1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1][-4:] != '.prg':
            filepath = str(sys.argv[1]) + '.prg'
        else:
            filepath = str(sys.argv[1])

        with open(filepath, 'r') as f:
            string = f.read()

    elif len(sys.argv) == 1:
        string = sys.stdin.read()
    else:
        print(f'usage: {sys.argv[0]} <src>\nor cat <src.prg> | {sys.argv[0]}')
        sys.exit(1)
    
    instructions = Instructions(string)

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
    

