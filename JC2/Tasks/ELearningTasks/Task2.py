#1 a)
NamesArr = [None for i in range(11)]
ScoresArr = [0 for i in range(11)]
# NamesArr = ["FYI", "GUO", "JHP", "TJW", "YKE", "RUL", "PQM", "STR", "ANP", "BCX"]
# ScoresArr = [10000, 9600, 8700, 7300, 5600, 5500, 4800, 4300, 3900, 3700]

#1 b)
def ReadHighScores():
    try: 
        FileHandle = open("C:/Users/Valerie JC2T/Desktop/Valerie Wilson JC1T/JC2/Tasks/ELearningTasks/HighScore.txt", 'r') # Copy the path from file explorer and then replace all the \ with /
        for index in range(10):
            TextFromFile = FileHandle.readline().strip()
            NamesArr[index] = TextFromFile[:3]
            ScoresArr[index] = int(TextFromFile[3:])
        FileHandle.close
    except FileNotFoundError:
        print("Sorry, the file you are looking for does not exist.")

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
while NewPlayerScore < 1 or NewPlayerScore > 100000:
    NewPlayerScore = input("Player Score must be between 1 and 100000 inclusive. Please re-enter: ")

for index in range(1, len(ScoresArr)):
    key = ScoresArr[index]
    j = index - 1
    while j >= 0 and key < ScoresArr[j]:
        temp = ScoresArr[j]
        ScoresArr[j] = ScoresArr[j + 1]
        ScoresArr[j + 1] = temp
        temp = NamesArr[j]
        NamesArr[j] = NamesArr[j + 1]
        NamesArr[j + 1] = temp
        j = j - 1

# FileHandle = open("C:/Users/Valerie JC2T/Desktop/Valerie Wilson JC1T/JC2/Tasks/ELearningTasks/HighScore.txt", 'a') # Copy the path from file explorer and then replace all the \ with /
# for index in range(10):
#     FileHandle.write(f"{NamesArr[index]} {ScoresArr[index]}\n") 
# FileHandle.close

# OutputHighScores()

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
