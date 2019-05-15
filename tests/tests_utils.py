import unittest

from tests import load_resource
from tibiawikisql.utils import *


class TestWikiApi(unittest.TestCase):
    def testCleanLinks(self):
        # Regular link
        self.assertEqual(clean_links("[[Holy Damage]]"), "Holy Damage")
        # Named link
        self.assertEqual(clean_links("[[Curse (Charm)|Curse]]"), "Curse")
        # Comments
        self.assertEqual(clean_links("Hello <!-- world -->"), "Hello")

    def testParseBoolean(self):
        self.assertEqual(parse_boolean("yes"), True)
        self.assertEqual(parse_boolean("no"), False)
        self.assertEqual(parse_boolean("--"), False)
        self.assertEqual(parse_boolean("--", True), True)
        self.assertEqual(parse_boolean("no", invert=True), True)

    def testParseFloat(self):
        self.assertEqual(parse_float("1.45"), 1.45)
        self.assertEqual(parse_float("?"), 0.0)
        self.assertEqual(parse_float("?", None), None)
        self.assertEqual(parse_float("2.55%"), 2.55)

    def testParseInteger(self):
        self.assertEqual(parse_integer("100 tibia coins"), 100)
        self.assertEqual(parse_integer("10056"), 10056)
        self.assertEqual(parse_integer("--"), 0)

    def testParseMinMax(self):
        self.assertEqual(parse_min_max("5-20"), (5, 20))
        self.assertEqual(parse_min_max("50"), (0, 50))

    def testParseSounds(self):
        sound_string = "{{Sound List|Sound 1|Sound 2|Sound 3}}"
        sounds = parse_sounds(sound_string)
        self.assertEqual(len(sounds), 3)

        self.assertFalse(parse_sounds("?"))

    def testParseLootStatistics(self):
        content = load_resource("content_loot_statistics.txt")
        kills, loot_statistics = parse_loot_statistics(content)
        self.assertEqual(kills, 33023)
        self.assertEqual(len(loot_statistics), 73)

        kills, loot_statistics = parse_loot_statistics("Something else")
        self.assertEqual(kills, 0)
        self.assertFalse(loot_statistics)

    def testClientLightToRgb(self):
        self.assertEqual(client_color_to_rgb(-1), 0)
        self.assertEqual(client_color_to_rgb(0), 0)
        self.assertEqual(client_color_to_rgb(3), 0x99)
        self.assertEqual(client_color_to_rgb(215), 0xffffff)
        self.assertEqual(client_color_to_rgb(216), 0)
