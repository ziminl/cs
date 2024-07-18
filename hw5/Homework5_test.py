import unittest
from Homework5 import *

class TestGladiatorFightGame(unittest.TestCase):

    def setUp(self):
        self.pugio = Weapon("pugio", 2)
        self.spatha = Weapon("spatha", 10)
        self.fascina = Weapon("fascina", 12)
        self.cuirass = Armor("cuirass", 5)
        self.helmet = Armor("helmet", 2)
        self.spartacus = Gladiator("spartacus", self.spatha, self.cuirass, 1.5, 0.2)
        self.flamma = Gladiator("flamma", self.spatha, self.helmet, 1.6, 0.1)
        self.attilius = Gladiator("attilius", self.pugio, self.helmet, 1.1, 0.5)

    def test_weapon_initialization(self):
        self.assertEqual(self.pugio.name, "pugio")
        self.assertEqual(self.pugio.damage, 2)
        self.assertEqual(self.spatha.name, "spatha")
        self.assertEqual(self.spatha.damage, 10)

    def test_armor_initialization(self):
        self.assertEqual(self.cuirass.name, "cuirass")
        self.assertEqual(self.cuirass.defense, 5)
        self.assertEqual(self.helmet.name, "helmet")
        self.assertEqual(self.helmet.defense, 2)

    def test_gladiator_initialization(self):
        self.assertEqual(self.spartacus.name, "spartacus")
        self.assertEqual(self.spartacus.weapon, self.spatha)
        self.assertEqual(self.spartacus.armor, self.cuirass)
        self.assertEqual(self.spartacus.strength, 1.5)
        self.assertEqual(self.spartacus.luck, 0.2)
        self.assertEqual(self.spartacus.health, 100)

    def test_attack(self):
        # Check that the attack method is generating a positive value
        self.assertTrue(self.spartacus.attack() > 0)
        self.assertTrue(self.flamma.attack() > 0)

    def test_defend(self):
        # Check that the defend method reduces the health points
        initial_health = self.spartacus.health
        self.spartacus.defend(20)
        self.assertTrue(self.spartacus.health < initial_health)


if __name__ == '__main__':
    unittest.main()
