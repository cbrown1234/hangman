import random

words = [
    'some',
    'words',
    'which',
    'test',
    'the',
    'game',
]


class Game:
    max_misses = 8

    def __init__(self, word: str):
        self.word = word.lower()
        self.known_letters = '_'*len(self.word)
        self.guess = '?'
        self.misses = []

    @property
    def ui(self):
        return f"""
Word: {self.known_letters}
Misses ({len(self.misses)}/{self.max_misses}): {', '.join(self.misses)}
"""

    def check_letter(self, letter):
        if letter in self.word:
            known_letters_list = [
                letter if letter == l1 else l2
                for l1, l2 in zip(self.word, self.known_letters)
            ]
            self.known_letters = ''.join(known_letters_list)
        else:
            self.misses.append(letter)
        return self.known_letters

    def check_word(self, word):
        if self.word == word:
            self.known_letters = word
        else:
            self.misses.append(word)

    def check_guess(self):
        if self.guess in self.misses:
            print(f'Already tried {self.guess}')
        else:
            if len(self.guess) == 1:
                self.check_letter(self.guess)
            else:
                self.check_word(self.guess)

    def play(self):
        print('Starting Hangman')
        print(f'The word has {len(self.word)} letters: {self.known_letters}')
        while len(self.misses) < self.max_misses:
            self.guess = str(input('Next guess?')).lower()
            self.check_guess()
            print(self.ui)

        if self.known_letters == self.word:
            print('Well Done!')
        else:
            print(f'Bad luck, the word was: {self.word}')


def main():
    game = Game(random.choice(words))
    game.play()


if __name__ == '__main__':
    main()
