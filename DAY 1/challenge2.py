def lengthOfTheLastWord(sentence) :
    sentenceCopy = sentence.strip() #Used to trim spaces
    wordLength = 0 #assumed length

    for i in range(len(sentenceCopy)):
        if sentenceCopy[i] == " ":
            wordLength = 0
        else: 
            wordLength += 1
    return wordLength

#This is used as an entry point to execute code only if the file was run directly and not imported
if __name__ == "__main__" :
    sentence = input("Write a sentence: ")
    print("The length of the last word is: ", lengthOfTheLastWord(sentence))

