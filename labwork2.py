print("play my quiz")

score = 0

question_1 = input('''    
when was tesla founded
1)2007
2)2005
3)2003
4)2013 
write answer: '''
)

if question_1 == '3':
    score = score + 1 
    print(f"you earned {score}")
else:
    print("you are a failure")

    
question_2 = input('''    
what year was the internet created
1)1954
2)1965
3)1983
4)1998
write answer: '''
)

if question_2 == '3':
    score = score + 1 
    print(f"you earned {score}")
else:
    print("you are a failure")

question_3 = input('''    
when was the first andriod created
1)2005
2)2007
3)2013
4)2009
write answer: '''
)

if   question_3 == '2':
    score = score + 1 
    print(f"you earned {score}")
else:
    print("you are a failure")


question_4 = input('''    
what year was basketball invented
1)1921
2)1774
3)1873
4)1891
write answer: '''
)

if question_4 == '2':
    score = score + 1 
    print(f"you earned {score}")
else:
    print("you are a failure")

  
question_5 = input('''    
who is the president of the us 
1)barak obama
2)emmanuel marcon
3)joe biden
4)donald trump
write answer: '''
)

if question_5 == '3':
    score = score + 1 
    print(f"you earned {score}")
else:
    print("you are a failure")

