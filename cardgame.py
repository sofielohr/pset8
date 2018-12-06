class Card(object):
  def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"{self.value} of {self.suit}"
        
if __name__ = "__main__":
    var1 = Card(spades, ace)
    print(var1)
