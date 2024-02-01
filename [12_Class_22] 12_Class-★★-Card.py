class Card:
    def __init__(self, value, suit):
        self.value=str(value)
        self.suit=suit
        
    def __str__(self):
        return '('+self.value+' '+str(self.suit)+')'

    def getScore(self):
        if self.value=='A':
            return 1
        if self.value=='K' or self.value=='J' or self.value=='Q':
            return 10
        return int(self.value)
 
    def sum(self, other):
        a=self.getScore()
        b=other.getScore()
        return (a+b)%10
 
    def __lt__(self, rhs):
        a=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        b=['club','diamond','heart','spade']
        return (a.index(self.value),b.index(self.suit))<(a.index(rhs.value),b.index(rhs.suit))

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])