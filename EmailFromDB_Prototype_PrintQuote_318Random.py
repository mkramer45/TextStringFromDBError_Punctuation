import smtplib
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')

conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur2 = cursor.execute('SELECT msg FROM Motivational ORDER BY RANDOM() LIMIT 1;')
info2 = cur2.fetchall()

y = [x[0].encode("utf-8") for x in info2]

print str(y)[1:-1]


# example of error:
# ' The reason most people never reach their goals is that they don\xe2\x80\x99t define them ...'
# where '\xe2\x80\x99' is returned instead of the apostrophe in 'don't'