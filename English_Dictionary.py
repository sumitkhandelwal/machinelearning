from nltk.corpus import wordnet
flag = 1
while(flag == 1):
    str1 = str(input("Enter your word :")) # We are going to take input from user
    word = wordnet.synsets(str1)
    print ("Meaning of Your word ", str1 ," is :", end ='')
    print(word[0].definition())
    flag1 = int(input("Press 0 to stop or Press 1 to continue."))
    flag = flag1
    if(flag==0):
        break