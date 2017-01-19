import unittest
import ForbidIsland_SSD as fb

class TestInputTypes(unittest.TestCase):
    def test_maptiles_list(self):
        self.assertEqual(type(fb.map_tiles),list, 'Map Tiles should be list but it is %s' % type(fb.map_tiles))

    def test_treasurecards_list(self):        
        self.assertEqual(type(fb.treasure_cards),list, 'Treasure Cards should be list but it is %s' % type(fb.treasure_cards))

    def test_adventurers_list(self):
        self.assertEqual(type(fb.adventurers),dict, 'Adventurer should be dictionary but it is %s' % type(fb.adventurers))

if __name__ == '__main__':
    unittest.main()