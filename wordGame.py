import re

class Game:
    def __init__(self):
        self.words_used = []
        self.score= 0

    def checked_word(self, word):  # 입력 단어 조건 확인
        # 입력한 단어가 한글로 이루어 졌는지 확인
        if not re.match("^[ㄱ-ㅎㅏ-ㅣ가-힣]+$", word):
            return False
        # 입력 단어에 공백 확인
        if ' ' in word:
            return False
        # 입력 단어의 길이 확인
        if 2 < len(word) < 10:
            return False
        # 입력 단어가 이전 단어 목록에 있는지 확인
        if word in self.words_used:
            return False

        return True

    def play_game(self):    # 단어 입력 및 조건에 부합하지 않은 단어일 경우 재입력 메세지 출력

        while True:
            print("현재 점수:", self.score)
            word = input("단어 입력:").strip()

            if not self.checked_word(word):
                print("다른 단어를 입력하세요.")
                self.score -= 1
                continue

            if self.words_used and self.words_used[-1][-1] != word[0]:
                print("규칙에 어긋나는 단어에요, 다른 단어를 입력하세요.")
                self.score -= 1
                continue

            self.words_used.append(word)
            self.score += len(word)

if __name__ == "__main__":
    game = Game()
    game.play_game()
