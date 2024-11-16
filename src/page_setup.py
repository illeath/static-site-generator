import os
from pathlib import Path
from blocks import markdown_to_html_node

def extract_title(markdown):
    if markdown.startswith("#"):
        if markdown[1] == "#":
            raise Exception("not a h1 header")
        else:
            no_header = markdown.lstrip("# ").rstrip()
            return no_header
    else:
        raise Exception("no header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown_content = file.read()
    with open(template_path) as file:
        template_content = file.read()
    title = extract_title(markdown_content)
    html_node = markdown_to_html_node(markdown_content)
    html_string = html_node.to_html()
    replaced_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    with open(dest_path, "w") as file:
        file.write(replaced_content)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                transformed_file = Path(filename).with_suffix(".html")
                dest_path = os.path.join(dest_dir_path, transformed_file)
                generate_page(from_path, template_path, dest_path)
        else:
            new_dest_path = os.path.join(dest_dir_path, filename)
            generate_pages_recursive(from_path, template_path, new_dest_path)