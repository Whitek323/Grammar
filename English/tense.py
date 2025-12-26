from parts_of_speech import PartsOfSpeech

class Tense:
    def simple(self):
        
        return 
    
    
    def _verb_have_s(self,s,v):
        
        return 
    
    def _verb_to_ing(self,s,v):
        s = self._verb_to_be(s)
        result = v+'ing'
        return result
    
    def _verb_to_be(self,s):
        s_lower = s.lower()
        if s_lower == 'i':
            s_lower += ' am'
            
        elif s_lower == 'you' or s_lower == 'we' or s_lower == 'they':
            s_lower += ' are'
            
        elif s_lower == 'he' or s_lower == 'she' or s_lower == 'it':
            s_lower += ' is'
        
        return s_lower
    
    def _verb_to_have(self,s):
        if PartsOfSpeech.Pronoun._subject_is_sigular(s):
            return 'has'
        else:
            return 'have' 
            
        
class Present(Tense):
    def simple(self,s,v,o):
        result = s+' '+v+' '+o
        if PartsOfSpeech.Pronoun._subject_is_sigular(s):
            result = s+' '+v+'s '+o
            
        return result.capitalize()
    
    def continuous(self,s,v,o):
        result = s+' '+self._verb_to_ing(s,v)+' '+o
        
        return result.capitalize()
    
    def perfect(self,s,v,o):
        result = s+' '+self._verb_to_have(s)+' '+v+' '+o
        return result.capitalize()
    
    def perfect_continuous(self,s,v,o):
        result = s+' '+self._verb_to_have(s)+' been '
        + self._verb_to_ing(s,v)+' '+o
        return result.capitalize()
    
    
# class Past(Tense):
    
# class Future(Tense):
    

subject = input("Enter subject\t")
verb = input("Enter verb\t")
object = input("Enter object\t")


present_tense = Present()
print_present_simple = present_tense.simple(subject,verb,object)
print_present_continue = present_tense.continuous(subject,verb,object)
print_present_perfect = present_tense.perfect(subject,verb,object)
print_present_perfect_continue = present_tense.perfect_continuous(subject,verb,object)

print("\nPresent Simple : "+print_present_simple)
print("Present Continue : "+print_present_continue)
print("Present Perfect : "+print_present_perfect)
print("Present Perfect Continuuous: "+print_present_perfect_continue)
