import re
from textnode import *
from htmlnode import ParentNode
from inline_markdown import *

def markdown_to_blocks(markdown):
    block = []
    lines = markdown.split("\n\n")
    for line in lines:
            if line == "":
                continue
            strip_whitespace = line.strip()
            block.append(strip_whitespace)
    return block

def block_to_block_type(block):
     lines = block.splitlines()
     if lines:
          match= re.match(r"^#{1,6} ", lines[0])
          if match:
               return "heading"
     if block.startswith("```") and block.endswith("```"):
          return "code"
     is_quote = all(line.startswith(">") for line in lines)
     if is_quote:
          return "quote"
     is_unordered_list = all(line.startswith("* ") or line.startswith("- ") for line in lines)
     if is_unordered_list:
          return "unordered list"
     ordered_list = True
     for i , line in enumerate(lines, start=1):
          if not line.startswith(f"{i}. "):
               ordered_list = False
               break
     if ordered_list:
          return "ordered list"
     else:
          return "paragraph"

def markdown_to_html_node(markdown):
     blocks = markdown_to_blocks(markdown)
     children = []
     for block in blocks:
          block_type = block_to_block_type(block)
          if block_type == "heading":
               child = heading_block(block)
               children.append(child)
          elif block_type == "quote":
               child = quote_block(block)
               children.append(child)
          elif block_type == "code":
               child = code_block(block)
               children.append(child)
          elif block_type == "unordered list":
               child = unordered_list_block(block)
               children.append(child)
          elif block_type == "ordered list":
               child = ordered_list_block(block)
               children.append(child)
          elif block_type == "paragraph":
               child = paragraph_block(block)
               children.append(child)
     return ParentNode(tag = "div", children = children)

def text_to_children(text):
     textnodes = text_to_textnodes(text)
     result = []
     for textnode in textnodes:
          good_text = text_node_to_html_node(textnode)
          result.append(good_text)
     return result

def heading_block(block):
     count = 0
     for char in block:
          if char == "#":
               count += 1
          else:
               break
     if count + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {count}")
     no_heading = block[count:].strip()
     inline_handled = text_to_children(no_heading)
     return ParentNode(tag = f"h{count}", children = inline_handled)

def quote_block(block):
     lines = block.split("\n")
     new_lines = []
     for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
     content = " ".join(new_lines)
     inline_handled = text_to_children(content)
     return ParentNode(tag = "blockquote", children = inline_handled)

def code_block(block):
      no_markdown = block.strip("```")
      inline_handled = text_to_children(no_markdown)
      code_node = ParentNode(tag = "code", children = inline_handled)
      return ParentNode(tag = "pre", children = code_node)

def unordered_list_block(block):
     items = block.split("\n")
     list_items = []
     for item in items:
           cleaned_item = item.lstrip("* -").strip()
           item_nodes = text_to_children(cleaned_item)
           li_node = ParentNode(tag = "li", children = item_nodes)
           list_items.append(li_node)
     return ParentNode(tag = "ul", children = list_items) 

def ordered_list_block(block):
     items = block.split("\n")
     list_items = []
     for item in items:
           cleaned_item = item[3:]
           item_nodes = text_to_children(cleaned_item)
           li_node = ParentNode(tag = "li", children = item_nodes)
           list_items.append(li_node)
     return ParentNode(tag = "ol", children = list_items)

def paragraph_block(block):
      lines = block.split("\n")
      paragraph = " ".join(lines)
      inline_handled = text_to_children(paragraph)
      return ParentNode(tag = "p", children = inline_handled)

