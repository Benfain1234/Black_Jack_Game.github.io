#!/usr/bin/env python
# coding: utf-8

# In[16]:


import random
suits = ('Hearts','Diamonds','spades','clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values= {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
game_on =True


# In[17]:


class card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
       
    def __str__(self):
        return self.rank+ " of "+ self.suit


# In[18]:


class deck:
    
    def __init__(self):
        
        self.all_cards=[]
        
        for suit in suits:
            for rank in ranks:
                created_card= card(suit,rank)
                
                self.all_cards.append(created_card)
     
    
     
    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return "the deck has:"+ deck_comp   
    
    
    def shuffle(self):
           random.shuffle(self.all_cards)
            
            

    def deal(self):
        card=self.all_cards.pop()
        return card
        
    def addcard(self,card):
        self.all_cards.append(card)
        

    


# In[19]:


class hand:
    def __init__(self):
        self.cards= []
        self.value= 0
        self.aces = 0
        
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces+=1
            
    def adjust_for_ace(self):
        while self.value >21 and self.aces:
            self.value -= 10
            self.aces -= 1
    def remove(self):
        self.value-= values[self.cards[-1].rank]
        return(self.cards.pop())

# In[20]:


class chips:
    def __init__(self,total=100):
        self.total = total
        self.bet= 0
        
    def win_bet(self):
        self.total+=self.bet
        
    def lose_bet(self):
        self.total-=self.bet
     
   


# In[21]:


def take_bet(chips):
       
       while True:
           
           try:
               chips.bet = int(input("how many chips would u like to bet "))
               
           except:
               print("sorry please provide a number")
           else:
               if chips.bet>chips.total:
                   print("sorry you dont have enough chips! you have: {}".format(chips.total))
               else:
                   break
               


# In[22]:


def hit(deck,hand):
    single_card =deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# In[23]:


def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Hit or Stand? enter h or s")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print("player stands dealer's turn")
            playing= False
            
        else:
            print("sorry, i did no understand please enter h or s")
            continue
        break    


# In[24]:


def show_some(player,dealer):
    print("\n dealer's hand:")
    print("first card hidden!")
    print(dealer.cards[1])
    
    
    print("\n player's hand:")
    for card in player.cards:
        print(card)
    
    
    
    
    
def show_all(player,dealer):
    
    print("\n dealer's hand:")
    for card in dealer.cards:
        print(card)
    
    print(f"value of dealer's hand is {dealer.value}")
    
    print("\n player's hand:")
    for card in player.cards:
        print(card)
    
    print(f"value of player's hand is {player.value}")


# In[25]:


def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("Player Wins! Dealer Bust")
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("Player Bust! Dealer Wins!")
    
def push(player,dealer):
    print("Tie")

    


# In[26]:
deck = deck()

while True:
    
    print("WELCOME TO BLACKJACK")
    
    
    deck.shuffle()
    
    player_hand = hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips = chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    playing=True
    while playing:
        
        
        hit_or_stand(deck,player_hand)
        
        show_some(player_hand,dealer_hand)
        
        if player_hand.value >21:
            player_busts(player_hand,dealer_hand,player_chips)
            
            break
     
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
            
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand,dealer_hand)
            
            
    print(f"Player total chips: {player_chips.total}") 
    
    new_game = input("would u like to play another hand? y/n")
    
    if new_game[0].lower() == 'y':
        playing = True
        while player_hand.value>0:
            deck.addcard(player_hand.remove())
        while dealer_hand.value>0:
            deck.addcard(dealer_hand.remove())

        continue
        
    else:
        print("thank u for playing")
        
        break
            


# In[ ]:




