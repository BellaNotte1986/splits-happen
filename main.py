"""
ref: http://www.fryes4fun.com/Bowling/scoring.htm
ref: https://www.rookieroad.com/bowling/scoring-rules/
"""

# store the basic score of the single mark
dic = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'X':10,'-':0}


def calTotal(s):
    '''
    Calculate the total score of a complete bowling game based on result of a string
    :param: s
    :type: str
    :rtype: int
    '''
    score = 0
    # count the frame of the scores, two half equal to one frame
    # X mark take a whole frame, while others take a half
    frame, half = 0, 0
    # main loop
    for i in range(len(s)):
        # exit when the frame is filled
        if frame == 10:
            break
        # '-' equals to 0, no need to add
        if s[i] == '-':
            half += 1
        # other marks
        else:
            if s[i].upper() == 'X':
                score += 10 + calXScore(s[i+1],s[i+2])
                frame += 1
            elif s[i] in dic:
                score += dic[s[i]]
                half += 1
            elif s[i] == '/':
                score += 10 - dic[s[i-1]] + dic[s[i+1]]
                half += 1
        # count frames
        if half == 2:
            half = 0
            frame += 1

    return score


def calXScore(next1,next2):
    '''
    Calculate score related to a single X mark
    :param: next1, next2
    :type: str, str
    :rtype: int
    '''
    temp = 0
    temp += dic[next1]
    if next2 == '/':
        temp += 10 - dic[next1]
    else:
        temp += dic[next2]
    return temp


# main body of the program 
def calScore():
    '''
    Get input string represeting scores from users, and calculate scores
    '''
    strScore = input("Enter a result of game ('q' to exit): ")
    while strScore != 'q':
        ans = calTotal(strScore)
        print(ans)
        strScore = input("Enter a result of game ('q' to exit): ")
    print("end")

# calScore()
if __name__ == '__main__':
    calScore()


