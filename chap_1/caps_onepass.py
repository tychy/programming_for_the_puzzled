cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 
'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 
'B', 'B', 'B', 'F', 'F', 'F', 'F']


def pleaseConform(caps):
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] != caps[0]:
                print("People in positions" + str(i))
            else:
                print("through " + str(i - 1) + ",please flip your caps")


pleaseConform(cap2)