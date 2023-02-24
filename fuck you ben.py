from hexidecimal import hexEncode
from hexidecimal import hexDecode

count=1
found=0
base=1
while True:
    squared = hexEncode(base, count*count)
    if len(squared)%2==0:
        initial = squared[:(len(squared)//2)]
        final = squared[(len(squared)//2):]
        if initial == final:
            if hexDecode(base, squared) == count*count:
                found+=1
                print('Sol. found')
                print("C: " + str(count) + 'sqr: ' + str(count ** 2) + '(' + squared + ') / ('+str(found)+')' )
    if count == 5000000000:
        base+=1
    count+=1
