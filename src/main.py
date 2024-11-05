from textnode import *

def main():
   node = TextNode(text = "this is a test",
                   text_type = TextType.ITALIC,
                   url = "https://www.boot.dev")
   print(node)


if __name__ == "__main__":
    main()