#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import mysql.connector
from mysql.connector import Error


def printString(r):
    length = len(r)
    strToPrint = ""
    for char in range(length):
        strToPrint += "="

    print strToPrint

try:
    connection = mysql.connector.connect(host='jinado.se', database='gymnasiearbete', user='garaspscreen', password='IatRPs.Iwdatm!')

    sql_query = "SELECT string FROM raspberries WHERE email LIKE 'johannes.emmoth@gmail.com' AND name LIKE 'Kontorsdörr 1'"
    cursor = connection.cursor()
    cursor.execute(sql_query)
    records = cursor.fetchall()

    # Check to see if a file exists, if it does, open it and read the first line
    # then compare the read value with the fetched value, if they're equal, do nothing
    # if they're not equal, write the fetched value into the file and then close it
    # print the fetched value

    try:
        readVal = ""
        with codecs.open('./screenData.txt', 'r', 'utf-8-sig') as f:
            readVal = f.readlines()
        if(readVal[0] != "" and readVal[0] != records[0][0]):
            # NOT THE SAME
            with codecs.open('./screenData.txt', 'w', 'utf-8-sig') as f:
                f.write(records[0][0])

            printString(records[0][0])
            print records[0][0]
            printString(records[0][0])
    except IOError:
        with codecs.open('./screenData.txt', 'w', 'utf-8-sig') as f:
            f.write(records[0][0])
    
        printString(records[0][0])
        print records[0][0]
        printString(records[0][0])
 
    # If the file does not exist, create it and write the fetched value to it.
    # After that, print the fetched value

except Error as e:
    print "Error reading data from MySQL table", e
finally:
    if(connection.is_connected()):
        connection.close()
        cursor.close()
