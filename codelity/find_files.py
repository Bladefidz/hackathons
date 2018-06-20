# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import unittest
import sys

def solution(S):
    '''
    Specification:
        col         : "date perm name"
            date -> "last modification":
                format  : "dd MMM yyyy"
                    -> dd   : combination('0123456789', 2)
                    -> MMM  : pick_one('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
                    -> yyyy : combination('0123456789', 4)
                length  : 11
            perm -> "permissions":
                format  : combination('rwx-', 3)
                length  : 3
            name -> "name of file":
                format  : random(ASCII, 255)
                length  : 255

        new line    : ASCII(10)
    Statement:
        - Find read-only files (perm <- 'r--' or perm <- 'r-x').
        - Filter only date > '19 Jul 2004'
    Query:
        SELECT * FROM collection WHERE perm in ('r--', 'r-x') AND date >= DATE('19-07-2004')
    Note:
        "Bah, it is easy when came to SQL!"
    Correctness:
        - If QUERY not satisfied, then return "NO FILES"

    @param S: str
    @return : int or "NO FILES"
    '''
    N = len(S)

    # Sanity check
    if N == 0:
        return "NO FILES"

    # Preprocessing Step 1
    files = S.split('\n')

    # Sanity check
    # print(files)
    # print("Print first 10 items in files")
    # i = 0
    # for f in files:
    #     print(f)
    #     if i > 10:
    #         break
    #     i += 1

    # Preprocessing Step 2
    fileObjects = []
    for file in files:
        fileObjects.append(File(file))

    # Sanity check
    # print("Print first 10 items in fileObjects")
    # i = 0
    # for f in fileObjects:
    #     print(f)
    #     if i > 10:
    #         break
    #     i += 1

    # Filter match by given query
    matchedFiles = []
    for f in fileObjects:
        if f.isReadOnly() and f.newerThan('18 Jul 2004'):
            matchedFiles.append(f)

    # Sanity check
    # for f in matchedFiles:
    #     print(f)

    # Find lowest file name in matched files
    minNameLength = sys.maxsize
    for f in matchedFiles:
        if len(f.name) < minNameLength:
            minNameLength = len(f.name)

    if minNameLength == sys.maxsize:
        return "NO FILES"

    return str(minNameLength)


####################
# Helper Functions #
####################

DATES = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def monthToInt(m):
    '''
    @param m: str
    @return: int
    '''
    # print(m)
    return DATES.index(m) + 1

def dateToInt(date):
    '''
    @param date: str
    @return: int
    '''
    # print(date)
    dateInt = 0
    i = 1
    for val in date:
        val = val.strip()
        if i == 2:
            dateInt += monthToInt(val.lower())**i
        else:
            dateInt += int(val)**i
        i += 1
    return dateInt



##################
# Helper classes #
##################

class DateInt(object):
    """Integer formated Date"""
    def __init__(self, dateArr):
        self.val = dateToInt(dateArr)

    def compareTo(self, other):
        '''
        @param other: DateInt
        @return     : -1, 0, 1
        '''
        if self.val > other.val:
            return 1
        if self.val < other.val:
            return -1
        return 0

    def value(self):
        return self.val

class File(object):
    """Representation of File"""
    def __init__(self, fileStr):
        self.fileStrSplitted = fileStr.split(' ') 
        self.date = " ".join(self.fileStrSplitted[:3])
        self.dateInt = DateInt(self.fileStrSplitted[:3])
        self.perm = self.fileStrSplitted[3].strip()
        self.name = self.fileStrSplitted[4].strip()

    def compareTo(self, other, options):
        if 'name' in options.keys():
            if self.name != other.name:
                return -1
        if 'perm' in options.keys():
            if self.perm != other.perm:
                return -1
        if 'date' in options.keys():
            if self.dateInt > other.dateInt:
                return 1
            if self.dateInt < other.dateInt:
                return -1
        return 0

    def isReadOnly(self):
        if 'w' in self.perm or 'r' not in self.perm:
            return False
        return True

    def newerThan(self, dateStr):
        dateInt = DateInt(dateStr.strip().split(' '))
        if self.dateInt.value() < dateInt.value():
            return False
        return True

    def __str__(self):
        '''
        @return string
        '''
        info = {
            'date': self.date,
            'date_int': self.dateInt.val,
            'permission': self.perm,
            'name': self.name
        }
        return str(info)