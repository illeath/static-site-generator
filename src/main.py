import os
import shutil
from page_setup import generate_pages_recursive
from copystaticimage import copy_files_recursive

dir_path_content = "./content"
dir_path_static = "./static"
dir_path_public = "./public"

def main():
   print("Deleting public directory...")
   if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

   print("Copying static files to public directory...")
   copy_files_recursive(dir_path_static, dir_path_public)

   print("generating a new page")
   generate_pages_recursive("./content", "./template.html", "./public")


if __name__ == "__main__":
    main()