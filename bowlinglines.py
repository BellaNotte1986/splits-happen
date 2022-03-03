#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:44:25 2022

@author: emmadionne
EITR American 10-Pin Bowling
"""

def score(line):
    """
    calculates the score of each line of bowling

    Parameters
    ----------
    line : str
        String of each bowling roll with X for strike, / for spare, and - for miss.

    Returns
    -------
    score : int
        returns the total score of the function.

    """
    
    # create an array of each roll
    line_arr = list(line)
    score = 0;
    i = 0;
    frame_count = 1;
    # change the misses and strikes to integer values in the array
    for i in range(len(line_arr)):
        if line_arr[i] == '-':
            line_arr[i] = 0
        elif line_arr[i] == 'X':
            line_arr[i] = 10
    
    i = 0;
    
    #count each fram out - leave the last one out (special rules)
    while (frame_count < 10):
        # strike
        if(len(line_arr) > (i+2) and int(line_arr[i]) == 10):
            score += 10 + int(line_arr[i+1])
            # strike and the next roll is a spare
            if line_arr[i+2] == '/':
                score += 10 - int(line_arr[i+1])
                i = i+1;
                frame_count += 1;
            # strike and normal next roll
            else:
                score += int(line_arr[i+2])
                i = i + 1;
                frame_count += 1;
        # normal roll
        else:
            score += int(line_arr[i])
            # spare
            if (len(line_arr) > (i+2) and line_arr[i+1] == '/'):
                score += 10 - int(line_arr[i]) + int(line_arr[i+2])
                i += 1;
            # miss, doesn't count as an individual frame
            elif int(line_arr[i]) == 0:
                frame_count -= 1;
            i += 1;
            frame_count += 1;
                
        
    
    # now on the last frame:
    if(line_arr[i] == 10):
        score += 10 + int(line_arr[i+1]) + int(line_arr[i+2]);
    elif(len(line_arr) > i+1 and line_arr[i+1] == "/"):
        score += 10 + int(line_arr[i+2]);
    else:
        score += int(line_arr[i]) + int(line_arr[i+1]);
    
    return score

if __name__ == '__main__':
    # main program --> takes input from the user
    line = input("please enter your scores for the game: \n")
    print(line)
    print(score(line))