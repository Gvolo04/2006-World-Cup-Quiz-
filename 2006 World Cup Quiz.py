name = input("Please eneter your name?")


print("Hello " + name+ " thanks for taking my quiz"+ "!")


quiz = {
    "First Question":{
        "question":"Who won the 2006 World Cup?",
        "answer":"Italy"

        },
    "Second Question":{
        "question":"Who was the top goal scorer of the 2006 World Cup?",
        "answer":"Miroslav Klose"
        },

    "Third Question":{
        "question":"Who won the Golden Glove at the 2006 World Cup?",
        "answer":"Gianluigi Buffon"
        },

    "Fourth Question":{
        "question":"Where was the 2006 world cup held?",
        "answer":"Germany"
        },

    "Fifth Question":{
        "question":"Who was teh runnner-up at the 2006 World Cup?",
        "answer":"France"
        },

    
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer?")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Score:" + str(score))

    else:
        print("Wrong")
        print("The answer is:" + value['answer'])
        print("Your score is:" + str(score))

print("You got " + str(score) + " out of 5 questions correct")
print("Thanks for taking my quiz " + name + " you got a " + str(score/5 * 100) + "%")
