name = input()
description = input()

function = False
within = False
var = False
string = ""
"""for word in description:
    if ".py" in word:
        name = word
        greet = open(name, 'w')
    if "" != word:
        print(name)
        greet = open(name, 'a')
    elif "def" == word:
        function = True
    elif function == True:
        function = False
        within = True
        greet.write("def " + word + "():\n\tpass")
    elif within == True:
        if "define" == word:
            var = True
        if 

    greet.close()"""

description = description.split(" ")

writefile = open(name, 'w')

for word in description:
    if "define" == word:
        var = True
        print(var)
    elif var == True:
        var = word
        print(var)
    elif type(var) == str:
        if word == "String":
            string = True
        else:
            string = False
        print(string)
    elif type(string) == bool:
        print("yes")
        if string == True:
            line = var + " = '" + word + "'"
            writefile.write(line)
            writefile.write("\n")
        else:
            writefile.write(var + " = " + word)
            writefile.write("\n")
    elif "def" == word:
        function = True
    elif function == True:
        function = False
        within = True
        line = "def " + word + "():\n\tpass"
        writefile.write(line)
