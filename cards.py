#!/usr/bin/env python3

class Card(object):
  def __init__(self, number:int, suit:str):
    self.number = number
    self.suit = suit

  def __str__(self) -> str:
    return 'C<{},{}>'.format(self.number,self.suit)

  def __repr__(self) -> str:
    return str(self)
  
  def __gt__(self, other) -> bool:
    return self.number > other.number

  def __lt__(self, other) -> bool:
    return self.number < other.number




class Hand(object):
  """docstring for Hands"""
  def __init__(self, cards:[Card]):
    self.cards = sorted(cards)
    self.assignRank()

  def __str__(self) -> str:
    return str(self.cards)

  def __repr__(self) -> str:
    return str(self)
  

  def assignRank(self):
    if self.isStraight() and self.isFlush():
      self.rank = 1
    elif self.is4ofaKind():
      self.rank = 2
    elif self.isFullHouse():
      self.rank = 3
    elif self.isFlush():
      self.rank = 4
    elif self.isStraight():
      self.rank = 5
    elif self.isTriple():
      self.rank = 6
    elif self.istwoPairs():
      self.rank = 7
    elif self.isPair():
      self.rank = 8
    else:
      self.rank = 9


  def isFlush(self) -> bool:
    suit = self.cards[0].suit
    for i in range(5):
      if self.cards[i].suit != suit:
        return False
    return True

  def isStraight(self) -> bool:
    for i in range(4):
      if (self.cards[i].number+1) != self.cards[(i+1)].number:
        return False
    return True

  def is4ofaKind(self)-> bool:
    if self.cards[0].number == self.cards[3].number or self.cards[1].number == self.cards[4].number:
      return True
    return False

  def isFullHouse(self)->bool:
    s = len(set(self.cards[i].number for i in range(5)))
    if s ==2 and self.is4ofaKind() == False:
      return True
    return False

  def isTriple(self) -> bool:
    if self.cards[0].number == self.cards[2].number or self.cards[1].number == self.cards[3].number or self.cards[2].number == self.cards[4].number:
      return True
    return False

  def istwoPairs(self)->bool:
    s = len(set(self.cards[i].number for i in range(5)))
    if s ==3 and self.isTriple() == False:
      return True
    return False

  def isPair(self)->bool:
    s = len(set(self.cards[i].number for i in range(5)))
    if s ==4:
      return True
    return False   

def compare(hand1, hand2):
  if hand1.assignRank() > hand2.assignRank():
    return 'hand1 win!'
  elif hand1.assignRank() < hand2.assignRank():
    return 'hand2 win!'
  
y = Card(3,'H')
z = Card(4,'S')
print(y>z)

#print(a)

h =Hand([Card(3,'H'), Card(4,'H'), Card(5,'H'), Card(8,'S') ,Card(9,'D')]) 
print(h.isStraight())
print(h.isFlush())

a =Hand([Card(3,'H'), Card(4,'H'), Card(5,'H'), Card(6,'S') ,Card(7,'D')]) 
print(a.isStraight())
print(a.isFlush())

b =Hand([Card(3,'H'), Card(4,'H'), Card(5,'H'), Card(6,'H') ,Card(7,'H')])
print(b.isStraight())
print(b.isFlush())

c =Hand([Card(3,'H'), Card(3,'H'), Card(5,'H'), Card(6,'S') ,Card(7,'D')])
print(c.isStraight())
print(c.isFlush())
print(c.is4ofaKind())
print(c.isFullHouse())

d =Hand([Card(3,'H'), Card(3,'H'), Card(7,'H'), Card(3,'S') ,Card(3,'D')])
print(d.is4ofaKind())

e =Hand([Card(3,'H'), Card(3,'H'), Card(2,'H'), Card(3,'S') ,Card(3,'D')])
print(e.is4ofaKind())
print(e.isFullHouse())

f =Hand([Card(3,'H'), Card(3,'H'), Card(2,'H'), Card(2,'S') ,Card(2,'D')])
print(f.isFullHouse())



#high card
#pair
#two pairs  
#triple
#straight 5 in a row
#flush 5 the same suit
#full house (triple and a pair)
#4 of a kind 
#a straight flush

