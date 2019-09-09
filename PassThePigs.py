import random

def passThePigs():
    # two random numbers 1-100 inclusive
    pigList = [random.randint(1,100), random.randint(1,100)]
    resultList = []

    # populate results list
    for i in pigList:
        if 1 <= i <= 65:                            # 65% chance of sider
            resultList.append('Sider')
        elif 65 < i <= 85:                          # 20% chance of razorback
            resultList.append('Razorback')
        elif 85 < i <= 95:                          # 10% chance of trotter
            resultList.append('Trotter')
        elif 95 < i <= 99:                          # 4% chance of snouter
            resultList.append('Snouter')
        elif i == 100:                              # 1% chance of leaning jowler
            resultList.append('Leaning Jowler')
    
    return resultList