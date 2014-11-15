class WordChecker:
    def contains(self, letter, word):
        return letter in word

    def words_contains(self, letter, *words):
        return [self.contains(letter, x) for x in words]
