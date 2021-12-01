name = input("what is your name ? \n")#this prompts the user for input which is assigned to the name variable
if name == "Arya stark":# == checks to see for equality,if the condition is satisfied,it'll print out the message
    print("Valar Morghulis")
elif name == "Jon snow":#if the first condition wasn't satisfied ,it'll come to see if the second condition is met,if the second condition is satisfied ,it'll execute the print function,if not it'll skip to the next condition
    print("You know nothing")
elif name == ("Brieanne of Tarth"):#it is important not to forget to place a colon after a conditional statement so that it automatically indents into a block of executable code for the respective condition
    print("i love Jamie Lanister")    
else:#the else condition means ,if all conditions were  not met,do this instead
    print("carry on")         