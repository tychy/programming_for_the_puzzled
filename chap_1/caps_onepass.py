cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 
'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 
'B', 'B', 'B', 'F', 'F', 'F', 'F']

cap3 = ['F', 'B', 'F']
cap4 = []
cap5 = ['F', 'F', 'B', 'H', 'B', 'B', 'F', 
'B', 'B', 'B', 'F', 'F', 'F', 'F']

 # F B F B
def pleaseConform(caps):
    if caps == []:
        print('caps is []')
        return
    caps = caps + [caps[0]]
    start = 0
    for i in range(1, len(caps)):
        if caps[i] == 'H':
            if caps[i - 1] != caps[0]:
                if start == i - 1:
                    print('flip your cap!')
                else:
                    print('through ', i - 1, ',please flip your caps')
            continue
        if caps[i] != caps[i - 1]:
            if caps[i] != caps[0]:
                print('People in positions',i,end=' ')
                start = i
            else:
                if start == i - 1:
                    print('flip your cap!')
                else:
                    print('through ', i - 1, ',please flip your caps')


pleaseConform(cap3)