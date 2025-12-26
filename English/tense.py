class Tense:
    def simple(self):
        
        return 
    
    def continuous(self):
        
        return 
    
    def perfect(self):
        
        return
    
    def perfect_continuous(self):
        
        return 
    

class Present(Tense):
    def simple(self,s,v,o):
        result = s+' '+v+' '+o
        return result.capitalize()
    
# class Past(Tense):
    
# class Future(Tense):
    

subject = input("Enter subject ")
verb = input("Enter verb ")
object = input("Enter object ")


present_tense = Present()
text = present_tense.simple(subject,verb,object)
print(text)
