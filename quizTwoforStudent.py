"""
Student Name: Adrian Cedric O. Calindas
Course, Year, and Section: CS3B
Quiz No.: 2
Date: 10/11/2024
"""

studentName = "Lewis Fonsi" 
studentAddress = "City of Candon, Ilocos Sur" 
studentFavNum1 = 25                                 #declared an int
studentAge = 25    
studentAllowance = float(500)                      #declared a float by simply type the data type along with the value inside the parenthesis

classmateName = "Andrea Andres" 
classmateAddress = "City of Vigan, locos Sur" 
classmatefavNum1 = "18"                             #declared a string number
classmateAge = "21"
classmateAllowance = "700"

sName_Length =  len(studentName)
cName_Length = len(classmateName)

if "Ilocos Sur" in studentAddress and classmateAddress:
    print(studentName + " is from " + studentAddress)  #like an english sentence, if "Ilocos Sur" is included in the variable i assigned, it prints the output from line 24 and 25 followed by their word length if it's greater than the other variable (student and classmate's names)
    print(classmateName + " is from " + classmateAddress)
    if sName_Length > cName_Length:
        print("Andrea Andres has a longer name than Lewis Fonsi with 13 letters over 11 letters. ")
    else:
        print("Lewis Fonsi has a longer name than Andrea Andres with 13 letters over 11 letters.")
elif "Ilocos Sur" in studentAddress and classmateAddress:     
    sName_Split = studentName.split(" ")                   #it splits " " in between the student and classmate's names
    cName_Split = classmateName.split(" ")
    print(f"One among {sName_Split} or {cName_Split} Lives in Ilocos Sur")  #f is an easy way to concat statements
else:
    print("None of the Students live in Ilocos Sur")

addedAge = ((studentAge) + int(classmateAge))
print(f"The added age of Lewis Fonsi and Andrea Anfres is: {addedAge}")

subtractedFavNums = (studentFavNum1 - int(classmatefavNum1))
print(f"The subtracted value of favenum of Lewis Fonsi and Andea Andres is: {subtractedFavNums}")  

combinedWeeklyAllowance = (studentAllowance + float(classmateAllowance))
print(f"The weekly allowance of Lewis Fonsi and Andrea Andres is {combinedWeeklyAllowance:.2f} pesos")  #:.2f it determines how many decimals

classList = [studentName, classmateName]
classList_Ext = [studentAddress, classmateAddress]
classList.extend(classList_Ext)
for x in classList:      #prints it in for loop in iterating over a sequence
    print(x)

classNumbers = [studentAge, studentAllowance, studentFavNum1]
classNumbers.append(int(classmateAge))
classNumbers.append(int(classmatefavNum1))         #printing all the values that is already declared throughout the code and sort it
classNumbers.append(int(classmateAllowance))
classNumbers.sort()
for y in classNumbers:
    print(y)

def quizTwo():
    studenNameCS = "Calindas"
    print(f"Congratulations on Quiz 2 {studenNameCS}") #calling a functon
quizTwo()
