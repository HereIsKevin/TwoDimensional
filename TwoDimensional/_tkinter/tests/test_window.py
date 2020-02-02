import unittest
from ..window import Window


class TestWindow(unittest.TestCase):
    def test_name(self):
        window = Window()

        self.assertEqual(window.name(), "window")
        window.name("new window")
        self.assertEqual(window.name(), "new window")

    def test_dimensions(self):
        window = Window()

        self.assertEqual(window.dimensions(), (500, 500))
        window.dimensions((750, 750))
        self.assertEqual(window.dimensions(), (750, 750))

    def test_location(self):
        window = Window()

        self.assertEqual(window.location(), (50, 50))
        window.location((100, 100))
        self.assertEqual(window.location(), (100, 100))

    def test_resizable(self):
        window = Window()

        self.assertEqual(window.resizable(), True)
        window.resizable(False)
        self.assertEqual(window.resizable(), False)

    def test_show(self):
        window = Window()

        self.assertEqual(window.state(), "shown")
        window.hide()
        self.assertEqual(window.state(), "hidden")
        window.show()
        self.assertEqual(window.state(), "shown")
