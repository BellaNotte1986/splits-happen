def ScoreCalc(seq):
    """Determines values and calculates score"""
    score = 0
    seq = list(''.join(seq.split()))
    for i in range(len(seq)):
        if seq[i] == 'X':
            seq[i] = 10
        elif seq[i] == '-':
            seq[i] = 0
        elif seq[i] == '/':
            continue
        else:
            seq[i] = int(seq[i])

    for j in range(len(seq)):
        roll = seq[j]
        if len(seq) - 3 <= j:
            if roll == '/':
                score += (10 - seq[j-1])
            else:
                score += roll
            continue
        elif roll == 10:
            score += roll
            score += seq[j+1]
            if seq[j+2] == '/':
                score += (10 - seq[j+1])
            else:
                score += seq[j+2]
        elif roll == '/':
            score += (10 - seq[j-1])
            score += seq[j+1]
        else:
            score += roll

    return score

def StartScoring(seq):
    while seq != 'q':
        print(f"Your score is {ScoreCalc(seq)}")
        seq = input("Enter your bowling score ( q to quit ): ")
    print("quiting program.")

if __name__ == '__main__':
    seq = input("Enter your bowling score ( q to quit ): ")
    StartScoring(seq)
