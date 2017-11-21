#!/usr/bin/python

'''This module implements a complete English dictionary using trie data
structure and MySQL

'''
import MySQLdb

import Trie

# Create an empty Trie

trie = Trie.Trie()

db= MySQLdb.connect(host="127.0.0.1",db="entries",passwd="********")    #passwd  : your passwd for mysql server

cursor=db.cursor()

queryString="select * from  entries"

cursor.execute(queryString)

row=cursor.fetchone()

while row is not None:
    trie.insert(row[0],row[1],row[2])
    row=cursor.fetchone()

test=int(input("Enter the no of queries you want to do\n"))

while test>0:

    word=input("Enter the word\n")

    Res=trie.get_meaning(word)

    if len(Res)==0: # i.e if the tuple returned is an empty tuple
        print("Sorry ! The word doesn't exist")
    else:
        print(Res[1], "\n", Res[2])

    test=test-1


db.close()