# Circuit-Simulator [Py]
## Digital Circuit Simulator
  - This program takes circuit structure file, user's desired primary input values;
  And simulates the circuit with the given inputs.
  When simulation completes, the program will print values at the primary output nodes.

## Circuit Structure File (.txt)
- Must be in the same format as s27.txt, s298f_2.txt, s344f_2txt, s349f_2.txt provided
- Each line is composed in following structure
  - If Gate is OR || NOR || AND || NAND
      [Gate Type] [Input 1 Node][Input 2 Node] [Output Node]
  - If Gate is INV || BUF
      [Gate Type] [Input 1 Node] [Output Node]
  - For the line starting with "INPUT"
      Lists Primary Input nodes where the values can be controlled by user's input
  - For the line starting with "OUTPUT"
      Lists Primary Output nodes
      
      
[Imgur](https://imgur.com/gx0wVtU)
