cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 
'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 
'B', 'B', 'B', 'F', 'F', 'F', 'F']

cap3 = ['F', 'B', 'F']
 # F B F B
def pleaseConform(caps):
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] != caps[0]:
                print('People in positions',i,end=' ')
            else:
                if caps[i - 1] != caps[i - 2]:
                    print('flip your cap!')
                else:
                    print('through ', i - 1, ',please flip your caps')


pleaseConform(cap3)