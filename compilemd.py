# This file goes through the md files in postsmd and makes them in html in posts

import os
import markdown

# Set directories
posts_dir = 'posts'
posts_md_dir = 'postsmd'

# Create output directory if it doesn't exist
if not os.path.exists(posts_md_dir):
    os.makedirs(posts_md_dir)

# Loop through files in the posts directory
for filename in os.listdir(posts_md_dir):
    print(f"Looking at file {filename}")
    if filename.endswith('.md') or filename.endswith(".markdown"):
        print("It's markdown...")
        # Read the markdown file
        markdown_path = os.path.join(posts_md_dir, filename)
        with open(markdown_path, 'r', encoding='utf-8') as file:
            md_content = file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content)

        # Output HTML file path
        html_filename = filename.replace('.md', '.html')
        html_path = os.path.join(posts_dir, html_filename)

        # Write the HTML to the new file
        with open(html_path, 'w', encoding='utf-8') as file:
            file.write(html_content + "\n<style>\n*{\n\tcolor: white;\n}\n</style>")

        print(f"Converted {filename} to {html_filename}")

print("done")