score = 0
import time
quiz = input("Do you want a play a quiz on python? ")
if quiz =="No":
    print("Oh is that so? Alright, please come back at a later time.")
else:
    print("Oh! Good to see that you are up for the challenge. Okay, read the following instructions carefully and type 'Start' to begin the quiz!","1. This quiz is based on Python and you have 5 questions to answer.","2. Each correct answer will give you +2 points.","3. However, if you end up giving the wrong answer, you will be awarded -1 points.","4. You need to enter 1,2,3 or 4 depending on what you think is the right answer","5. If you don't know the answer and don't want to answer, type 0 to go to the next question",sep = "\n")
    quizstart = input("")
    if quizstart != "Start":
        print("Oh no, looks like you didn't type 'Start'. Please restart the program and try again.")
    else:
        question1= input("Which of the following is NOT a module in python? 1. math 2. random 3. statistics 4. All of the above are modules in python ")
        if question1 == "4":
            score = score + 2
        elif question1 =="0":
            score = score + 0
        else:
            score = score - 1
        question2= input("Which of the following is the element with index -3 in the list ['A','B','C','D']? 1. A 2. B 3. C 4. D ")
        if question2 == "2":
            score = score + 2
        elif question2 =="0":
            score = score + 0
        else:
            score = score - 1
        question3= input("Which of the following can be used to delete a element from a list? 1. pop() 2. del() 3. remove() 4. both 1 and 3 ")
        if question3 == "4":
            score = score + 2
        elif question3 =="0":
            score = score + 0
        else:
            score = score - 1
        question4 = input("Each pair of a data in a dictionary is 1. key-value pair 2. key-record pair 3. record-value pair 4. key-data pair ")
        if question4 == "1":
            score = score + 2
        elif question4 =="0":
            score = score + 0
        else:
            score = score - 1
        question5 = input("How many elements can lists store? 1. 10 2. 2325768996 3. 455476488 4. 536870912 ")
        if question5 == "4":
            score = score + 2
        elif question5 =="0":
            score = score + 0
        else:
            score = score - 1
        print("Well? Excited to know your score? You scored....")
        time.sleep(5)
        print(score)
        
    
        
            
        
          
