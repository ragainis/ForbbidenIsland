from random import shuffle

class FloodCard(object):
	pass

class FloodDeck(object):
	pass #has FloodCard

class IslandTiles(object):
    def __init__(self, name, type, status):
        self.name = name
        self.type = type
        self.status = status
    
    def set_status(self,status):
        self.status = status
    
class Map(object):
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

class TreasureCard(object):
	pass

class TreasureDeck(object):
	pass #has TreasureCard

class Adventurers(object):
	pass

class Engine(object):
 #has Map, FloodDeck, TreasureDeck, Adventurers, Water Level
#	map = Map()
#	flood_deck = FloodDeck()
#	treasure_deck = TreasureDeck()
#	adventurers = Adventurers()
#	water_level = WaterLevel()
    pass







map = Map()
map.create_map()
list = map.get_full_map()
print list