import random
import operator
wrong = 0
correct = 0


print("\nEnter difficulty level (1 or 2): ", end = "")
user = int(input())

print("1 = addition\n2 = Subtraction\n3 = Multiplication\n4 = Division\n5 = mixed operations")
print("Enter the operation(1 to 5) (-1 to exit): ", end = "")
inpt = int(input())

def math():
        return(random.randint(0,9), random.randint(0,9))
def math2():
        return(random.randint(10,99), random.randint(10,99))
x,y = math()
m,z = math2()

def corrects():
   global correct
   a=random.randint(1,3)
   if(a==1):
       print ("Very good!")
   elif(a==2):
       print ("Nice work!")
   elif(a==3):
       print ("Keep up the good work!")

  

def wrongs():

   global wrong
   a=random.randint(1,3)
   if(a==1):
       print ("No. Please try again.")
   elif(a==2):
       print ("Wrong. Try once more. ")
   elif(a==3):
       print ("No.Keep Trying")
       
def grade():
        print("Number of correct answers: ", correct)
        print("Number of wrong answers: ", wrong)
        print("Thanks for playing!")
        
def chooseType(inpt):
    global wrong
    global correct
    
    if (inpt == 1):
        addition()
    elif(inpt == 2):
        subtraction()
    elif(inpt == 3):
        multiplication()
    elif(inpt == 4):
        division()
    elif(inpt == 5):
        mix()
        
def addition():
    x,y = math()
    m,z = math2()
    global wrong
    global correct
    
    if user == 1:
        print("how much is " , str(x), "plus", str(y), "?")
        print("Enter your answer", end = "")
        ans = int(input())
        
        if (x+y) == ans:
            
            corrects()
            correct = correct + 1
        else:
            while (x+y != ans):
                wrongs()
                wrong = wrong + 1
                ans = int(input("Enter your answer"))
            corrects()
        if ans == -1:
                grade()

    if user == 2:
        print("how much is " , str(m), "plus", str(z), "?")
        print("Enter your answer", end = "")
        ans = int(input())
        
        if (m+z) == ans:
            
            corrects()
            correct = correct + 1
        else:
            while (m+z != ans):
                wrongs()
                wrong = wrong + 1
                ans = int(input("Enter your answer"))
            corrects()
        if ans == -1:
                grade()

def subtraction():
    x,y = math()
    m,z = math2()
    global wrong
    global correct
    
    if user == 1:
        if str(x) < str(y):
            print("How much is ",str(y), "minus", str(x))
            result = y-x
        else:
            print("How much is ",str(x), "minus", str(y))
            result = x-y

        
        print("Enter your answer", end = "")
        ans = int(input())
        
        
        if (result) == ans:
            
            corrects()
            correct = correct + 1
        else:
            while (result != ans):
                wrongs()
                wrong = wrong + 1
                ans = int(input("Enter your answer"))
            corrects()
        if ans == -1:
                grade()


    if user == 2:
        if str(m) < str(z):
            print("How much is ",str(z), "minus", str(m))
            result = z-m
        else:
            print("How much is ",str(m), "minus", str(z))
            result = m-z
        
        print("Enter your answer", end = "")
        ans = int(input())
        
        if (result) == ans:
            
            corrects()
            correct = correct + 1
        else:
            while (result != ans):
                wrongs()
                wrong = wrong + 1
                ans = int(input("Enter your answer"))
            corrects()
        if ans == -1:
                grade()

def multiplication():
    x,y = math()
    m,z = math2()
    global wrong
    global correct
            
    if user == 1:
        print("how much is " , str(x), "times", str(y), "?")
        print("Enter your answer", end = "")
        ans = int(input())
                                
        if (x*y) == ans:
                corrects()
                correct = correct + 1
                        
        else:
                while (x*y != ans):
                        wrongs()
                        wrong = wrong + 1
                        ans = int(input("Enter your answer"))
                corrects()
                

    if user == 2:
        print("how much is " , str(m), "times", str(z), "?")
        print("Enter your answer", end = "")
        ans = int(input())
        
        if (m*z) == ans:
            
            corrects()
            correct = correct + 1
        else:
            while (m*z != ans):
                wrongs()
                wrong = wrong + 1
                ans = int(input("Enter your answer"))
            corrects()

            
def division():
    x,y = math()
    m,z = math2()
    global wrong
    global correct
    
    if user == 1:
        
        if str(x) < str(y):
            print("How much is ",str(y), "divided by", str(x))
            if str(x) == 0:
                    x = 1
                    print("How much is ", y, "divided by", x)
                    result = y//1
            else: 
                    result = y//x
        else:
            print("How much is ",str(x), "divided by", str(y))
            if str(y) == 0:
                    y = 1
                    print("How much is ", x, "divided by", y)
                    result = x//1
            else:
                    result = x//y
        
 
        print("Enter your answer", end = "")
        ans = int(input())
        
        
        if (result) == ans:
            
            corrects()
            correct = correct + 1
        else:
            while (result != ans):
                wrongs()
                wrong = wrong + 1
                ans = int(input("Enter your answer"))
            corrects()
        if ans == -1:
            grade()

    if user == 2:
        if str(m) < str(z):
            print("How much is ",str(z), "divided by", str(m))
            result = z//m
        else:
            print("How much is ",str(m), "divided by", str(z))
            result = m//z


        
        print("Enter your answer", end = "")
        ans = int(input())
        
        if (result) == ans:
            
            corrects()
            correct = correct + 1
        else:
            while (result != ans):
                wrongs()
                wrong = wrong + 1
                ans = int(input("Enter your answer"))
            corrects()
        if ans == -1:
                grade()
def mix():
    x,y = math()
    m,z = math2()
    global wrong
    global correct

    operators = [operator.add , operator.sub , operator.mul ,operator.floordiv]
    random_operator = random.choice(operators)
    
    if user == 1:
        
        if random_operator == operator.add:
            print("How much is ",str(x), "plus", str(y))
            result = random_operator(x,y)
        if random_operator == operator.sub:
            if str(x) < str(y):
                print("How much is ",str(y), "minus", str(x))
                result = random_operator(y,x)
            else:
                print("How much is ",str(x), "minus", str(y))
                result = random_operator(x,y)
                

        if random_operator == operator.mul:
            print("How much is ",str(x), "times", str(y))
            result = random_operator(x,y)
        if random_operator == operator.floordiv:
            if str(x) < str(y):
                print("How much is ",str(y), "divided by", str(x))
                result = random_operator(y,x)
            else:
                print("How much is ",str(x), "divided by", str(y))
                result = random_operator(x,y)
 
            
        print("Enter your answer", end = "")
        ans = int(input())
        
        
        if (result) == ans:
            
            corrects()
            correct = correct + 1
        else:
            while (result != ans):
                wrongs()
                wrong = wrong + 1
                ans = int(input("Enter your answer"))
            corrects()
        if ans == -1:
                grade()

    if user == 2:
        
        if random_operator == operator.add:
            print("How much is ",str(m), "plus", str(z))
        if random_operator == operator.sub:
            print("How much is ",str(m), "minus", str(z))
            if str(m) < str(z):
                print("How much is ",str(y), "minus", str(x))
                result = z-m
            else:
                print("How much is ",str(m), "minus", str(z))
                result = m-z
 
        if random_operator == operator.mul:
            print("How much is ",str(m), "times", str(z))
        if random_operator == operator.floordiv:
            if str(m) < str(z):
                print("How much is ",str(z), "divided by", str(m))
                result = z//m
            else:
                print("How much is ",str(m), "divided by", str(z))
                result = m//z
                
        result = random_operator(m,z)

        print("Enter your answer", end = "")
        ans = int(input())
        
        if result == ans:
            
            corrects()
            correct = correct + 1
        else:
            while (result != ans):
                wrongs()
                wrong = wrong + 1
                ans = int(input("Enter your answer"))
            corrects()
        if ans == -1:
                grade()



            
while inpt != -1:
        chooseType(inpt)
        print("\nEnter difficulty level (1 or 2): ", end = "")
        user = int(input())

        print("1 = addition\n2 = Subtraction\n3 = Multiplication\n4 = Division\n5 = mixed operations")
        print("Enter the operation(1 to 5) (-1 to exit):", end = "")
        inpt = int(input())
        if inpt == -1:
                grade()
