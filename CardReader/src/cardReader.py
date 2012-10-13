'''
Created on Oct 7, 2012

@author: Alex Zavala
'''
import MySQLdb
import sys

def checkIfExists(myUIN, myCursor):
    '''This function takes a UIN and checks if it already exists in the database.
    @param myUIN: a University Identification Number in integer format.
    @param myCursor: a cursor for the SHPE members database.
    '''
    
    myCursor.execute('SELECT UIN FROM members')
    
    for storedUIN in myCursor.fetchall():
        if storedUIN == myUIN:
            return True
    return False

def connectToDB():
    '''This functions connects to the SHPE shpeuiuc_members database.
    '''
    db=MySQLdb.connect(host='127.0.0.1',user='shpeuiuc_shpeuiuc_2012',passwd='xtTjlqno',db='shpeuiuc_shpeuiuc_members')
    myCursor = db.cursor()
    return myCursor

def updateGBMAttendance(UIN, myCursor):
    '''This function increases the members gbm attendance by 1.
    @param UIN: a University Identification Number in integer format.
    @param myCursor: a cursor for the SHPE members database.
    '''
    myCursor.execute('UPDATE members SET gbmsAttended=gbmsAttended+1 WHERE UIN=%d',UIN)
    
def firstAttendance(UIN, myCursor):
    '''This function increases the members gbm attendance by 1.
    @param UIN: a University Identification Number in integer format.
    @param myCursor: a cursor for the SHPE members database.
    '''
    myCursor.execute('INSERT INTO members (UIN,gbmAttended) VALUES (%d,%d)',UIN,1)

def main():
    while(True):
        cardString = raw_input("Please swipe your card.")
        if cardString == 'exit':
            break;
        try:
            UIN = int(cardString[5:-16])
        except ValueError:
            print 'Given UIN is not in the correct format'
        print UIN
        myCursor = connectToDB()
        if checkIfExists(UIN,myCursor):
            updateGBMAttendance(UIN,myCursor)
        else:
            firstAttendance(UIN,myCursor)
        print 'Card read successfully'
    
    
if __name__ == '__main__':
    sys.exit(main())