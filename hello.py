#///3 main statements are numbers/strings/boolean(true or false )
#-----the print statement, how to print a string or group of characters

#character_name = "Zerolina"
#character_age = "28"
#print("There once was a girl called " + character_name + ",") 
#print("She was "+ character_age + "years old. ")
#character_age = "50"
#print("After "+ character_age +  " years of creativity "+ character_name +" finnaly met arduino,")
#print("but hated basic electronica.")
#--------------------------------
#print("becode\"academy") //use backslach to start a new line
#--------------------------------
#///appending strings (concatenation)
#phrase = "Cath is awesome"
#print(phrase + "and very dark")
#--------------------------------
#///use functions
#phrase = "Cath is awesome"
#print(phrase.upper().isupper())
#----string slicing
#first = phrase[3] #starts counting at 0
#space = phrase[4]
#last = phrase[len(phrase)-1]
#print(phrase[-2])
#---string slicing with step
phrase = "Cath is awesome" #15
#print(phrase[5:7]) #(start:end)
#print(phrase[8:len(phrase)]) #start:lenght phrase 
#print(phrase[0:7:2]) #start:lenght of charachters:steps to jump
#----reversed sliding
#print(phrase[10:1:-1]) #ewa si ht
#print(phrase[10:3:-2]) #ea s
#----partial slicing
#print(phrase[:6]) #all characters before :s
#print(phrase[6:]) #all characters after s:
#print(phrase[:]) #the whole string
#print(phrase[::-1]) #the hole string in reverse
#------reverse logic by using intex function
print(phrase.index("is")) #locate the characterposition


