
################################################################################################################################################################################################

#Author: Suleka Helmini (https://github.com/suleka96)

#this model was designed to test using the Enron datase (pre-processed version)
#it can be obtained through the blow link.
#https://www.kaggle.com/crawford/20-newsgroups
#If you are running this in your local machine right out of the batch, download the dataset and put all the emails into one folder called 'emails' which is inside a folder called 'enron'.
#or change the 'direc' to where your emails are

################################################################################################################################################################################################

import os
from collections import Counter
from sklearn.metrics import f1_score, recall_score, precision_score, accuracy_score
from sklearn.linear_model import LogisticRegression


def pre_process():

    #bag-of-words approach

    direc = "enron/email2/"
    files = os.listdir(direc)
    emails = [direc+email for email in files]

    # keeps all the words of all emails
    words = []

    for email in emails:
        f = open(email,encoding="utf8", errors='ignore')
        blob = f.read()
        words += blob.split(" ")
    #turning al uppercase letters into lowercase
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    #making a dictionary of all the words (remove duplicates)
    dict = Counter(words)
    #deleting empty spaces
    del dict[""]
    #getting most common 3000 words from the dictionary
    dictionary = dict.most_common(3000)

    direc = "enron/email2/"
    files = os.listdir(direc)
    #holds all the emails
    emails = [direc + email for email in files]

    feature_set = []
    labels = []

    for email in emails:
        data = []
        f = open(email, encoding="utf8", errors='ignore')
        words = f.read().split(' ')

        for entry in dictionary:
            #for each word in the dictionary, the number of times that word occurs in the email will be appended to the data list
            data.append(words.count(entry[0]))
        feature_set.append(data)
        #preparing the labels
        if "ham" in email:
            labels.append(0)
        else:
            labels.append(1)

    return feature_set, labels


if __name__ == '__main__':


    features, labels = pre_process()


    # splitting features and labels into a testing (20%) and a training set (80%)
    split_frac1 = 0.8

    idx1 = int(len(features) * split_frac1)
    train_x, test_x = features[:idx1], features[idx1:]
    train_y, test_y = labels[:idx1], labels[idx1:]

    #defining the machine learning algorithm
    clf = LogisticRegression()
    #fitting training set to the model (basically training the model)
    clf.fit(train_x, train_y)
    #make a prediction using the testing set
    pred = clf.predict(test_x)

    #evaluating the model
    print("----------------------Logistic Regression------------------------------")
    print("Accuracy score")
    print(accuracy_score(test_y, pred))
    print("F1 score")
    print(f1_score(test_y, pred, average='macro'))
    print("Recall")
    print(recall_score(test_y, pred, average='macro'))
    print("Precision")
    print(precision_score(test_y, pred, average='macro'))




