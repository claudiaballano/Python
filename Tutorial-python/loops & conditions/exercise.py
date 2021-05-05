#Create a list of names and use a for loop to output the lenght of each name (len())

names = ['Claudia', 'Marc', 'Aina', 'Carlos', 'Irene', 'Napoleón', 'Josefina', 'Nadia']

for i in range(len(names)):
    #Add an if check inside the loop to only output names longer than 5 characters
    #Add another check to see whether a name includes a 'n' or 'N' character
    names_to_remove= True

    if len(names[i])>5 and ('n' in names[i] or 'N' in names[i]):
        print(names[i])
    
# Use a while loop to empty the list
while len(names)>0:
    names.pop()

print(names)


