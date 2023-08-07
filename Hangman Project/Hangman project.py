import random

stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
words_list=list(open("/Users/Pranjal/Downloads/words.txt"))
lives=6
chosen_word=random.choice(words_list)
display=[]
for i in range(len(chosen_word)-1):
    display+='_'
print(chosen_word)
print(display)



game_over=False
while not game_over:
 guessed_letter=input("Guess a letter:")
 for position in range(len(chosen_word)-1):
  if chosen_word[position]==guessed_letter:
      display[position]=guessed_letter     
 print(display) 
 if guessed_letter not in chosen_word:
      print("Wrong choice!")
      lives-=1
      if lives==0:
          game_over=True
          print("You lose")
 if '_' not in display:
    game_over=True
    print("You win")
 print(stages[lives])