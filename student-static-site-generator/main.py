import os
import markdown
from jinja2 import Template

content_dir = 'content'
template_path = 'templates/base.html'
output_dir = 'dist'

# Load HTML template
with open(template_path, 'r') as f:
    template = Template(f.read())
import os
import markdown
from jinja2 import Template

CONTENT_DIR = 'content'
TEMPLATE_PATH = 'templates/base.html'
OUTPUT_DIR = 'dist'

def load_template(path):
    with open(path, 'r', encoding='utf-8') as f:
        return Template(f.read())

def convert_markdown_to_html(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    return markdown.markdown(md_content)

def generate_site():
    template = load_template(TEMPLATE_PATH)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith('.md'):
            md_path = os.path.join(CONTENT_DIR, filename)
            html_content = convert_markdown_to_html(md_path)
            html_page = template.render(title='My Page', content=html_content)

            output_path = os.path.join(OUTPUT_DIR, filename.replace('.md', '.html'))
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_page)

    print(f"Site generated in '{OUTPUT_DIR}' directory.")

if __name__ == "__main__":
    generate_site()

# Process markdown files
for filename in os.listdir(content_dir):
    if filename.endswith('.md'):
        with open(os.path.join(content_dir, filename), 'r') as f:
            md_content = f.read()
            html_content = markdown.markdown(md_content)
            html_page = template.render(title='My Page', content=html_content)

        output_path = os.path.join(output_dir, filename.replace('.md', '.html'))
        with open(output_path, 'w') as f:
            f.write(html_page)

print("Site generated in 'dist' directory.")
