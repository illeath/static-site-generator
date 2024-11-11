import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links

class RegexTest(unittest.TestCase):
    def test_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(result, expected)
    
    def test_multi_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(result, expected)
    
    def test_link(self):
        text = "here's a random [youtube link](https://www.youtube.com/watch?v=RZaWlNOj1oM)"
        result = extract_markdown_links(text)
        expected = [("youtube link", "https://www.youtube.com/watch?v=RZaWlNOj1oM")]
        self.assertEqual(result, expected)
    
    def test_multi_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()