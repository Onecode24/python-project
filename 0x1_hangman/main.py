from random import seed
from random import randint


# Random word generation from list
def getWord(lists):
    n = len(lists)
    i = randint(0,n)
    return lists[i-1]

# Chek if gammer found the word
def foundWord(word):
    for j in range(len(word)):
        if word[j]=="_":
            return True
        # print(j)
    return False

# Check if the letter is in the word and return the word
def foundLetter(guessWord,word,letter):
    for j in range(len(word)):
        if word[j]==letter:
            newStr = list(guessWord)
            newStr[j]=letter
            guessWord= "".join(newStr)
    return guessWord

# main function
def main():
    print("----------Start hangman game------------")

    lists = ["succes","moto","voitures","avion","maison","impertubable"]

    word = getWord(lists)
    guessWord = ""
    guessWord += "_"*len(word)
    print("_ "*len(word))
    # print(guessWord)
    n=0

    while foundWord(guessWord):
        letter = input("Enter one letter: ")
        guessWord = foundLetter(guessWord,word,letter)
        for i in range(len(guessWord)):
            print(guessWord[i]+" ",end='')
        print()
        n = n+1
        if(n>=10):
            break

    if n<10:
        print("Congratulation you guess the world "+word)
    else:
        print("You lose the world was "+word)

# Start a programm
main()