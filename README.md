# buffaloscript
A programming language that uses only the tokens "Buffalo", "buffalo", " " and ".". Each program must also be grammatically correct in English. Based on Minsky's Program Machine (1967)

Currently written as a Domain Specific Language in Python

This started when I realised that
```
alias buffalo="grep"
echo "buffalo" > buffalo; buffalo buffalo buffalo
```
gives the output "buffalo" in bash, and that any desired number of trailing buffalos can be added, with the the result being 3 additional buffalos in the output for the first additional buffalo in the input, followed by 2 additional buffalos in the output for each buffalo in the input after that.

So, naturally, the next step was Turing completeness.

To use:
```
./buffalotoprogrammachine.py buffalo
```

or 

```
echo "Buffalo buffalo buffalo buffalo Buffalo buffalo buffalo. Buffalo buffalo buffalo buffalo. Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo buffalo buffalo buffalo Buffalo buffalo. Buffalo buffalo buffalo buffalo buffalo buffalo buffalo buffalo. Buffalo buffalo buffalo buffalo Buffalo buffalo Buffalo buffalo buffalo buffalo. Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo buffalo." | ./buffalotoprogrammachine.py
```

There are two registers (buffalo and Buffalo). This is sufficient for Turing completeness, although I may add support for "fish" and "police" as additional registers in the future.

The first two sentences give the initial state of the registers. The first two words in the sentence are fixed as "Buffalo buffalo". Following this is the first variable word, which can be either "Buffalo" (1) or "buffalo" (0). The next word is fixed as "buffalo". This alternates with every other word representing one bit, interspersed with fixed "buffalo". The lowest value (1) bit comes first, followed by the 2 bit, then the 4 bit etc. This means that the sentence can end with any number of trailing "buffalo"s without affecting the binary value. This is used to ensure the sentence can be interpreted in English (if it does not parse, add more trailing buffalos until it does parse). TODO: Prove formally that if "buffalo" is placed at least every other word, there is always a number of trailing buffalos which can be added to the end of the sentence which will make it parse correctly in English.
For example: "Buffalo buffalo buffalo buffalo" represents 0. "Buffalo buffalo Buffalo buffalo" represents 1, but this is not a valid sentence, so instead we use "Buffalo buffalo Buffalo buffalo buffalo buffalo", which also evaluates to 1 but is a valid sentence. "Buffalo buffalo buffalo buffalo Buffalo buffalo" represents 2, but this also needs one extra "buffalo" on the end to parse as a valid sentence.

After the first two sentences (which set the initial register values) come the instructions. Again, the first two words of each instruction are fixed as "Buffalo buffalo".
If the third word is "Buffalo", the instruction is "JZ". In this case, the fifth word represents the register (buffalo or Buffalo) to check, and the 7th word onwards represent the line to jump to if the register is empty, in the same binary format as used to set the initial state of the registers. Any number of trailing buffalos can be added to ensure that this parses as a valid English sentence.
If the third word is "buffalo", we check the fifth word. If the fifth word is "Buffalo", the instruction is "INC", and the 7th word represents the register to increment (buffalo or Buffalo). If the fifth word is "buffalo", the instruction is "DEC", and the 7th word represents the register to decrement (buffalo or Buffalo). Again, any number of trailing buffalos can be added to force the sentence to be valid in English.

The interpreter will throw an error if any of the sentences in the input program fail to parse according to the grammar defined in buffaloparse.py . Note that this does not currently include "Buffalo buffalo" as a valid verb meaning "to buffalo in a manner specific to the city of Buffalo".

TODO: Add functionality for  🐃 to escape comments. The style guide will strongly encourage comments to be used only for incidental asides, and not for useful comments on the function of the program.


N.B. A much more polished version of this idea already exists at http://bfalo.com/. I am using a very different architecture based on register machines, and also attempt to ensure that each program parses as valid English.
