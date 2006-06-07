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
    counter_missing = 0
    counter_glitter = 0
    counter_team = 0
    counter_stadium = 0
    missing = file('wc2006.txt', 'r').readlines()
    all_stickers = file('wc2006full.txt', 'r').readlines()
    for i in missing:
        counter_missing = counter_missing + 1
        for j in all_stickers:
            j_splitted = string.split(j)
            if string.rstrip(i) == j_splitted[0]:
                for delcek in j_splitted:
                    if delcek == "Glitter":
                        counter_glitter = counter_glitter + 1
                    elif delcek == "Team":
                        counter_team = counter_team + 1
                    elif delcek == "Stadium":
                        counter_stadium = counter_stadium + 1 

    print "Manjka ti se:"
    print "   ",counter_missing
    print "Od tega ti manjka se:"
    print "   Sijoce slicice:",counter_glitter
    print "   Ekipne slicice:",counter_team
    print "   Slicice igrisc:",counter_stadium

def fHaving():
    count_posamezna = 0
    count_vseh = 0
    having = file('duple.txt', 'r').readlines()
    all_stickers = file('wc2006full.txt', 'r').readlines()
    for i in having:
        c = string.split(i, '|') # c = i.split('|')
        count_vseh = count_vseh + int(c[1])
    print "Imas",count_vseh,"odvecnih slicic."
        
def fPrint():
    missing = file('wc2006.txt', 'r').readlines()
    f = file('print.txt', 'w')
    for i in missing:
        j = string.rstrip(i)
        f.write(j)
        c = ", "
        f.write(c)
    f.close()

def fNet():
    missing = file('wc2006.txt', 'r').readlines()
    all_stickers = file('wc2006full.txt', 'r').readlines()
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



ftp_pass = getpass("Prosim vnesite geslo: ")
#sys.stderr.write("")
fNet()
fMissing()
#fHaving()
#fSyncDownload()
fSyncUpload()

fPrint()
