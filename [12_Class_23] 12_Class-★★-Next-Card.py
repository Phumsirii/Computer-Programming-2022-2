class Card:
    def __init__(self, value, suit):
        self.value=str(value)
        self.suit=suit
 
    def __str__(self):
        return '('+self.value+' '+self.suit+')'
 
    def next1(self):
        a=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        b=['club','diamond','heart','spade']
        c=a.index(self.value)
        d=(b.index(self.suit)+1)%len(b)
        if d==0:
            c=(c+1)%len(a)
        return Card(a[c],b[d])

    def next2(self):
        a=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        b=['club','diamond','heart','spade']
        c=a.index(self.value)
        d=(b.index(self.suit)+1)%len(b)
        if d==0:
            c=(c+1)%len(a)
        self.value=a[c]
        self.suit=b[d]

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
