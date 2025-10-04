class StringManipulator:

    def find_character(self,text, char):
        return text.find(char)
    
    def find_word_length(self,text):
        return len(text)
    
    def to_upper(self,text):
        return text.upper()
 
name = StringManipulator()

results = name.find_character("example",'x')
print(results)
word_length = name.find_word_length("example")
print(word_length)
upper_case_word = name.to_upper("example")
print(upper_case_word)
