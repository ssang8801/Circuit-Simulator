def Ready_Checker(elements):
    if elements[0] == "INV":
        if elements[4] != -1:
            if elements[2] == 0:
                Ready_Gates.append(elements[1])

    if elements[0] == "BUF":
        if elements[2] == 0:
            if elements[4] != -1:
                Ready_Gates.append(elements[1])

    if elements[0] == "OR":
        if elements[4] != -1:
            if elements[6] != -1:
                if elements[2] == 0:
                    Ready_Gates.append(elements[1])

    if elements[0] == "NOR":
        if elements[2] == 0:
            if elements[4] != -1:
                if elements[6] != -1:
                    Ready_Gates.append(elements[1])


    if elements[0] == "AND":
        if elements[2] == 0:
            if elements[4] != -1:
                if elements[6] != -1:
                    Ready_Gates.append(elements[1])

    if elements[0] == "NAND":
        if elements[2] == 0:
            if elements[4] != -1:
                if elements[6] != -1:
                    Ready_Gates.append(elements[1])


print("Digital Circuit-Simulator".center(40, '-'))

filename = input("Please enter the name of the file you would like to simulate:")

circuitfile = open(filename)

#format - list within list
#list 1 = Gate = [Gate Type, Input 1 Node, Input 1 Value, Input 2 Node, Input 2 Value, Ouptput Node, Output Value]
#list 2 = Gates = contain list of Gate above
#list 3 = Inputs = [Primary Input Node, Primary Input Values]
#list 4 = Outputs = [Primary Output Node, Primary Output Values]

Gates = list()
Inputs = list()
Outputs = list()
Input_length = 0
Output_length = 0
GateNum = 0;
for line in circuitfile:
    if line.startswith("INPUT"):
        templist = line.split()
        input_length = len(templist)-2
        for elements in templist:
            if elements != 'INPUT':
                if elements != '-1':
                    Inputs.append([elements, '-1'])
        #print(Inputs)
    elif line.startswith("OUTPUT"):
        templist = line.split()
        for elements in templist:
            if elements != 'OUTPUT':
                if elements != '-1':
                    Outputs.append([elements, '-1'])
        #print(Outputs)
    elif line.startswith("INV"):
        templist = line.split()
        Gates.append(["INV", GateNum, 0, templist[1], -1, -1, -1, templist[2], -1])
        #print(Gates)
    elif line.startswith("BUF"):
        templist = line.split()
        Gates.append(["BUF", GateNum, 0, templist[1], -1, -1, -1, templist[2], -1])

    elif line.startswith("OR"):
        templist = line.split()
        Gates.append(["OR", GateNum, 0, templist[1], -1, templist[2], -1, templist[3], -1])

    elif line.startswith("NOR"):
        templist = line.split()
        Gates.append(["NOR", GateNum, 0, templist[1], -1, templist[2], -1, templist[3], -1])

    elif line.startswith("AND"):
        templist = line.split()
        Gates.append(["AND", GateNum, 0, templist[1], -1, templist[2], -1, templist[3], -1])

    elif line.startswith("NAND"):
        templist = line.split()
        Gates.append(["NAND", GateNum, 0, templist[1], -1, templist[2], -1, templist[3], -1])

    GateNum = GateNum + 1

binary_checker = 0
print("\nPlease enter the input vector you would like to test[", input_length, "binary digits ]:")
User_Input = input()

if len(User_Input) !=  len(Inputs):
    binary_checker = 1

for elements in User_Input:
    if elements != '0':
        if elements != '1':
            binary_checker = 1

while(binary_checker == 1):
    binary_checker = 0
    print("\nPlease enter correct input vector[", input_length, "binary digits ]:")
    User_Input = input()

    if len(User_Input) !=  len(Inputs):
        binary_checker = 1

    for elements in User_Input:
        if elements != '0':
            if elements != '1':
                binary_checker = 1


for i in range(len(User_Input)):
    Inputs[i][1] = int(User_Input[i])

#[Type, Num, Exe, In1Node, In1Val, In2Node, In2Val, OutNode, OutVal]
# 0      1    2      3       4       5         6       7       8
for elements in Gates:
    for elements2 in Inputs:
        if elements[3] == elements2[0]:
            elements[4] = elements2[1]
        if elements[5] == elements2[0]:
            elements[6] = elements2[1]

Ready_Gates = list()

for elements in Gates:
    Ready_Checker(elements)

while(Ready_Gates):
    for elements in Gates:
        for elements2 in Ready_Gates:
            if elements[1] == elements2:
                elements[2] = 1
                if elements[0] == 'INV':
                    if elements[4] == 1:
                        elements[8] = 0
                    if elements[4] == 0:
                        elements[8] = 1
                if elements[0] == 'BUF':
                    if elements[4] == 1:
                        elements[8] = 1
                    if elements[4] == 0:
                        elements[8] = 0
                if elements[0] == 'OR':
                    if (elements[4] | elements[6]) == 0:
                        elements[8] = 0
                    if (elements[4] | elements[6]) >= 1:
                        elements[8] = 1

                if elements[0] == 'NOR':
                    if (elements[4] | elements[6]) == 0:
                        elements[8] = 1
                    if (elements[4] | elements[6]) >= 1:
                        elements[8] = 0
                if elements[0] == 'AND':
                    if (elements[4] & elements[6]) == 0:
                        elements[8] = 0
                    if (elements[4] & elements[6]) == 1:
                        elements[8] = 1
                if elements[0] == 'NAND':
                    if (elements[4] & elements[6]) == 0:
                        elements[8] = 1
                    if (elements[4] & elements[6]) == 1:
                        elements[8] = 0
    #Gates2 = Gates
    for elements in Gates:
        if elements[8] != -1:
            for elements2 in Gates:
                if elements2[3] == elements[7]:
                    elements2[4] = elements[8]
                if elements2[5] == elements[7]:
                    elements2[6] = elements[8]
    #Gates = Gates2

    Ready_Gates.clear()
    for elements in Gates:
        Ready_Checker(elements)

print ("\n")
for elements in Outputs:
    for elements2 in Gates:
        if elements2[7] == elements[0]:
            print("Value at Primary Output Node", elements[0], "is ", elements2[8])
            elements[1] = elements2[8]

print("\nPrimary Output Nodes:")
for elements in Outputs:
    print(elements[0], end =" ")

print("\n\nValues at primary output nodes")
for elements in Outputs:
    print(elements[1], end = " ")

#print(Ready_Gates)
#print(Gates)
#print(Inputs)
#print(Outputs)
