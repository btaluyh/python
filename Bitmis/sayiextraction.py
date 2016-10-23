
## dosya adi regex_sum_319125.txt

### line = " From: asdasd@hotmail.com sat 5 january 20:205:2016 999"
##    line2 = "My 2 favourite numbers are 19 and 42"
##    line = line.rstrip()
##    line = line.lstrip()
##    print (line, "  olay 1")
##
##    y = re.findall("^F.+?:", line)
##                   
##
##    m = re.findall("[0-9]+", line2)
##    print (y)

def sayi ():
    import re


    variable = input("Dosya Adi girin")

    f = open(variable)
    toplam = 0
    numbers = list()
    empty = []
    for line in f:
        m = re.findall("[0-9]+", line)

        if not m == []:
            numbers.append(m)


    for i in numbers:
        for m in i:
            m = int(m)
            toplam = toplam + m

    print (toplam)
