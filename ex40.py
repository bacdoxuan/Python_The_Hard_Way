print("Importing ex40_mystuff:...")
import ex40_mystuff
print("Done!")

import time

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            time.sleep(1)


if __name__ == '__main__':
    ex40_mystuff.apple()
    print(ex40_mystuff.tangerine)
    happy_bday = Song(["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])
    bulls_on_parade = Song(["They rally around the family",
    "With pockets full of shells"])
    happy_bday.sing_me_a_song()
    bulls_on_parade.sing_me_a_song()
