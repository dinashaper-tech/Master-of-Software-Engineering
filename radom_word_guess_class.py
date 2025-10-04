from wonderwords import RandomWord

class WordGuessGame:
    def __init__(self):
        self.word = RandomWord().word(include_parts_of_speech=["nouns"]).lower()
        self.guessed, self.turns = set(), len(self.word)

    def play(self):
        print(f"\nThe word has {len(self.word)} letters.")
        while self.turns > 0:
            display = "".join(ch if ch in self.guessed else "_" for ch in self.word)
            print("Word:", display)
            if "_" not in display:
                return print(f"You guessed it! The word was: {self.word}")
            letter = input("Enter a letter: ").lower()
            if len(letter) != 1 or not letter.isalpha():
                print("Enter a single letter."); continue
            if letter in self.guessed:
                print("Already guessed."); continue
            if letter in self.word:
                self.guessed.add(letter); print("Correct!")
            else:
                self.turns -= 1; print(f"No luck. Turns left: {self.turns}")
        print(f"Out of turns! The word was: {self.word}")

if __name__ == "__main__":
    WordGuessGame().play()
