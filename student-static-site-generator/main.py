import os
import markdown
from jinja2 import Template

content_dir = 'content'
template_path = 'templates/base.html'
output_dir = 'dist'

# Load HTML template
with open(template_path, 'r') as f:
    template = Template(f.read())

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
