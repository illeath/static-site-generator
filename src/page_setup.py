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