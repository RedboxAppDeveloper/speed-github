# ./src/update/generate_index_html.py
import markdown
from pathlib import Path

readme_path = Path("README.md")
output_path = Path("index.html")

if readme_path.exists():
    with readme_path.open("r", encoding="utf-8") as f:
        text = f.read()
        html = markdown.markdown(text, extensions=["fenced_code", "codehilite"])

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>README</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
        }}
        pre code {{
            background: #f4f4f4;
            padding: 10px;
            display: block;
            overflow-x: auto;
        }}
    </style>
</head>
<body>
{html}
</body>
</html>"""

    with output_path.open("w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Generated {output_path}")
else:
    print("README.md not found.")
