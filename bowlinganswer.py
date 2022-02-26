def decodeScore(score):
  """
   This function decodes the symbols and adds them to a continuous variable called sum that will
   be returned as the final value of the given string.
  """
  values = {"X": 10, "-": 0, "/": 10}        # Value of the symbols that can't be intified
  sum = 0                                    # running total score
  count = 0                                  # used to determine when we have extra rolls
  for i in range(len(score)):
    if score[i] == "X":                      # had to remember that an X is worth a whole frame or two rolls.
      count = count + 2
    else:
      count = count + 1

    if count > 19:                           # Given the way I calculated the count variable I know extra time is any roll past 19
      if score[i] in values.keys():          # had to know whether or not the next element is a symbol or an string that can be intified.
        if score[i] == "/":                  # had to remember a spare in a frame means the frame is worth ten had to subtract to calculate value of each roll and make sure I don't exceed a value of ten for the frame.
          sum = sum - int(score[i-1])
          sum = sum + 10
        else:
          sum = sum + values.get(score[i])
      else: 
        sum = sum + int(score[i])
    elif score[i] == "X":
      if score[i + 1] in values.keys():
        sum = sum + 10 + values.get(score[i + 1])
      else:
        sum = sum + 10 + int(score[i+1])
      if score[i+2] in values.keys():
        if score[i+2] == '/':                              # had to make sure I know the value of each roll in a frame with a spare to add it to the strike.
          if score[i+1] in values.keys():
            sum = sum + (10 - values.get(score[i+1]))
          else:
            sum = sum + (10 - int(score[i+1]))
        else:
          sum = sum + values.get(score[i+2])
      else:
        sum = sum + int(score[i+2])

    elif score[i] == "-":
      sum = sum + 0

    elif score[i] == "/":
      sum = sum - int(score[i-1])
      sum = sum + 10
      if score[i+1] in values.keys():
        sum = sum + values.get(score[i+1])
      else:
        sum = sum + int(score[i+1])

    else:
      sum = sum + int(score[i])

    
      

  
  return sum

def main():
  test1 = "XXXXXXXXXXXX"
  test2 = "9-9-9-9-9-9-9-9-9-9-"
  test3 = "5/5/5/5/5/5/5/5/5/5/5"
  test4 = "X7/9-X-88/-6XXX81"

  testone = decodeScore(test1)            # not sure how you are going to test the code wether it be in returns in a compiler or just print statements but
                                          # went a head and made every test example into a variable.
  testtwo = decodeScore(test2)
  testthree = decodeScore(test3)
  testfour = decodeScore(test4)

if __name__ == "__main__":
  main()
