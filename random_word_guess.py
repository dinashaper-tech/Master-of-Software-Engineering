from wonderwords import RandomWord

rw = RandomWord()

def generate_random_word():
    return rw.word(include_parts_of_speech=["nouns"])

def guess_random_word(random_word):
    turns = len(random_word)
    guessed_letters = set()  
    print(f"\nThe word has {len(random_word)} letters.") 
    
    while turns > 0:

        display_word = "".join([letter if letter in guessed_letters else "_" for letter in random_word])
        print("Word:", display_word)
        
        if "_" not in display_word:
            print("You guessed it! The word was:", random_word)
            return
 
        letter = input("Enter a letter: ").lower()
        
        if letter in random_word:
            guessed_letters.add(letter)
            print("Correct guess!")
        else:
            turns -= 1
            print(f"No luck. Turns left: {turns}")
    
    print("Out of turns! The word was:", random_word)


if __name__ == "__main__":
    word = generate_random_word()
    guess_random_word(word)
