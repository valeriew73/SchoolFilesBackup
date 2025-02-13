StudentNames = [" " for i in range(10)]
Test1Scores = [0 for i in range(10)]
Test2Scores = [0 for i in range(10)]
TestAvg = [0.0 for i in range(10)]

print(StudentNames)

for i in range(10):
    TestAvg[i] = (Test1Scores[i] + Test2Scores[i]) / 2
