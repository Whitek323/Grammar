from src import *
      
class Tense(Grammar):
    def __init__(self):
        self.tenseType = "present"
        
    def simple(self,s,v,o):
        result = s+' '+v+' '+o
        if PartsOfSpeech.Pronoun._subject_is_sigular(s):
            if self.tenseType == "present":
                result = s+' '+v+'s '+o
            else:
                return "Error"
            
        return result.capitalize()
    
    def continuous(self,s,v,o):
        result = s+' '+self._verb_to_ing(s,v)+' '+o
        
        return result.capitalize()
    
    def perfect(self,s,v,o):
        result = s+' '+self._verb_to_have(s)+' '+v+' '+o
        return result.capitalize()
    
    def perfect_continuous(self,s,v,o):
        result = s+' '+self._verb_to_have(s)+' been '+o
        return result.capitalize()