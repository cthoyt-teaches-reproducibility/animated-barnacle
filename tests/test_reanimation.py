import unittest

from animated_barnacle import reanimate


class TestReanimation(unittest.TestCase):
    def test_reanimate(self):
        """Tests reanimation works as planned, with no unintended consequences, such as
        evil monster barnacles"""
        x = reanimate.Reanimator('Chet')

        self.assertFalse(x.alive)

        x.reanimate()
        self.assertTrue(x.alive)

    def test_rereanimate_failure(self):
        """Tests that reanimated objects can't be reanimated more"""
        x = reanimate.Reanimator('Chet')
        x.reanimate()

        with self.assertRaises(ValueError):
            x.reanimate()
