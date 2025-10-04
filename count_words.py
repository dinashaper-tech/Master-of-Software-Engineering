#Week3- Activity 2: count the words in the demo text file
#Develop a new project that reads demo.txt and returns the total number of words. 


class StringManipulator:
    def __init__(self,text):
        self.text = text

    def word_count(self):
        return len(self.text.strip().split())
   
    
if __name__ == "__main__":
    with open("demo.txt",encoding="utf-8", errors="replace") as data:
        content = data.read()  # Read the whole file as one string

    text = StringManipulator(content)
    count = text.word_count()
    print(count) #134046





