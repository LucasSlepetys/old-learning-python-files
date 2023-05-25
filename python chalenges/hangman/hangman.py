import random
import time
import sys
try:
    from words import hard_word_list, easy_word_list
except Exception:
    print("Error: Cannot import word_list from words.\n")
    print("It seems that you don't have the file 'words.py' in the same folder as 'hangman.py'..." +
          "\n" + "Please make sure both files can be found at the same folder!")
    print("\n")
    sys.exit(1)

try:
    import colorama
    from colorama import Fore, Back, Style
except Exception:
    print("Error: Cannot import colorama.\n")
    print("It seems that you don't have colorama installed in your computer..." +
          "\n" + "Please go to your terminal and type the following:")
    print("---> pip install colorama \n")
    sys.exit(1)


colorama.init(autoreset=True)


def get_words():
    print(Fore.RED + "-----------------------------------------------------------")
    print(Style.BRIGHT + "Let's play hangman!" + "\n" +
          "You have 6 tries to guess the word! Every turn you can guess a letter!")
    start = input(Style.DIM + Fore.BLUE + "Let's start? (Y/N)")
    start = start.upper()
    print("\n")

    if start != "Y":
        time.sleep(1)
        start = input(Style.DIM + Fore.BLUE + "Try again! Let's start? (Y/N)")
        start = start.upper()

    play = "true"
    if start == "N":
        print(Style.BRIGHT + Fore.BLUE + "That's okay... Let's play later!")
        sys.exit(1)

    if play == "true":
        print(Fore.BLUE + Style.BRIGHT + "Choose your level of difficult!")
        word_list = input(Fore.BLUE + "Hard or easy? (hard/easy) --->")
        print("\n")
        word_list = word_list.upper()

        while word_list != "HARD" and word_list != "EASY":
            print(Fore.RED + "It seems you typed something wrong... Make sure you type 'easy' for a easy difficult and 'hard' for a hard difficult...")
            word_list = input(Fore.BLUE + "Hard or easy? (hard/easy) --->")
            print("\n")
            word_list = word_list.upper()

        if word_list == "HARD":
            word = random.choice(hard_word_list)

        if word_list == "EASY":
            word = random.choice(easy_word_list)
        
        return word.upper()


def play(word):
    start = "Y"
    display = "_" * len(word)
    letters_guessed = []
    words_guessed = []
    tries = 6
    lenght = len(word)

    delay = input(
        Fore.GREEN + "Would you like a delay of a few seconds between each question? (Y/N)")
    delay = delay.upper()

    if delay != "Y" and delay != "N":
        print(Style.DIM + Fore.RED +
              "Ops... It seems you typed something wrong... Try again!")
        delay = input(
            Fore.GREEN + "Would you like a delay of a few seconds between each question? (Y/N)")
        delay = delay.upper()

    if delay != "Y" and delay != "N":
        print(tyle.DIM + Fore.RED + "I will consider you answer as a 'YES'... ")
        delay = "Y"

    playing = True
    word_to_guess = word

    print("\n")

    if delay == "Y":
        time.sleep(2)

    while start == "Y" and playing == True:
        while tries > 0 and playing == True:
            print("\n")
            print(Fore.RED + "--------------------------------------------------")
            print("\n")
            print(Fore.BLACK + Back.WHITE + "The word is: " + display)
            print(Fore.BLACK + Back.WHITE +
                  "The length of the word is: " + str(lenght) + "!")
            print(Fore.BLACK + Back.WHITE + "You have " +
                  str(tries) + " tries left!")
            print("\n")
            print(Fore.BLACK + Back.WHITE +
                  "Letters guessed: " + str(letters_guessed))
            print(Fore.BLACK + Back.WHITE +
                  "Words guessed: " + str(words_guessed))
            print("\n")
            print(display_hangman(tries))
            print("\n")

            if delay == "Y":
                time.sleep(1)

            guess = input(Style.DIM + Fore.BLUE + "Guess a letter! --->")
            guess = guess.upper()

            guessing = True

            while guessing == True:
                if guess not in letters_guessed:
                    guessing = False
                    continue
                else:
                    print(Fore.RED + "I'm afraid you already guessed this letter...")
                    guess = input(Style.BRIGHT + Fore.BLUE +
                                  "Guess another letter! --->")
                    guess = guess.upper()
                    print("\n")

            letters_guessed.append(guess)

            x = 0
            y = 0
            word = list(word)
            display_list = list(display)
            display = ''
            for i in word:
                if i == guess:
                    display += i
                    x = 1
                else:
                    add = display_list[y]
                    display += str(add)

                y += 1

            display_list = list(display)
            if "_" not in display:
                playing = False

            if delay == "Y":
                time.sleep(1)

            if x == 1 and playing == True:
                print(Fore.BLUE + Style.BRIGHT +
                      "Congrats! You guessed the correct letter!")
                print(Fore.BLUE + Style.BRIGHT +
                      "Now you have a chance of guessing the word!")
                guessing = input(Style.DIM + Fore.BLUE +
                                 "Guess a word? (Y/N) -->")
                guessing = guessing.upper()
                print("\n")

                if delay == "Y":
                    time.sleep(1)
                if guessing == "Y":
                    print(Fore.GREEN + "You already know --->" + display)
                    guess_working = input(
                        Style.DIM + Fore.BLUE + "Take your best guess! --->")
                    guess_working = guess_working.upper()

                    guessing = True
                    while guessing == True:
                        if guess_working not in words_guessed:
                            guessing = False
                            continue
                        else:
                            print(
                                Fore.RED + "I'm afraid you already guessed this word...")
                            guess_working = input(
                                Style.BRIGHT + Fore.BLUE + "Guess another word! --->")
                            guess_working = guess.upper()
                            print("\n")

                    words_guessed.append(guess_working)

                    if guess_working == word_to_guess:
                        if delay == "Y":
                            time.sleep(1)
                        print(Fore.BLUE + Style.BRIGHT +
                              "Congrats! You won! You guessed the correct word!")
                        tries = 6
                        playing = False

                    else:
                        print(Fore.RED + "Uhmm... Wrong word... Try again next time!")
                        if delay == "Y":
                            time.sleep(1)

                else:
                    pass

            else:
                if playing == True:
                    print(Fore.RED + "Uhmmm... Try again next time...")
                    if tries == 4:
                        hint = input(Style.BRIGHT + Back.BLUE +
                                     Fore.WHITE + "Would you like a hint? (Y/N) -->")
                        hint = hint.upper()

                        print(Style.RESET_ALL + "\n")

                        if hint != "Y" and hint != "N":
                            hint = input(
                                Style.RESET_ALL + Fore.RED + "Was it a type error? Would you like a hint???? (Y/N) -->")
                            hint = hint.upper()

                        stop = False
                        if hint == "Y" and stop == False:
                            for ii in word:
                                guess = ii

                                if guess not in letters_guessed and stop == False:
                                    print(Style.RESET_ALL + Fore.GREEN +
                                          "One of the letters is: " + guess)
                                    letters_guessed.append(guess)
                                    display_list = list(display)
                                    display = ''
                                    y = 0
                                    for i in word:
                                        if i == guess:
                                            display += i

                                        else:
                                            add = display_list[y]
                                            display += str(add)

                                        y += 1

                                    print(Style.RESET_ALL + Fore.GREEN +
                                          "Now you know: " + display)
                                    stop = True

                        else:
                            print("Okay...")

                if delay == "Y" and playing == True:
                    time.sleep(1)

                tries -= 1

            print("\n")
            print(Fore.RED + "--------------------------------------------------")
            print("\n")
            if delay == "Y" and playing == True:
                time.sleep(1)

            if tries <= 0:
                playing = False

    if tries <= 0:
        print("\n")
        print("\n")
        if delay == "Y":
            time.sleep(1)
        print(Style.BRIGHT + Back.RED + Fore.WHITE + display_hangman(tries))
        print("\n" + "\n")
        if delay == "Y":
            time.sleep(1)
        print(Fore.RED + "I am afraid you lost... The correct word was: " +
              word_to_guess + "...")

    elif tries >= 0 and playing == False:
        print(Fore.BLUE + Style.BRIGHT + "Congrats! You won! You guessed all the correct letters!!" +
              "The word was: " + word_to_guess + "!")


def display_hangman(tries):
    stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
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
    return stages[tries]


word = get_words()
play(word)
