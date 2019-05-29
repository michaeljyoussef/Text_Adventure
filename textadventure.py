import story #Story

answerOne = ["1", "Yes", "One", "Y", "YES", "ONE", "Choice 1", "A", "T", "TRUE", "True", "true"]
answerTwo = ["2", "No", "Two", "N", "NO", "TWO", "Choice 2", "B", "F", "FALSE", "False", "false"]

isRunning = 0 #Game Running
a = "0" #startVariable
textVar = "A" #setsCurrentFunction
choice = "" #Variable to choose code

while(isRunning == 0):
    chosenFunc = textVar + a
    function = getattr(story,chosenFunc)
    function()
    choice = input("Please select an option.")
    #while(choice not in answerOne or choice not in answerTwo):
    #choice = input("Please select an option.")
    if choice in answerOne:
        a = a + "1"
    elif choice in answerTwo:
        a = a + "2"

print("Thanks for playing! Hope you enjoyed!")