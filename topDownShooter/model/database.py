import sqlite3
connection = sqlite3.connect('score.db')

cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS ScoreBoard
  (
        Player1Name    TEXT,
        Player2Name    TEXT,
        Player1Score    INT,
        Player2Score    INT
  ); 
    '''
    )
cursor.execute('''
CREATE TABLE IF NOT EXISTS ConfigurationP1
  (
        Player1Name    TEXT,
        Player1Lives    TEXT,
        Player1HP    INT,
        Player1Dmg    INT,
        Player1AtkSpeed    INT
  ); 
    '''
    )

# # send to database one query
Game = ('midouch', 'amine',2365,259)
# # cursor.execute('INSERT INTO score VALUES (?,?)', Best_User)
cursor.execute('INSERT INTO ScoreBoard VALUES (?,?,?,?)', Game)

connection.commit()
# # print the first
# cursor.execute("SELECT * FROM ScoreBoard")
# # record = cursor.fetchone()
# # print all
# record = cursor.fetchall()
# # print a specific number of entry
# # record = cursor.fetchmany(2)

# # loop to print line by line
# # for records in record:
#     # print(record)

# print(record)

# connection.close()
def getScores():
    connection = sqlite3.connect('score.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ScoreBoard")
    record = cursor.fetchall()
    connection.close()
    return record
