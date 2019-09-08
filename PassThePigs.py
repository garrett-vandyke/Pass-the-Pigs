import random
from PIL import Image

def passThePigs():
    # keep rolling while true
    #game = True

    #while game:
        # get two numbers 1-100 inclusive
    pigList = [random.randint(1,100), random.randint(1,100)]
    resultList = []

    # populate results list
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
    
    # print results, prompt next move
    #print('\n' + resultList[0] + ' ' + resultList[1])
    # this image idea was not great
    #showImage(resultList[0], resultList[1])
    #userStopGo = input('Press enter to roll again, or type "q" to quit: ')

    # quit scenario
    #if userStopGo == 'q':
     #   game = False
      #  print('\nDrive safe! (a.k.a. get an Uber!)')
    return resultList
def showImage(pig1, pig2):
    # format filename
    pig1 = pig1.lower().replace(' ','')
    pig2 = pig2.lower().replace(' ','')

    pig1Pic = Image.open(pig1 + '.gif')
    pig2Pic = Image.open(pig2 + '.gif')

    pig1Pic.show()
    pig2Pic.show()

passThePigs()