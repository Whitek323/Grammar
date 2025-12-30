from src.parts_of_speech import PartsOfSpeech

class Grammar:
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
            

    
    
# class Past(Tense):
    
# class Future(Tense):
    
