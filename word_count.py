#Week 2 - Activity 5: Develop a project to work with Strings

class StringManipulator:

    def __init__(self,sentence):
        self.sentence = sentence

    def word_count(self):
        return len(self.sentence.strip().split())
    
if __name__ == "__main__":
    sentence = input("Enter your sentense: ")
    name = StringManipulator(sentence)
    count = name.word_count()
    print(count)


