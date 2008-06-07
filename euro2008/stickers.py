#!/usr/bin/python
# Filename: stickers_wc06.py
#| wc2006 stickers helper, list generator, ftp uploads, ...

import string, ftplib, sha
from getpass import getpass

#variables FTP (address, username, (hashed) pass, working dir)
synclogin = ('86.61.67.170', 'b4d', 'f8ef1f4ba1751b5d8dccb87bcc633bffff77e820', 'public_html/code/python/wc2006/')

##creating hash pwds
#import sha
#sha.new('sifra').hexdigest()

def fMissing():
    stetje = [0,0,0,0,0,0] #missing, glitter, team, stadium, venue, in action
    missing = file('euro2008.txt', 'r').readlines()
    all_stickers = file('euro2008full.txt', 'r').readlines()
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


def fHaving():
    count_posamezna = 0
    count_vseh = 0
    having = file('duple.txt', 'r').readlines()
    all_stickers = file('euro2008full.txt', 'r').readlines()
    for i in having:
        c = string.split(i, '|') # c = i.split('|')
        count_vseh = count_vseh + int(c[1])
    print "Imas",count_vseh,"odvecnih slicic."


def fPrint():
    missing = file('euro2008.txt', 'r').readlines()
    f = file('print.txt', 'w')
    for i in missing:
        j = string.rstrip(i)
        f.write(j)
        c = ", "
        f.write(c)
    f.close()


def fNet():
    missing = file('euro2008.txt', 'r').readlines()
    all_stickers = file('euro2008full.txt', 'r').readlines()
    f = file('net.txt', 'w')
    for i in missing:
        for j in all_stickers:
            j_splitted = string.split(j)
            if string.rstrip(i) == j_splitted[0]:
                f.write(j)
    f.close()


#sync upload on every exit
def fSyncUpload():
    ftp = ftplib.FTP(synclogin[0])
    ftp.login(synclogin[1], ftp_pass)
    ftp.cwd(synclogin[3]) #4
    localhave = open('net.txt','r')
    ftp.storlines('STOR net.txt',localhave)
    ftp.quit()
    localhave.close()



#synchronization download
def fSyncDownload():
    ftp = ftplib.FTP(synclogin[0])
    ftp.login(synclogin[1], ftp_pass)
    ftp.cwd(synclogin[3]) #4
    localhave = open('net.txt','w')
    ftp.retrlines("RETR net.txt", lambda s, w=localhave.write: w(s+"\n"))
    ftp.quit()
    localhave.close()



#ftp_pass = getpass("Prosim vnesite geslo: ")
#sys.stderr.write("")
#fNet()
fMissing()
#fHaving()
#fSyncDownload()
#fSyncUpload()

#fPrint()
