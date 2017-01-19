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
	"""Adventurer takes name as string. 
	On initialization Adventurer uses name as key to lookup starting position in dictionary.
	Methods: 
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
	Method:
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
    Methods:
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
	"""Pass list of cards to initialize deck as list of Card instances.
	This will also initializes empty 'discard' and 'removed' lists.
	Methods:
	    shuffle_deck(deck = 'main')
	    take_card_from_main():
	        - 
	    add_discarded_to_main():
	        - shuffles Deck.discard list 
	        - extends Deck.deck with Deck.discard
	        - sets Deck.discard to empty list
	    add_card_to_disard(card):
	        - expects Card instance
	        - appends card to Deck.discard
	    add_card_to_removed(card):
	        - expects Card instance
	        - appends card to Deck.removed 
	"""

	def __init__(self, list):
		self.deck = []
		self.discard = []
		self.removed = []
	
	# creates initial deck of cards based on passed list 
		for card in list:
			self.deck.append(Card(card))	
		
		self.shuffle_deck()
		
	def __str__(self):
		self.cards = []
		for card in self.deck:
			self.cards.append(str(card.name)) 
		
		return '\n '.join(self.cards)
			
	def shuffle_deck(self, deck = 'main'):
	# shuffles list of cards
	
		if deck == 'main':
			shuffle(self.deck)
			
		elif deck == 'discard':
			shuffle(self.discard)
		
		else:
			print "Invalid value. Only 'main' and 'discard' values are supported."
	
	def take_card_from_main(self):
		return self.deck.pop()
	
	def add_discarded_to_main(self):
		
		self.shuffle_deck('discard')
		self.deck.extend(self.discard)
		self.discard = []
	
	def add_card_to_discard(self, card):
		self.discard.append(card)

	def add_card_to_removed(self, card):
		self.removed.append(card)

class Map(Deck):
    def __init__(self, list):
		self.deck = []
		self.discard = []
		self.removed = []
	
	# creates initial deck of cards based on passed list 
		for card in list:
			self.deck.append(MapTile(card))	
		
		self.shuffle_deck()
	
    def remove_card_from_map(self, card):
		pass
    
class Maps(object):
    #hold Island tiles
    def __init__(self):
        self.map = []
	self.status = ('Active','Flooded','Drowned')
	self.tiles = {
		'1': ["Observatory", 0],
		'2': ["Crimson Forest", 0],
		'3': ["Phantom Rock", 0],
		'4': ["Dunes of Deception", 0],
		'5': ["Lost Lagoon", 0],
		'6': ["Misty Marsh", 0],
		'7': ["Twilight Hollow", 0],
		'8': ["Watchtower", 0],
		'9': ["Breakers Bridge", 0],
		'10': ["Cliffs of Abandon", 0],
		'11': ["Whispering Garden", 1],
		'12': ["Howling Garden", 1],
		'13': ["Cave of Embers", 2],
		'14': ["Cave of Shadows", 2],
		'15': ["Coral Palace", 3],
		'16': ["Tidal Palace", 3],
		'17': ["Temple of Sun", 4],
		'18': ["Temple of the Moon", 4],
		'19': ["Silver Gate", 5],
		'20': ["Iron Gate", 6],
		'21': ["Gold Gate", 7],
		'22': ["Bronze Gate", 8],
		'23': ["Copper Gate", 9],
		'24': ["Fool's Landing", 10],
		}

    def create_map(self):
        #create IslandTile instances and assign them to random position (1 to 24)
        for i in range(0, 24):
            name = self.tiles[str(i+1)][0]
            type = self.tiles[str(i+1)][1]
            status = self.status[0]
            tile = IslandTiles(name, type, status)
            self.map.append(tile)
   	#randomly assign positions for the tiles and returns
        return shuffle(self.map)

    def get_map(self):
       # print list of cards 	
        map = [0 for x in range(0,24)]
        for i in range(0,24):
            map[i] = self.map[i].name
        return map

    def get_full_map(self):
       # print list of cards 	
        map = [0 for x in range(0,24)]
        for i in range(0,24):
            #map[i] = self.map[i].name + str(' - ') + str(self.map[i].type) + str(' - ') + str(self.map[i].status)
            map[i] = [self.map[i].name, self.map[i].type, self.map[i].status]
        return map

    def config_map(self):
        # assign positions to the map
        # TODO: How to store positions. List with lists for each line. May need empty tiles.
        self.position = []

    def update_status(self, position, status):
        # position should be in range 0,24 and status in 0,2
        self.map[position].set_status(self.status[status])
        print self.map[position].status


def pick_adventurers(number):
	
	result = []
	for x in range(0, number):
		random_adventurer = adventurers.keys()[randint(0,len(adventurers)-1)]
		while random_adventurer in result:
			random_adventurer = adventurers.keys()[randint(0,len(adventurers)-1)]
		result.append(random_adventurer)
	return result

		
tdeck = Deck(treasure_cards)
fdeck = Deck(map_tiles)
mdeck = Map(map_tiles)
players = pick_adventurers(2)


def flood_phase(number):
	for x in range(0, number):
		current_flood_card = fdeck.take_card_from_main()
		map_index = 0
		for x in range(len(mdeck.deck)):
			if mdeck.deck[x].name == current_flood_card.name:
				map_index = x
		current_map_card = mdeck.deck[map_index]
		current_map_status = current_map_card.get_tile_status()		
		
		if current_map_status == 'Active':
			current_map_card.set_tile_status('Flooded')
			fdeck.add_card_to_discard(current_flood_card)
		
		elif current_map_status == 'Flooded':
			current_map_card.set_tile_status('Drowned')
			fdeck.add_card_to_removed(current_flood_card)
			#DO I NEED TO IMPLEMENT REMOVE CARD FROM MAP METHOD?





