from random import randint
from random import shuffle

treasure_cards = ['Treasure One', 'Treasure One', 'Treasure One', 'Treasure One', 'Treasure One',
					'Treasure Two', 'Treasure Two', 'Treasure Two', 'Treasure Two', 'Treasure Two',
					'Treasure Three', 'Treasure Three', 'Treasure Three', 'Treasure Three', 'Treasure Three',
					'Treasure Four', 'Treasure Four', 'Treasure Four', 'Treasure Four', 'Treasure Four',
					'Helicopter Lift', 'Helicopter Lift', 'Helicopter Lift', 'Helicopter Lift', 
					'Sand Bag', 'Sand Bag', 'Sand Bag']

map_tiles = ['Observatory', 'Crimson Forest', 'Phantom Rock', 'Dunes of Deception', 'Lost Lagoon',
			'Misty Marsh', 'Twilight Hollow', 'Watchtower', 'Breakers Bridge', 'Cliffs of Abandon', 
			'Whispering Garden', 'Howling Garden', 'Cave of Embers', 'Cave of Shadows', 'Coral Palace',
			'Tidal Palace', 'Temple of Sun', 'Temple of the Moon', 'Silver Gate', 'Iron Gate', 
			'Gold Gate', 'Bronze Gate', 'Copper Gate', 'Fools Landing']

adventurers = {	'Diver': 'Iron Gate', 
				'Pilot': 'Fools Landing', 
				'Explorer': 'Copper Gate', 
				'Messenger': 'Silver Gate', 
				'Navigator': 'Gold Gate', 
				'Engineer': 'Bronze Gate'}

class Adventurer(object):
	"""
	On initialization Adventurer uses name as key to lookup starting position in dictionary.
	Arguments:
		name - string
	Methods: 
		__init__(name) - sets name and position. Start position is retrieved from adventurers dictionary.
	    get_name() - returns name as string
	    get_position() - returns position as string
	"""
	def __init__(self, name):
		self.name = name
		self.position = adventurers[name]
	
	def get_name(self):
		return self.name
		
	def get_position(self):
		return self.position
		
	
class Card(object):
	"""Card expects name as a string.
	Arguments:
		name - string
	Method:
	   __init__ - sets name
	   get_name() - returns name as string
	"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)
	
	def get_name(self):
	    return self.name

class MapTile(Card):
    """MapTile expects name as string.
	Arguments:
		name - string
    Methods:
        __init__ - uses Card class to set name, defaults status to 'Active'
		set_tile_status(type='Flooded'):
            - takes type as string. 
            - available types: 'Active', 'Flooded', 'Drowned'
            - sets status to tile
            - returns updated status as string
        get_tile_status() - returns status as string
        get_tile_name() - returns tile name as string"""
    
    def __init__(self, name):
		Card.__init__(self, name)
		self.status = 'Active'
		
    def set_tile_status(self, type = 'Flooded'):
		
		if type == 'Active':
			self.status = 'Active'
		
		elif type == 'Flooded':
			self.status = 'Flooded'
		
		elif type == 'Drowned':
			self.status = 'Drowned'
		
		return get_tile_status()
	
    def get_tile_status(self):
		return self.status
		
    def get_tile_name(self):
		return self.name
		
class Deck(object):
	"""
	Arguments:
		list - list of names as strings
	Methods:
	    __init__ - uses list of names to create Card instances and append to main list. 
					This will also initializes empty 'discard' and 'removed' lists.
		shuffle_deck(deck = 'main'):
			- shuffles list of cards. By default shuffles 'main'. Pass 'discard' to shuffle discard.
	    take_card_from_main():
	        - pops card from main list
	    add_discarded_to_main():
	        - shuffles Deck.discard list 
	        - extends Deck.main with Deck.discard
	        - sets Deck.discard to empty list
	    add_card_to_disard(card):
	        - expects Card instance
	        - appends card to Deck.discard
	    add_card_to_removed(card):
	        - expects Card instance
	        - appends card to Deck.removed 
	"""

	def __init__(self, list):
		self.main = []
		self.discard = []
		self.removed = []
	
	# creates initial main of cards based on passed list 
		for card in list:
			self.main.append(Card(card))	
		
		self.shuffle_deck()
		
	def __str__(self):
		self.cards = []
		for card in self.main:
			self.cards.append(str(card.name)) 
		
		return '\n '.join(self.cards)
			
	def shuffle_deck(self, deck = 'main'):
	# shuffles list of cards
	
		if deck == 'main':
			shuffle(self.main)
			
		elif deck == 'discard':
			shuffle(self.discard)
		
		else:
			print "Invalid value. Only 'main' and 'discard' values are supported."
	
	def take_card_from_main(self):
		return self.main.pop()
	
	def add_discarded_to_main(self):
		
		self.shuffle_deck('discard')
		self.main.extend(self.discard)
		self.discard = []
	
	def add_card_to_discard(self, card):
		self.discard.append(card)

	def add_card_to_removed(self, card):
		self.removed.append(card)

class Map(Deck):
	"""
	Arguments:
	
	Method:
		__init__ - takes list of names. Creates MapTile instances and append to main deck.
				This also initializes empty list for 'discard' and 'removed' decks.
		
	"""

    def __init__(self, list):
		self.main = []
		self.discard = []
		self.removed = []
	
	# creates initial main of cards based on passed list 
		for card in list:
			self.main.append(MapTile(card))	
		
		self.shuffle_deck()


		
def pick_adventurers(number):
	
	result = []
	for x in range(0, number):
		random_adventurer = adventurers.keys()[randint(0,len(adventurers)-1)]
		while random_adventurer in result:
			random_adventurer = adventurers.keys()[randint(0,len(adventurers)-1)]
		result.append(random_adventurer)
	return result


def flood_phase(number):
	for x in range(0, number):
		current_flood_card = fdeck.take_card_from_main()
		map_index = 0
		for x in range(len(mdeck.main)):
			if mdeck.main[x].name == current_flood_card.name:
				map_index = x
		current_map_card = mdeck.main[map_index]
		current_map_status = current_map_card.get_tile_status()		
		
		if current_map_status == 'Active':
			current_map_card.set_tile_status('Flooded')
			fdeck.add_card_to_discard(current_flood_card)
		
		elif current_map_status == 'Flooded':
			current_map_card.set_tile_status('Drowned')
			fdeck.add_card_to_removed(current_flood_card)
			#DO I NEED TO IMPLEMENT REMOVE CARD FROM MAP METHOD?

#Initial sequence for debugging and testing
tdeck = Deck(treasure_cards)
tdeck.shuffle_deck()
fdeck = Deck(map_tiles)
fdeck.shuffle_deck()
mdeck = Map(map_tiles)
mdeck.shuffle_deck()
players = pick_adventurers(2)
flood_phase(10)
fdeck.add_discarded_to_main()
print fdeck
print mdeck




