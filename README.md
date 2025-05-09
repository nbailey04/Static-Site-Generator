# Student Static Site Generator

This is a simple static site generator written in Python. It converts Markdown files into styled HTML pages using Jinja2 templating.

## Features

- Converts `.md` (Markdown) files from the `content/` directory into `.html` pages
- Uses a base HTML template stored in `templates/base.html`
- Outputs generated HTML files to the `dist/` directory

## Getting Started

### Prerequisites

You'll need to install the required libraries:

```bash
pip install markdown jinja2
