class StringManipulator:
    #more professional to have initializer
    def __init__(self,text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def find_word_length(self):
        return len(self.text)
    
    def to_upper(self):
        return self.text.upper()

#create a object    
name = StringManipulator("example")

results = name.find_character('x')
print(results)
word_length = name.find_word_length()
print(word_length)
upper_case_word = name.to_upper()
print(upper_case_word)
