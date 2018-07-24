def Reverse_Word(word):
    w=[]
    for i in range(0,len(word)):
        w.append(word[len(word)-(i+1)])
    word=''.join(w)
    print("Reversed word="+word)

a=raw_input("Enter a word")
Reverse_Word(a)