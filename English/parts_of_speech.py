class PartsOfSpeech:
    def __init__(self):
        pass
    
    class Pronoun:
        def _subject_is_sigular(s):
            s_lower = s.lower()
            
            if s_lower == 'he' or s_lower == 'she' or s_lower == 'it':
                return True
            if s_lower == 'i' or s_lower == 'you' or s_lower== 'we' or s_lower=='they':
                return False
