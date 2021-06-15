class UnoCard():
    def __init__(self,c,n):
        self.c=c
        self.n=n
    def canPlay(self,other):
        if(self.c==other.c or self.n==other.n):
            return True
        else:
            return False
#green=0,yellow=1,blue=2,red=3
card1=UnoCard(0,3)
card2=UnoCard(1,6)
class CollectionOfUnoCards():
    def __init__(self):
        self.deck=[]
        for color in["Green","Red","Blue","Yellow"]:
            for i in range(2):
                for n in range(1,10):
                    self.deck.append(UnoCard(n,color))
    def canPlay(self,):
        return str(self.c)+""+str(self.n)
    def addCard (self,card):
        self.cardlist.append(card)
    def __str__(self):
        return "An uno deck with"+str(len(self.deck))+"cards remaining"
        return couc_str
    def makeDeck(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        strs = ["Yellow", "Blue", "Red", "Green"]
        topdeck = nums + strs
        print(topdeck)
        return topdeck
    def getTopCard(self):
        return self.deck.pop()
import itertools, random
topdeck=list(itertools.product(range(1,10),['Green','Yellow','Red','Blue']))
deck1=list(itertools.product(range(1,10),['Green','Yellow','Red','Blue']))
deck2=list(itertools.product(range(1,10),['Green','Yellow','Red','Blue']))
random.shuffle(deck1)
deck=CollectionOfUnoCards()
print(deck)
print("Player 1 got:")
for i in range(7):
   print(deck1[i][0], "of", deck1[i][1])
import itertools, random
deck2 = list(itertools.product(range(1,10),['Red','Green','Yellow','Blue']))
random.shuffle(deck2)
print("Player 2 got:")
topdeck = list(itertools.product(range(1,10),['Red','Green','Yellow','Blue']))
for i in range(7):
   print(topdeck[i][0], "of", topdeck[i][1])
import itertools, random
random.shuffle(topdeck)
print("Top of the deck is:")
for i in range(1):
   print(topdeck[i][0], "of", topdeck[i][1])
strs = ["Yellow", "Blue", "Red", "Green"]
if (topdeck[i][1],topdeck[i][0] == deck1[i][0],deck1[1]):
    print("Player 1 can play")
    print("Player 1 played")
elif(topdeck[i][1],topdeck[i][0] != deck1[i][0],deck1[1]):
            print("Player 1 draws a card")
if (topdeck[i][0],topdeck[i][1] == deck2[i][1],deck2[i][0]):
    print("Player 2 can play")
    print("Player 2 played")
elif(topdeck[i][0],topdeck[i][1] != deck2[i][1],deck2[i][0]):
    print("Player 2 draws a card")
if (topdeck[i][1],topdeck[i][0] == deck1[i][0],deck1[1]):
    print("Player 1 can play")
    print("Player 1 played")
elif(topdeck[i][1],topdeck[i][0] != deck1[i][0],deck1[1]):
            print("Player 1 draws a card")
if (topdeck[i][0],topdeck[i][1] == deck2[i][1],deck2[i][0]):
    print("Player 2 can play")
    print("Player 2 played")
elif(topdeck[i][0],topdeck[i][1] != deck2[i][1],deck2[i][0]):
    print("Player 2 draws a card")
if (topdeck[i][1],topdeck[i][0] == deck1[i][0],deck1[1]):
    print("Player 1 can play")
    print("Player 1 played")
elif(topdeck[i][1],topdeck[i][0] != deck1[i][0],deck1[1]):
            print("Player 1 draws a card")
if (topdeck[i][0],topdeck[i][1] == deck2[i][1],deck2[i][0]):
    print("Player 2 can play")
    print("Player 2 played")
elif(topdeck[i][0],topdeck[i][1] != deck2[i][1],deck2[i][0]):
    print("Player 2 draws a card")
if (topdeck[i][1],topdeck[i][0] == deck1[i][0],deck1[1]):
    print("Player 1 can play")
    print("Player 1 played")
elif(topdeck[i][1],topdeck[i][0] != deck1[i][0],deck1[1]):
            print("Player 1 draws a card")
if (topdeck[i][0],topdeck[i][1] == deck2[i][1],deck2[i][0]):
    print("Player 2 can play")
    print("Player 2 played")
elif(topdeck[i][0],topdeck[i][1] != deck2[i][1],deck2[i][0]):
    print("Player 2 draws a card")
if (topdeck[i][1],topdeck[i][0] == deck1[i][0],deck1[1]):
    print("Player 1 can play")
    print("Player 1 played")
elif(topdeck[i][1],topdeck[i][0] != deck1[i][0],deck1[1]):
            print("Player 1 draws a card")
if (topdeck[i][0],topdeck[i][1] == deck2[i][1],deck2[i][0]):
    print("Player 2 can play")
    print("Player 2 played")
elif(topdeck[i][0],topdeck[i][1] != deck2[i][1],deck2[i][0]):
    print("Player 2 draws a card")
if (topdeck[i][1],topdeck[i][0] == deck1[i][0],deck1[1]):
    print("Player 1 can play")
    print("Player 1 played")
elif(topdeck[i][1],topdeck[i][0] != deck1[i][0],deck1[1]):
            print("Player 1 draws a card")
if (topdeck[i][0],topdeck[i][1] == deck2[i][1],deck2[i][0]):
    print("Player 2 can play")
    print("Player 2 played")
elif(topdeck[i][0],topdeck[i][1] != deck2[i][1],deck2[i][0]):
    print("Player 2 draws a card")
if (topdeck[i][1],topdeck[i][0] == deck1[i][0],deck1[1]):
    print("Player 1 can play")
    print("Player 1 played")
    print("Player 1 shouts uno!!!")
elif(topdeck[i][1],topdeck[i][0] != deck1[i][0],deck1[1]):
            print("Player 1 draws a card")
if (topdeck[i][0],topdeck[i][1] == deck2[i][1],deck2[i][0]):
    print("Player 2 can play")
    print("Player 2 played")
elif(topdeck[i][0],topdeck[i][1] != deck2[i][1],deck2[i][0]):
    print("Player 2 draws a card")
print("Player 1 wins")





