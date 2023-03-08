from datetime import datetime
import csv
import os

# define variables

filename = str(os.path.dirname(__file__)) + "\\benlogs.csv"
print(filename)
answer = []  # list of answers. Will be written to later.

def hexDecode(base, hexidecimal):
    if base > 35 or base <= 0: return 'BASE IS OUT OF RANGE'
    output = 0
    a = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
          'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
          'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35 }
    for i in hexidecimal:
        output = output * base + a[i]
    return output

def hexEncode(base, integer):
    if base > 35 or base <= 0: return 'BASE IS OUT OF RANGE'
    output = ''
    multiplication = 1
    while multiplication <= integer:
        multiplication *= base
    while multiplication > 1:
        multiplication /= base

        output += chr(ord('0') + int(integer // multiplication))
        integer %= multiplication
    return output

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
                        "Ans #" + str(found) + ": @ " + dt_string + ": " + str(i) + " - " + str(
                            i * i) + " - " + squared + " - " + str(finalEcho) + " - " + finalEchoHex)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Finished at", dt_string)


