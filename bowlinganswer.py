def decodeScore(score):
  values = {"X": 10, "-": 0, "/": 10}
  sum = 0
  count = 0
  for i in range(len(score)):
    if score[i] == "X":
      count = count + 2
    else:
      count = count + 1

    if count > 19:
      if score[i] in values.keys():
        if score[i] == "/":
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
        if score[i+2] == '/':
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

  testone = decodeScore(test1)
  testtwo = decodeScore(test2)
  testthree = decodeScore(test3)
  testfour = decodeScore(test4)

if __name__ == "__main__":
  main()
