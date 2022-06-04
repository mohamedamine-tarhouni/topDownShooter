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
CREATE TABLE IF NOT EXISTS ConfigurationP2
  (
        Player2Name    TEXT,
        Player2Lives    INT,
        Player2HP    INT,
        Player2Dmg    INT,
        Player2AtkSpeed    INT
  ); 
    '''
    )
cursor.execute('''
CREATE TABLE IF NOT EXISTS ConfigurationP1
  (
        Player1Name    TEXT,
        Player1Lives    INT,
        Player1HP    INT,
        Player1Dmg    INT,
        Player1AtkSpeed    INT
  ); 
    '''
    )

# # # send to database one query
# Game = ('midouch', 'amine',2365,259)
# # # cursor.execute('INSERT INTO score VALUES (?,?)', Best_User)
# cursor.execute('INSERT INTO ScoreBoard VALUES (?,?,?,?)', Game)

# connection.commit()
# # cursor.execute("DELETE FROM ScoreBoard")
# # connection.commit()
# # # print the first
# cursor.execute("SELECT * FROM ConfigurationP1")
# # # record = cursor.fetchone()
# # # print all
# record = cursor.fetchall()
# # # print a specific number of entry
# # # record = cursor.fetchmany(2)

# # # loop to print line by line
# # # for records in record:
# print(record)

# print(record)

# connection.close()
def insertValue(player,pos):
    connection = sqlite3.connect('score.db')
    cursor = connection.cursor()

    playerData=(player.name,player.lives,player.maxHP,player.Dmg,player.atkSpeed)
    if pos==1:
      cursor.execute("DELETE FROM ConfigurationP1")
      connection.commit()
      cursor.execute('INSERT INTO ConfigurationP1 VALUES (?,?,?,?,?)', playerData)
      connection.commit()
    else:
      cursor.execute("DELETE FROM ConfigurationP2")
      connection.commit()
      cursor.execute('INSERT INTO ConfigurationP2 VALUES (?,?,?,?,?)', playerData)
      connection.commit()
def insertMatchData(player1,player2):
    connection = sqlite3.connect('score.db')
    cursor = connection.cursor()
    Game = (player1.name, player2.name,player1.score,player2.score)
    # # cursor.execute('INSERT INTO score VALUES (?,?)', Best_User)
    cursor.execute('INSERT INTO ScoreBoard VALUES (?,?,?,?)', Game)

    connection.commit()
# def insertValue(column,value):
#     connection = sqlite3.connect('score.db')
#     cursor = connection.cursor()
#     cursor.execute('INSERT INTO ConfigurationP1(?) VALUES (?)', column,value)
#     connection.commit()
def getScores():
    connection = sqlite3.connect('score.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ScoreBoard")
    record = cursor.fetchall()
    connection.close()
    return record
def getPlayerData(pos):
    connection = sqlite3.connect('score.db')
    cursor = connection.cursor()
    if pos==1:
      cursor.execute("SELECT * FROM ConfigurationP1")
    else:
      cursor.execute("SELECT * FROM ConfigurationP2")
    record = cursor.fetchall()
    connection.close()
    return record
