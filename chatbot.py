
word=""
while word!="bye":
    word=input("Enter the word u want to talk with chatbot:").lower()
    if word=="hello":
        print("hii")
    elif word=="how are you" or word=="how r u?" or word=="how are you?":
        print("i'm fine,thank you")
    elif word=="bye":
        print("goodbye")
        exit()
    else:
        print("i didn't understand!")