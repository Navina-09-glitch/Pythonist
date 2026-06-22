def learnAI():
    sub1="AI"
    print("To develop '{}' based applications, we use '{}' programming language".format(sub1,lang))
def learnML():
    sub2="ML"
    print("To develop '{}' based applications, we use '{}' programming Lang".format(sub2,lang))
def learnDS():
    sub3="DS"
    print("To develop '{}' based applications, we use '{}' programming Lang".format(sub3,lang))
#Main Program
#learnAI() we cannot access 'lang' inside of learn AI because of 'lang' defined after function call
#learnML() we cannot access 'lang' inside of learn ML because of 'lang' defined after function call
lang="PYTHON" #here lang is called Global Variable
learnDS()