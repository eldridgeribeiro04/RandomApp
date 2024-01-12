from game_questions import Game_Questions

QA = ['What color is a tree? \n Green,\n Blue,\n Brown\n\n',
      'What is a python? \n Coding Language \n Snake \n Animal\n\n',
      'Which animal is the deadliest \n Bear, \nLion, \nTiger\n\n']

answer = [
    Game_Questions(QA[0], 'Green'),
    Game_Questions(QA[1], 'Snake'),
    Game_Questions(QA[2], 'Bear')
]

def test(answer):
    print("Welcome to the quiz game. Hope you enjoy!")
    playing = input("Do you want to play?: ").lower()
    if playing == 'yes':
        score = 0

        for q in answer:
            answers = input(q.question).lower()
            if answers == q.answer.lower():
                score += 1

        print("You scored" + " " + str(score) + " " + 'out of' + " " + str(len(answer)))
        print("Your test percent is: " + str(score/len(answer)*100))
    else:
        quit()


test(answer)
