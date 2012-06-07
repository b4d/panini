#!/usr/bin/python

import string
def fMissing():
    stetje = [0,0,0,0,0,0] #missing, glitter, team, stadium, venue, in action
    missing = file('euro2012.txt', 'r').readlines()
    all_stickers = file('euro2012full.txt', 'r').readlines()
    for i in missing:
        stetje[0] += 1
        for j in all_stickers:
            j_splitted = string.split(j)
            if string.rstrip(i) == j_splitted[0]:
                for delcek in j_splitted:
                    if delcek == "Glitter":
                        stetje[1] += 1
                        break
                    elif delcek == "Team":
                        stetje[2] += 1
                        break
                    elif delcek == "Stadium":
                        stetje[3] += 1
                        break
                    elif delcek == "Venues":
                        stetje[4] += 1
                        break
                    elif delcek == "action":
                        stetje[5] += 1

    print "+-----------+---------+-------+---------+-------+----------+"
    print "| Mankajoce | Glitter | Ekipe | Igrisca | Mesta | V akciji |"
    print "+-----------+---------+-------+---------+-------+----------+"
    print "| %9d | %7d | %5d | %7d | %5d | %8d |" % \
          (stetje[0], stetje[1], stetje[2], stetje[3], stetje[4], stetje[5])
    print "+-----------+---------+-------+---------+-------+----------+"


def fPrint():
    missing = file('euro2012.txt', 'r').readlines()
    f = file('print.txt', 'w')
    for i in missing:
        j = string.rstrip(i)
        f.write(j)
        c = ", "
        f.write(c)
    f.close()


fMissing()

fPrint()
