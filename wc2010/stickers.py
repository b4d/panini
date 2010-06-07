#!/usr/bin/python

import string

def fMissing():
    stetje = [0,0,0,0,0,0] #missing, glitter, team, stadium, venue, in action
    missing = file('wc2010.txt', 'r').readlines()
    all_stickers = file('wc2010full.txt', 'r').readlines()
    for i in missing:
        stetje[0] += 1
        for j in all_stickers:
            j_splitted = string.split(j)
            if string.rstrip(i) == j_splitted[0]:
                for delcek in j_splitted:
                    if delcek == "Emblem":
                        stetje[1] += 1
                        break
                    elif delcek == "Team":
                        stetje[2] += 1
                        break
                    elif delcek == "STADIUM":
                        stetje[3] += 1

    print "+-----------+---------+-------+---------+"
    print "| Mankajoce | Emblemi | Ekipe | Igrisca |"
    print "+-----------+---------+-------+---------+"
    print "| %9d | %7d | %5d | %7d |" % \
          (stetje[0], stetje[1], stetje[2], stetje[3])
    print "+-----------+---------+-------+---------+"


def fPrint():
    missing = file('wc2010.txt', 'r').readlines()
    f = file('print.txt', 'w')
    for i in missing:
        j = string.rstrip(i)
        f.write(j)
        c = ", "
        f.write(c)
    f.close()


fMissing()

#fPrint()
