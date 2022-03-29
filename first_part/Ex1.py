# ********* Exercice : 1 


# print every number between 1 and 100 as follows:
#For every multiple of 3 print "Three".
#For every multiple of 5 print "Five".
#And for every multiple of both 3 and 5 print "ThreeFive"


for n in range(1,100):
     
   
    if n % 15 == 0:
        print("THREEFIVE")                                        
        continue
 
   
    elif n % 3 == 0:    
        print("THREE")                                        
        continue
 
   
    elif n % 5 == 0:        
        print("FIVE")                                    
        continue
 

    print(n)