"""
By:

Rezwan Karim Ayon; 501196212

Abdullah Al Mahi Ononno; 501152685

Zahra Hossain; 501156177

Mohammad Nuaiman Hasan; 501151286
"""

import csv
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


dataFrame = pd.read_csv("Use of ChatGPT.csv")

# Working with the csv file and making counts to use them to plot praphs
with open("Use of ChatGPT.csv") as csvFile:
    csvReader = csv.DictReader(csvFile)
    KnowChatGPTcount = Counter()
    AgeGroupcount = Counter()
    EthnicityCount = Counter()
    Facultycount = Counter()
    Usagecount = Counter()
    Plagiarismcount = Counter()
    AllowGPTcount = Counter()
    UseCount = Counter()
    UseCount2 = Counter()
    UseCount3 = Counter()

    for row in csvReader:
        KnowChatGPTcount.update(row['Do you know what is ChatGPT?'].split(';'))
        AgeGroupcount.update(row['What is your age or what age group do you belong to?'].split(';'))
        EthnicityCount.update(row['What is your ethnicity?'].split(';'))
        Facultycount.update(row['You are under what faculty?'].split(';'))

        if row['Do you use ChatGPT?'] != '':
            Usagecount.update(row['Do you use ChatGPT?'].split(';'))

        if row['Do you think ChatGPT is plagiarism in and of itself? '] != '':
            Plagiarismcount.update((row['Do you think ChatGPT is plagiarism in and of itself? '].split(';')))
        if row['Do you think ChatGPT is plagiarism in and of itself? (If you use ChatGPT) '] != '':
            Plagiarismcount.update((row['Do you think ChatGPT is plagiarism in and of itself? (If you use ChatGPT) '].split(';')))
        if row['Do you think ChatGPT is plagiarism in and of itself?  (If you do not use ChatGPT) '] != '':
            Plagiarismcount.update((row['Do you think ChatGPT is plagiarism in and of itself?  (If you do not use '
                                        'ChatGPT) '].split(';')))

        if row['Do you think universities should allow the use of ChatGPT?'] != '':
            AllowGPTcount.update((row['Do you think universities should allow the use of ChatGPT?'].split(';')))
        if row['Do you think universities should allow the use of ChatGPT? (If you use ChatGPT)'] != '':
            AllowGPTcount.update((row['Do you think universities should allow the use of ChatGPT? (If you use ChatGPT)'].split(';')))
        if row['Do you think universities should allow the use of ChatGPT? (If you do not use ChatGPT)'] != '':
            AllowGPTcount.update((row['Do you think universities should allow the use of ChatGPT? (If you do not use '
                                      'ChatGPT)'].split(';')))

        if row['What do you think you could use ChatGPT for? (Select all that applies)'] != '':
            UseCount.update((row['What do you think you could use ChatGPT for? (Select all that applies)'].split(';')))

        if row['Now that you have an idea of what ChatGPT is, what would be the use of ChatGPT by students? (Select ' 
               'all that applies) '] != '':
            UseCount2.update((row['Now that you have an idea of what ChatGPT is, what would be the use of ChatGPT by '
                                 'students? (Select all that applies) '].split(';')))
        if row['In what way do you think ChatGPT is beneficial to education? (Select all that applies) '] != '':
            UseCount3.update((row['In what way do you think ChatGPT is beneficial to education? (Select all that '
                                 'applies) '].split(';')))



# Number of people who knows ChatGPT bar graph
answer = KnowChatGPTcount.keys()
answerCount = KnowChatGPTcount.values()
plt.ylabel("Number of people")
plt.title('Do you know what ChatGPT is?')
plt.bar(answer, answerCount)
plt.show()

# Genders pie chart
plt.pie(dataFrame["What is your gender?"].value_counts(), labels = ['Male', 'Female', 'Prefer Not To Say'])
plt.title("GENDERS")
plt.show()

# Age Group bar chart
ages = AgeGroupcount.keys()
ageCount = AgeGroupcount.values()
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.title("Age Groups")
plt.bar(ages, ageCount)
plt.show()

# Ethnicities pie chart
ethnicities = EthnicityCount.keys()
ethCount = EthnicityCount.values()
plt.title("Ethnicity Groups")
plt.pie(ethCount, labels=ethnicities)
plt.show()

# Faculties pie chart
faculties = Facultycount.keys()
faCount = Facultycount.values()
plt.title("Faculty of study")
plt.pie(faCount, labels=faculties)
plt.show()

# How many people use chatGPT
ChatGPTusers = Usagecount.keys()
userCount = Usagecount.values()
plt.title('How many people use ChatGPT?')
plt.pie(userCount, labels=ChatGPTusers)
plt.show()

# Is ChatGPT a type of plagiarism?
OpinionPlagiarism = Plagiarismcount.keys()
plagCount = Plagiarismcount.values()
plt.title('Is ChatGPT a type of plagiarism?')
plt.pie(plagCount, labels=OpinionPlagiarism)
plt.show()

# Should ChatGPT be allowed in universities
OpinionAllow = AllowGPTcount.keys()
allowCount = AllowGPTcount.values()
plt.title('Should ChatGPT be allowed in universities?')
plt.pie(allowCount, labels=OpinionAllow)
plt.show()

# usages of ChatGPT
uses = UseCount.keys()
usesCount = UseCount.values()
plt.xlabel("Uses")
plt.ylabel("Number of people")
plt.title("All the Usages of ChatGPT")
plt.xticks(fontsize=10)
plt.bar(uses, usesCount)
plt.show()
uses = UseCount2.keys()
usesCount = UseCount2.values()
plt.xlabel("Uses")
plt.ylabel("Number of people")
plt.title("All the Usages of ChatGPT")
plt.xticks(fontsize=5)
plt.bar(uses, usesCount)
plt.show()

# Correlation between usage and opinion of how detrimental ChatGPT is
x = dataFrame['On a scale of 5 how do you think that the use of AI tools such as ChatGPT would inhibit education? (' \
              'using ChatGPT) ']
y = dataFrame['On a scale of 10, how often do you use it?']
plt.xlabel('How much would ChatGPT inhibit education?')
plt.ylabel('How often do you use it?')
plt.scatter(x, y)
plt.show()