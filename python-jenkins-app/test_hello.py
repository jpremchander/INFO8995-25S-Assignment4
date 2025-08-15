import unittest
from hello import hello_world, add_numbers

class TestHello(unittest.TestCase):
    
    def test_hello_world(self):
        """Test the hello_world function."""
        result = hello_world()
        self.assertEqual(result, "Hello, World from Jenkins CI/CD!")
    
    def test_add_numbers(self):
        """Test the add_numbers function."""
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)
    
    def test_add_numbers_negative(self):
        """Test add_numbers with negative numbers."""
        result = add_numbers(-2, 5)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
