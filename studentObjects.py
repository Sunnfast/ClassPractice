'''
Programming Lab 7
Simone Christen
'''
# declare student object
class Student: 
  # intialize some values for the 7 data members
  def __init__(self): 
    self.name = "name"
    self.address = "address"
    self.state = "state"
    self.zip = 12345
    self.studentId = 123456
    self.gpa = 2.5
    
  def getInput(self):
    '''Collects input from the user and assigns it to the appropriate data member.'''
    print("Enter the name for this student: ") # prompts the user on which data member they will be assigning a value to
    self.name = str(input()) # convert input into the appropriate data type for the input

    print("Enter the address for this student: ")
    self.address = str(input())

    print("Enter the city for this student: ")
    self.city = str(input())
    
    print("Enter the state for this student: ")
    self.state = str(input())
    
    print("Enter the zip for this student: ")
    self.zip = str(input())
    # if I had the time I can go back and also try to do try statements or simple conditionals/while loop to check input data types to avoid giving the user the ability to completely crash the python program
    print("Enter the student ID for this student: ")
    self.studentID = int(input())

    print("Enter the gpa for this student: ")
    self.gpa = float(input())
  

  def printOut(self):
    '''Prints out the values of each data member.'''
    
    print("Output for ", self.name)
    print("Name: ", self.name)
    print("Street Address: ", self.address)
    print("City: ", self.city)
    print("Zip Code: ", self.zip)
    print("GPA: ", self.gpa)

# make 3 unitialized Student instances; objects named after characters from The Locked Tomb series

Harrowhark = Student()
Gideon = Student()
Camilla = Student()

Harrowhark.getInput() # gather input for Harrow
print("\n") # prints a blank line to make print statements a touch easier to read
Gideon.getInput() # gather input for Gideon
print("\n")
Camilla.getInput() # gather input for Camilla
print("\n")
Harrowhark.printOut() # print back out the input as the nicely formatted version as per the printOut() function
print("\n")
Gideon.printOut()
print("\n")
Camilla.printOut()