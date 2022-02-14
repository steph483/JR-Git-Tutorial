def main():
    # Introduction
    
    print("Hello and welcome to your new MadLibs game.")
    print("You can choose to do a happy or sad MadLib.")
    userChoice = input("Which one do you want? ")
    

    #Getting user input    
    if userChoice in ['sad', 'happy']:
        print("Great selection!")
        user_animal = input("Choose an animal: ")
        user_verb = input("Choose a gerund: ")
        user_location = input("Choose a location: ")      
        
    else:
        print("Please try again")
        print("-")
        main()

    #Sending user input to correct category
    if userChoice == 'sad':
        sad(user_animal, user_location, user_verb)
    elif userChoice == 'happy':
        happy(user_animal, user_location, user_verb)

    # Later Addition:
    # play_again = input("Thanks for playing. Want to play again? (y/n) ")
    # if play_again == 'y':
    #     main()
    # else:
    #     print("bye")



def happy(user_animal, user_location, user_verb):
    print("There was one a {} that lived in {}.".format(user_animal, user_location))
    print("The {} always showed their happiness by {} because their owner always took them out to walk.".format(user_animal, user_verb))
    

def sad(user_animal, user_location, user_verb):
    print("There was one a {} that lived in {}.".format(user_animal, user_location))
    print("Since the {}'s owner never paid attention to them, they were always {} and to try to get their attention.".format(user_animal, user_verb))

if __name__ == "__main__":
    main()