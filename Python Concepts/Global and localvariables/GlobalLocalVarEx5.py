#In this program we are trying to access local variables in one function in other function
def learnAI():
    sub1 = "AI"  # Local Var
    print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub1, lang))
    #print(sub2,sub3)We cannot access sub2 and sub3 because they are local in other functions

def learnML():
    sub2 = "ML"  # Local Var
    print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub2, lang))
    #print(sub1,sub3)We cannot access sub2 and sub3 because they are local in other functions

def learnDS():
    sub3 = "DS"  # Local Var
    print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub3, lang))
    #print(sub1,sub3)we cannot access sub1 and sub3 because they are local in other functions

# Main Program
lang = "PYTHON"  # here lang is called Global Variable
learnAI()
learnML()
learnDS()