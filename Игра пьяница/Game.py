from Player import Player
from Deck import Deck
class Game:
    def __init__(self,):
        name1 = input("Имя первого игрока:")
        name2 = input("Имя второго игрока:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        
    def wins(self, winner):
            w = "{} забирает карты".format(winner)
            print(w)   

    def draw(self, p1n, p1c, p2n, p2c):
            d = "{} кладет {}, а {} кладет {}".format(p1n, p1c, p2n, p2c)
            print(d)

    def play_game(self):
            cards = self.deck.cards
            print("Игра началась!!!")
            while len(cards)>=2:
                response = input ("Нажмите клавишу W для выхода:")
                if response == "W":
                    break
                p1c = self.deck.rm_card()
                p2c = self.deck.rm_card()
                p1n = self.p1.name
                p2n = self.p2.name
                self.draw(p1n,p1c,p2n,p2c)
                if p1c > p2c:
                    self.p1.win += 1
                    self.wins(self.p1.name)
                else: 
                    self.p2.win +=1
                    self.wins(self.p2.name)
            
            win = self.winner(self.p1,self.p2)
            print("Игра окончина. {} выиграл!".format(win))

    def winner(self, p1, p2):
            if p1.win > p2.win:
                return p1.name
            if p1.win < p2.win:
                return p2.name
            return "Ничья!"