import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        node = LeafNode("p", "testing is a pain")
        expected_result = '<p>testing is a pain</p>'
        self.assertEqual(node.to_html(), expected_result)
    
    def test_leaf2(self):
       node = LeafNode(None, "Hello, world!")
       self.assertEqual(node.to_html(), "Hello, world!")

class TestParentNode(unittest.TestCase):
    def test_no_children_raises_error(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("p", None, {'class': 'test'})
            node.to_html()

    def test_no_tag_error(self):
        children = [LeafNode("b", "Bold text"),
                    LeafNode("p", "Paragraph text")]
        with self.assertRaises(ValueError) as context:
            node = ParentNode(None, children, {'class': 'test'})
            node.to_html()

    def test_recursion(self):
        children = [LeafNode("i", "italic text")]
        children_node = ParentNode("span", children)
        outer_children = [
            LeafNode("b", "Bold text"),
            children_node,
            LeafNode(None, "Normal text")]
        outer_children_node = ParentNode("div", outer_children)
        expected_html = "<div><b>Bold text</b><span><i>italic text</i></span>Normal text</div>"
        self.assertEqual(outer_children_node.to_html(), expected_html)
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
        

if __name__ == "__main__":
    unittest.main()
