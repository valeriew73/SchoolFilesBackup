#1 a)
NamesArr = [None for i in range(11)]
ScoresArr = [0 for i in range(11)]
# NamesArr = ["FYI", "GUO", "JHP", "TJW", "YKE", "RUL", "PQM", "STR", "ANP", "BCX"]
# ScoresArr = [10000, 9600, 8700, 7300, 5600, 5500, 4800, 4300, 3900, 3700]

#1 b)
def ReadHighScores():
    FileHandle = open("HighScore.txt", 'r')
    for index in range(10):
        TextFromFile = FileHandle.readline().strip()
        NamesArr[index] = TextFromFile[0:3]
        ScoresArr[index] = int(TextFromFile[3:])
    FileHandle.close

#1 c)
def OutputHighScores():
    for index in range(len(NamesArr)):
        print(NamesArr[index], ScoresArr[index])

#1 d)
ReadHighScores()
OutputHighScores()

#1 e) i)
NewPlayerName = input("Please enter a 3 character player name: ")
while len(NewPlayerName) != 3:
    NewPlayerName = input("Player name has to be 3 characters only. Please re-enter: ")
    
NewPlayerScore = int(input("Please enter their new score: "))
while NewPlayerScore < 1 and NewPlayerScore > 100000:
    NewPlayerScore = input("Player Score must be between 1 and 100000 inclusive. Please re-enter: ")





# if appropriate, inserts the new player (name and score) into the top ten
# index = 0
# insert = False
# while not insert and index < len(NewFileArr):
#     compScore = int(NewFileArr[index][3:])
#     if NewPlayerScore >= compScore:
#         insert = True
#     index += 1

# if insert == True:
#     temp = NewFileArr[index-1]
#     index - 1

# Exception = an extreme condition that makes you program crash 
# can lead to loss of data in files