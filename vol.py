def getVowels(word):
    set=[]
    for i in range(len(word)):
        if word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u' :
            set.append(word[i])
    print("Vowels in word are:"+str(set))

word=raw_input("Enter a word")
getVowels(word)