import random

def roll():
    pigList = [random.randint(1,100), random.randint(1,100)]
    resultList = []

    for i in pigList:
        if 1 <= i <= 65:
            resultList.append('Sider')
        elif 65 < i <= 85:
            resultList.append('Razorback')
        elif 85 < i <= 95:
            resultList.append('Trotter')
        elif 95 < i <= 99:
            resultList.append('Snouter')
        elif i == 100:
            resultList.append('Leaning Jowler')
    
    print(resultList[0] + ' ' + resultList[1])

roll()