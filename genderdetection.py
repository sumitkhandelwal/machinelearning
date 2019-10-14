#-------------------------------------------------------------------------------
# Author:      sumit.khandelwal
# Created:     11/10/2019
# Copyright:   (c) sumit.khandelwal 2019
#-------------------------------------------------------------------------------
import random
from nltk.corpus import names
# print the files are avaible in names
print("Print the name of file available in names :", names.fileids())
# Display the names are presernt in female.txt and male.txt
print ("First Five names in Female.txt files :", names.words('female.txt')[:5])
print ("First Five names in Male.txt files :",names.words('male.txt')[:5])
# Building the classifier
label_name = [] # List of name of female and male names
# Adding Female names
for i in names.words('female.txt'):
    label_name.append((i,'female'))
# Adding male names
for i in names.words('male.txt'):
    label_name.append((i,'male'))
# print 5 file elements from a list
print(label_name[:5])
# Shuffle the data by calling random package for proper visualization
random.shuffle(label_name)
# print 5 file elements from a list
print(label_name[:5])
# Generate the features
# Feature extractor : Decide the feature as per last letter of name
def feature_exact(word):
    return {'last_letter_of_word ': word[-1]}
features = [] # Collect all feature in list
for (n, gender) in label_name:
    features.append((feature_exact(n),gender)) # Append the the last letter and gender in a list
for i in range(10): # print first 10 entries in a feature.
    print (features[i])
# Finalized Train and Test data from all feature data
n = int (len(features) * 0.8)
train_data = features[:n]
test_data = features[n:]
# Call Naive Bayes Classifier
from nltk import NaiveBayesClassifier
classifier_NB = NaiveBayesClassifier.train(train_data)
# Finding out classifier label
print("The Naive Bayes Classifier label is :", classifier_NB.labels())
# Finding out the accuracy of model
from nltk.classify  import accuracy
accuracy = accuracy(classifier_NB,test_data)
print ("Accuracy of a model is :", accuracy)

'''
# Call Decision Tree Classifier
from nltk import DecisionTreeClassifier
classifier_DT = DecisionTreeClassifier.train(train_data)
# Finding out classifier label
print("The Decision Tree Classifier label is :", classifier_DT.labels())
# Finding out the accuracy of model
from nltk.classify  import accuracy
accuracy1 = accuracy(classifier_DT,test_data)
print ("Accuracy of a model is :", accuracy1)

# Call Maxent Classifier
from nltk import MaxentClassifier
classifier_MC = MaxentClassifier.train(train_data)
# Finding out classifier label
print("The Maxent Classifier label is :", classifier_MC.labels())
# Finding out the accuracy of model
from nltk.classify  import accuracy
accuracy2 = accuracy(classifier_MC,test_data)
print ("Accuracy of a model is :", accuracy2)

# Call Conditional Exponential Classifier
from nltk import ConditionalExponentialClassifier
classifier_CE = ConditionalExponentialClassifier.train(train_data)
# Finding out classifier label
print("The Maxent Classifier label is :", classifier_MC.labels())
# Finding out the accuracy of model
from nltk.classify  import accuracy
accuracy3 = accuracy(classifier_CE,test_data)
print ("Accuracy of a model is :", accuracy3)
'''

# Testing of Model with TKinter GUI structure
import tkinter as tk
acc = accuracy
def show_entry_fields():
    new_name = str(e1.get())
    labelResult.config(text="Gender is =  %s " % classifier_NB.classify(feature_exact(new_name)))
master = tk.Tk()
acc = accuracy
master.title('Gender Finder')
master.geometry('400x200+100+200')
tk.Label(master, text="Name").grid(row=0)
e1 = tk.Entry(master)
e1.grid(row=0, column=1)
labelResult = tk.Label(master)
labelResult.grid(row=7, column=2)
tk.Button(master,text='Quit',command=master.quit).grid(row=3, column=0, sticky=tk.W,pady=4)
tk.Button(master,text='Show', command=show_entry_fields).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.mainloop()
