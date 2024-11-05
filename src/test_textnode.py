import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
            node = TextNode("this is a test", TextType.NORMAL, "https://www.youtube.com/watch?v=zeKE0NHUtUw")
            node2 = TextNode("this is a test", TextType.NORMAL, "https://www.youtube.com/watch?v=zeKE0NHUtUw")
            self.assertEqual(node, node2)
    
    def test_eq3(self):
         node = ("this is another test", TextType.ITALIC, None)
         node2 = ("this is another test", TextType.ITALIC, None)
         self.assertEqual(node, node2)
    
    def test_eq4(self):
         node = ("this is another test", TextType.ITALIC, None)
         node2 = ("this is another test", TextType.BOLD, None)
         self.assertNotEqual(node, node2)
    
    def test_eq5(self):
         node = ("this is another test", TextType.ITALIC, None)
         node2 = ("this is test", TextType.ITALIC, None)
         self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()