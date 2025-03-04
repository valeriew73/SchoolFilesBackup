
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

# ii)
def NewListProc(NewPlayerName, NewPlayerScore):  
    index = 0
    Insert = False
    while index < 10 and Insert == False:
        if NewPlayerScore >= ScoresArr[index]:
            Insert = True
        index += 1
    index -= 1
    
    if Insert == True:
        i = 0
        NewNamesList = []
        NewScoresList = [] 
        for i in range(10):
            if i < index:
                NewScoresList.append(ScoresArr[i])
                NewNamesList.append(NamesArr[i])
            if i == index:
                NewScoresList.append(NewPlayerScore)
                NewNamesList.append(NewPlayerName)
            elif i > index:
                NewScoresList.append(ScoresArr[i-1])
                NewNamesList.append(NamesArr[i-1])
        NamesArr = NewNamesList
        ScoresArr = NewScoresList

# iii)   
OutputHighScores()   
NewListProc(NewPlayerName, NewPlayerScore)
for i in range(10):
    print(NewNamesList[i], NewScoresList[i])



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
