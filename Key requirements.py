
Cards
	
	class TreasureCards
		def __init__(object):
			self.counts = {
					'EarthStone': 5,
					'StatueOfWind': 5,
					'CrystalOfFire': 5,
					'OceanChalice': 5,
					'HelicopterLift': 3,
					'SandBags': 2
					}
			
			self.create_card(self, name):
			
			
			self.create_deck(self):
				self.deck = []
				
				for t, c in self.iteritems():
					for i in range(0, c):
						self.deck.append()
	
	class FloodCards (object):

		def __init__(object):
			
			self.status = ('Active','Flooded','Drowned')
			self.type = ('Generic', 'StatueOfWind', 'CrystalOfFire', 'OceanChalice', 'EarthStone', 
						'GreyStart', 'BlackStart', 'YellowStart', 'RedStart', 'GreenStart', 'BlueStart')
			self.tiles =
						{
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
	MapCards
		Name
		HasArtifact
		StartTiles:
			Red - Bronze Gate
			Green - Copper Gate
			Grey - Silver Gate
			Blue - Fool's Landing
			Yellow - Gold Gate
			Black - Iron Gate
		CardState:
			IsActive
			IsFlooded
			IsDrowned
		IsHomeBase
		
	Adventurers
		Type:
			Explorer - move diagonally + shore up diagonally. Starting tile - 
			Pilot - move to any tile once per turn for 1 action
			Navigator - move another player up to 2 tiles per 1 action
			Diver - move through one or more adjacent missing and/or flooded tiles for 1 action
			Engineer - shore up to 2 tiles per action
			Messenger - give card not on same tile
		Actions:
			Move - 1 move per action NESW only to adjacent tile (exceptions apply Explorer, Pilot, Navigator, Diver)
			Shore up - flip flooded tile to unflooded. NESW plus active tile (exceptions Engineer, Explorer)
			Give Card - give card to player on same tile 1 per action (exception Messenger CANNOT GIVE SPECIAL CARDS)
			Capture a Treasure - use 1 action to claim treasure for set of 4 TreasureCards. Must be on matching Treasure Island Tile. Discard treasure cards.
	
	Turn sequence:
		1. Setup tiles. Shuffle Island tiles. Setup map. First 4x4 then 2 tiles per side in the middle. Initialize IslandTileDiscard = empty.
		2. Shuffle FloodCards. Draw first 6 cards and flip to Flooded. Initialize FloodedDiscardPile. Move initial 6 cards to FloodedDiscardPile.
		3. Shuffle Adventurers. Deal players as defined by starting conditions 2 - 4 players possible. Randomly initialize X players with unique types. Place them on respective starting tiles.
		4. Shuffle TreasureCards. Deal 2 cards to each player. If WaterRise card
			
			
Engine
	Loss conditions (all on FloodTiles draw)
		Player drowns
		Home base drowns
		Sea level too high
		
	Win conditions (only when player triggers claim artifact)
		Last artifact claimed, other artifacts collected AND all adventureres are on home base
	
Player
	Key attributes:
		Move limit
		Hand limit
		Share distance/availability
		Special moves
			Fly
			Dive
			
	Current Hand
		Take cards
		Discard cards
		
	Actions
		Move
		Shore up
		Share cards

Hand
	Limit
	Take cards
	Remove cards
	
	
+++++++++++++++++++++++++++++++++++++++++
Howling Garden (StatueOfWind),
			Observatory,
			Silver Gate (Grey Start),
			Iron Gate (Black Start),
			Phantom Rock,
			Temple of Sun (EarthStone),
			Watchtower,
			Coral Palace (OceanChalice),
			Whispering Garden (StatueOfWind),
			Crimson Forest,
			Fool's Landing (Blue start, home tile),
			Dunes of Deception,
			Gold gate (Yellow start),
			Copper gate (Green start),
			Lost Lagoon,
			Cave of Shadows (CrystalOfFire),
			Tidal Palace (OceanChalice),
			Misty Marsh,
			Twilight Hollow,
			Temple of the Moon (EarthStone),
			Cave of Embers (CrystalOfFire),
			Bronze Gate (Red Start)
			Breakers Bridge,
			Cliffs of Abandon
			
