def hexDecode(hexi):
    output = 0
    multiplication = 1
    a = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,'F': 15, 'G': 16, 'H':17, 'I':18}
    for i in hexi[::-1]:
        if type(i) is str: i=i.upper()
        output += (a[i] * multiplication)
        multiplication *= 18
    return int(output)
def hexEncode(integer):
    output = ''
    a = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14:'E', 15:'F',16:'G' ,17:'H', 18:'I'}
    base=18
    multiplication=1
    cycles = 0
    while cycles == 0 or multiplication >= 1:
        if base*multiplication >= integer:
            output = output + (str(a[integer // (multiplication)]))
            integer -= (multiplication * (integer // multiplication))
            multiplication /= base
        if base*multiplication <integer:
            multiplication*=base
        #print(str(multiplication) + ' / ' + str(integer) + ' / ' + str(output))
        cycles+=1
    return str(output)

count=1
found=0
while True:
    squared = hexEncode(count*count)
    if len(squared)%2==0:
        initial = squared[:(len(squared)//2)]
        final = squared[(len(squared)//2):]
        if initial == final:
            if hexDecode(squared) == count*count:
                found+=1
                print(str(count) + ' squared is ' + str(count ** 2) + '(' + squared + ') / ('+str(found)+')')
    count+=1
