def hexDecode(base, hexidecimal):
    if base > 35: return 'BASE CANNOT BE LARGER THAN 35'
    output = 0
    multiplication = 1
    a = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,'F': 15, 'G': 16, 'H':17, 'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
    for i in hexidecimal[::-1]:
        if type(i) is str: i=i.upper()
        output += (a[i] * multiplication)
        multiplication = base
    return int(output)
def hexEncode(base, integer):
    if base > 35: return 'BASE CANNOT BE LARGER THAN 35'
    output = ''
    a = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14:'E', 15:'F',16:'G' ,17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}
    multiplication=1
    cycles = 0
    while cycles == 0 or multiplication >= 1:
        if basemultiplication >= integer:
            output = output + (str(a[integer // (multiplication)]))
            integer -= (multiplication * (integer // multiplication))
            multiplication /= base
        if basemultiplication <integer:
            multiplication=base
        #print(str(multiplication) + ' / ' + str(integer) + ' / ' + str(output))
        cycles+=1
    return str(output)









