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
    def __init__(self, word: str):
        self.word = word
        self.known_letters = '_'*len(self.word)

    def check_letter(self, letter: str) -> str:
        known_letters_list = [
            letter if letter == l1 else l2
            for l1, l2 in zip(self.word, self.known_letters)
        ]
        self.known_letters = ''.join(known_letters_list)
        return self.known_letters

    def play(self):
        print('Starting Hangman')
        print(f'The word has {len(self.word)} letters: {self.known_letters}')
        while self.word != self.known_letters:
            letter = input('Next letter?')
            print(self.check_letter(letter))
        print('Well Done')


def main():
    game = Game(random.choice(words))
    game.play()


if __name__ == '__main__':
    main()
