#Question Four
phrase= input("Enter a Phrase ")
n = int(input("Enter How Many Times You Want To print Your Phrase: "))


def repeatPhrase(phrase, n):
    x=0
    while x<n :
        print (phrase.lower())
        x=x+1
        if x<n:
            print (phrase.upper())
            x=x+1
        
repeatPhrase(phrase, n)
