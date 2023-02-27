from datetime import datetime
import csv
import os

# define variables

filename = str(os.path.dirname(__file__)) + "\\benlogs.csv"
print(filename)
answer = []  # list of answers. Will be written to later.


# define functions

def hexDecode(base, hexidecimal):
    if base > 35 or base <= 0: return 'BASE IS OUT OF RANGE'
    output = 0
    multiplication = 1
    a = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
         'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
         'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    for i in hexidecimal[::-1]:
        if type(i) is str: i = i.upper()
        output += (a[i] * multiplication)
        multiplication *= base
    return int(output)


def hexEncode(base, integer):
    if base > 35 or base <= 0: return 'BASE IS OUT OF RANGE'
    output = ''
    a = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
         13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
         25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
    multiplication = 1
    cycles = 0
    while cycles == 0 or multiplication >= 1:
        if base * multiplication >= integer:
            output += (str(a[integer // (multiplication)]))
            integer -= (multiplication * (integer // multiplication))
            multiplication /= base
        if base * multiplication < integer:
            multiplication *= base
        # print(str(multiplication) + ' / ' + str(integer) + ' / ' + str(output))
        cycles += 1
    return str(output)


def csvWrite(list, filename):
    csv_str = ','.join([str(i) for i in list])
    with open(filename, 'a') as f:
        f.write('%s\n' % csv_str)


# Code starts here
f = open(filename, "w+")
f.close()


wap = ['Base', 'Number', 'Number SQ', 'Number SQ HEX', 'Number Echo', 'Number Echo HEX', 'Date/Time']
csvWrite(wap, filename)

found = 0
for base in range(2, 36):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Currently on base " + str(base) + " since " + dt_string)
    print("Found answers: ")
    for i in range(1000000000):
        squared = hexEncode(base, i * i)

        if len(squared) % 2 == 0:
            initial = squared[:(len(squared) // 2)]
            final = squared[(len(squared) // 2):]

            if initial == final:

                if hexDecode(base, squared) == i * i:
                    # If answer is found
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    # Not used for any calculations. Simply only to print out.
                    finalEcho = int(str(i) + str(i))
                    finalEchoHex = hexEncode(base, finalEcho)
                    answer = [base, i, i * i, squared, finalEcho, finalEchoHex, dt_string]
                    csvWrite(answer, filename)

                    # with open('fuckben-log.csv', 'wb') as csvfile:
                    #    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    #    filewriter.writerow([base, i, i * i, squared, finalEcho, finalEchoHex, dt_string])
                    # write to the csv file in this order: ['base', 'number', 'num sq', 'num sq in hex', 'num mir', 'num mir in hex', 'dt_string']

                    found += 1
                    print(
                        "Ans #" + str(found) + ": @ " + dt_string + ": " + str(i) + " - " + str(i * i) + " - " + squared + " - " + str(finalEcho) + " - " + finalEchoHex)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Finished at", dt_string)
