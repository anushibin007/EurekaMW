
import mysql.connector
from com.eurekamw.utils import DBConstants as DC


def isPresentInDB(name):
    return False

def getConnection():
        return mysql.connector.connect(host=DC.HOSTNAME,
                                       user=DC.DB_USERNAME,
                                       passwd=DC.DB_PASSWORD,
                                       database=DC.DB_NAME)
