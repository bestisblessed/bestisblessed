import markdown
import asyncio
from playwright.async_api import async_playwright
import os
import base64
import shutil

# GitHub-like CSS styling
GITHUB_CSS = """
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    color: #e6edf3;
    background-color: #0d1117;
    max-width: 900px;
    margin: 0 auto;
    padding: 45px;
}
a {
    color: #58a6ff;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
h1, h2, h3, h4, h5, h6 {
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
    color: #e6edf3;
    border-bottom: 1px solid #30363d;
    padding-bottom: 0.3em;
}
h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.25em; border-bottom: none; }
h4 { font-size: 1em; border-bottom: none; }
code {
    background-color: #161b22;
    border-radius: 6px;
    font-size: 85%;
    margin: 0;
    padding: 0.2em 0.4em;
    font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;
    color: #e6edf3;
}
pre {
    background-color: #161b22;
    border-radius: 6px;
    font-size: 85%;
    line-height: 1.45;
    overflow: auto;
    padding: 16px;
}
pre code {
    background-color: transparent;
    border: 0;
    display: inline;
    line-height: inherit;
    margin: 0;
    overflow: visible;
    padding: 0;
    word-wrap: normal;
}
blockquote {
    border-left: 0.25em solid #3b434b;
    color: #8b949e;
    margin: 0;
    padding: 0 1em;
}
table {
    border-collapse: collapse;
    border-spacing: 0;
    display: block;
    max-width: 100%;
    overflow: auto;
    width: max-content;
    margin: 0 auto;
}
table th, table td {
    border: 1px solid #30363d;
    padding: 6px 13px;
}
table tr {
    background-color: #0d1117;
    border-top: 1px solid #21262d;
}
table tr:nth-child(2n) {
    background-color: #161b22;
}
table th {
    background-color: #161b22;
    font-weight: 600;
}
hr {
    background-color: #30363d;
    border: 0;
    height: 0.25em;
    margin: 24px 0;
    padding: 0;
}
img {
    max-width: 100%;
    box-sizing: content-box;
    border-radius: 6px;
}
details {
    display: block;
}
details summary {
    cursor: pointer;
    display: list-item;
    color: #58a6ff;
}
p {
    margin-top: 0;
    margin-bottom: 16px;
}
ul, ol {
    margin-top: 0;
    margin-bottom: 16px;
    padding-left: 2em;
}
.center {
    text-align: center;
}
div[align="center"] {
    text-align: center;
}
div[align="left"] {
    text-align: left;
}
sub {
    color: #8b949e;
}
"""

def read_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def get_image_as_base64(image_path):
    """Convert local image to base64 for embedding"""
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')
            ext = image_path.split('.')[-1].lower()
            if ext == 'jpg':
                ext = 'jpeg'
            return f"data:image/{ext};base64,{data}"
    return image_path

def convert_md_to_html(md_content, title):
    # Replace local image paths with base64
    if 'images/justin-jefferson-2.jpg' in md_content:
        base64_img = get_image_as_base64('/workspace/images/justin-jefferson-2.jpg')
        md_content = md_content.replace('images/justin-jefferson-2.jpg', base64_img)
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite', 'md_in_html'])
    html_content = md.convert(md_content)
    
    # Wrap in full HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{GITHUB_CSS}</style>
</head>
<body>
    {html_content}
</body>
</html>"""
    return full_html

async def capture_screenshot(html_content, output_path, title):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1200, 'height': 800})
        
        # Set the HTML content
        await page.set_content(html_content, wait_until='networkidle')
        
        # Wait for images to load
        await page.wait_for_timeout(2000)
        
        # Get full page height
        height = await page.evaluate('document.body.scrollHeight')
        
        # Resize viewport to capture full page
        await page.set_viewport_size({'width': 1200, 'height': min(height + 100, 4000)})
        
        # Take screenshot
        await page.screenshot(path=output_path, full_page=True)
        
        await browser.close()
        print(f"✓ Generated: {output_path}")

async def main():
    variations = [
        ('README_VARIATION_1.md', 'preview_variation_1.png', 'Variation 1: Minimalist Collapsible'),
        ('README_VARIATION_2.md', 'preview_variation_2.png', 'Variation 2: Stats Dashboard'),
        ('README_VARIATION_3.md', 'preview_variation_3.png', 'Variation 3: Bold Visual Grid'),
    ]
    
    for md_file, output_file, title in variations:
        md_path = f'/workspace/{md_file}'
        output_path = f'/workspace/images/{output_file}'
        
        print(f"Processing {md_file}...")
        
        # Read markdown
        md_content = read_markdown_file(md_path)
        
        # Convert to HTML
        html_content = convert_md_to_html(md_content, title)
        
        # Capture screenshot
        await capture_screenshot(html_content, output_path, title)
    
    print("\n✅ All previews generated in /workspace/images/")

if __name__ == '__main__':
    asyncio.run(main())
