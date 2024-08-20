from django.test import TestCase

class SimpleTest(TestCase):
    def test_print_hello(self):
        print("Hello, Django Unit Test!")
        self.assertEqual(1, 1)  # A simple assertion that will always pass

    def test_print_goodbye(self):
        print("Goodbye, Django Unit Test!")
        self.assertTrue(True)  # Another assertion that will always pass
