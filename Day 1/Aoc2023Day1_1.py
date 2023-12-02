def day_01(filename):
    c = 0
    print('Openen van file: ' + filename)

    with open(filename) as f:
        totaal = 0
        for line in f:
            c = c + 1
            nummers = ""
            for d in line:
                if d.isdigit():
                    nummers = nummers + str(d)
            getallen_per_regel = nummers[0:1] + nummers[-1:]
            totaal = totaal + int(getallen_per_regel)
        print('Totaal: ' + str(totaal))

day_01('input.txt')
