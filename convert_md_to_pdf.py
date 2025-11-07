#!/usr/bin/env python3
"""
Convert Markdown to PDF using HTML template - refined for LinkedIn carousel.
"""

import os
from pathlib import Path
import markdown
from src.generator import PDFGenerator

# Read the markdown file
md_path = Path("it a 2hr video couarse make a written couse on wha.md")
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Remove unwanted sections: perplexity logo, header, transcript description, footer notes
lines = md_content.split('\n')
filtered_lines = []
skip_section = False
for line in lines:
    # Skip perplexity image and transcript intro
    if '<img src="https://r2cdn.perplexity.ai/' in line:
        continue
    if 'it a 2hr video couarse make a written couse' in line:
        skip_section = True
    if 'written course transcript' in line and 'Cole Medin' in line:
        skip_section = True
    if skip_section and '***' in line:
        skip_section = False
        continue
    if skip_section:
        continue
    # Skip the final notes
    if '**You now have the complete workflow**' in line:
        break
    if line.startswith('<div align="center">⁂</div>'):
        break
    if '[^1]:' in line:
        break
    filtered_lines.append(line)

# Join back and fix some text
refined_content = '\n'.join(filtered_lines)
# Fix typo
refined_content = refined_content.replace("couarse", "course")
refined_content = refined_content.replace("wha", "what")

# Convert markdown to HTML
html_content = markdown.markdown(refined_content)

# Custom color scheme for AI/tech theme (green)
css = '''<style>
    :root {
      --bg: #ffffff;
      --text: #1a1a1a;
      --accent: #10b981; /* Green for AI/tech */
      --accent-light: #d1fae5;
      --border: #e5e7eb;
      --code-bg: #f9fafb;
      --shadow: rgba(0, 0, 0, 0.05);
      --font-main: 'Segoe UI', system-ui, -apple-system, sans-serif;
      --font-mono: 'SF Mono', 'Monaco', 'Inconsolata', monospace;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: var(--font-main);
      line-height: 1.6;
      color: var(--text);
      background: var(--bg);
      padding: 2rem;
      max-width: 800px;
      margin: 0 auto;
    }

    @media print {
      body {
        padding: 1.5rem;
        max-width: 100%;
      }
      h1, h2, h3 {
        page-break-after: avoid;
        page-break-inside: avoid;
      }
      pre, code {
        page-break-inside: avoid;
      }
    }

    h1 {
      font-size: 2.8rem;
      font-weight: 800;
      margin: 1rem 0 2rem;
      color: var(--accent);
      text-align: center;
      letter-spacing: -0.02em;
    }

    h2 {
      font-size: 2rem;
      font-weight: 700;
      margin: 3rem 0 1.5rem;
      padding: 1rem;
      background: var(--accent-light);
      color: var(--text);
      border-radius: 8px;
      text-align: center;
      page-break-before: always; /* Each section on new page for carousel */
    }

    h3 {
      font-size: 1.4rem;
      font-weight: 600;
      margin: 2rem 0 1rem;
      color: var(--accent);
    }

    p, li {
      margin-bottom: 1rem;
      font-size: 1.1rem;
    }

    ul, ol {
      padding-left: 1.5rem;
      margin-bottom: 1.2rem;
    }

    li {
      margin-bottom: 0.8rem;
    }

    blockquote {
      background: var(--accent-light);
      border-left: 4px solid var(--accent);
      padding: 1rem 1.2rem;
      margin: 1.5rem 0;
      font-style: italic;
      border-radius: 0 6px 6px 0;
      font-weight: 500;
    }

    code {
      font-family: var(--font-mono);
      background: var(--code-bg);
      padding: 0.3rem 0.5rem;
      border-radius: 4px;
      font-size: 0.95em;
    }

    pre {
      background: var(--code-bg);
      padding: 1.2rem;
      border-radius: 8px;
      overflow-x: auto;
      margin: 1.5rem 0;
      font-family: var(--font-mono);
      font-size: 0.9em;
      border: 1px solid var(--border);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
    }

    th, td {
      padding: 0.8rem 1rem;
      text-align: left;
      border-bottom: 1px solid var(--border);
    }

    th {
      background: var(--accent-light);
      font-weight: 700;
      color: var(--accent);
    }

    tr:last-child td {
      border-bottom: none;
    }

    .highlight {
      background: #fffbeb;
      padding: 0.2rem 0.4rem;
      border-radius: 4px;
      font-weight: 600;
    }

    .footer {
      margin-top: 3rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--border);
      font-size: 0.9rem;
      color: #666;
      text-align: center;
    }

    .emoji {
      font-size: 1.5rem;
    }
  </style>'''

# Create header
header = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>The Ultimate Guide to Local AI and AI Agents</title>
  {css}
</head>
<body>
<h1>🚀 The Ultimate Guide to Local AI and AI Agents</h1>
<p style="text-align: center; font-size: 1.2rem; color: #666; margin-bottom: 3rem;">Build private, powerful AI agents on your own hardware</p>
'''

# Refine the HTML content for carousel style
# Add some visual elements and make it more slide-friendly
carousel_html = html_content.replace('<h2>', '<h2 class="slide-header">')
# Add emojis and visual elements
carousel_html = carousel_html.replace('<h2>Section 1: Introduction & Agenda</h2>', '<h2>📋 Slide 1: Why Go Local With AI?</h2>')
carousel_html = carousel_html.replace('<h2>Section 2: What is Local AI?</h2>', '<h2>🤖 Slide 2: What is Local AI?</h2>')
carousel_html = carousel_html.replace('<h2>Section 3: Local AI vs Cloud AI</h2>', '<h2>⚖️ Slide 3: Local vs Cloud AI</h2>')
carousel_html = carousel_html.replace('<h2>Section 4: Hardware Requirements</h2>', '<h2>🖥️ Slide 4: Hardware You Need</h2>')
carousel_html = carousel_html.replace('<h2>Section 5: Quantization & Offloading</h2>', '<h2>🔧 Slide 5: Optimization Techniques</h2>')
carousel_html = carousel_html.replace('<h2>Section 6: Ollama Configuration</h2>', '<h2>⚙️ Slide 6: Setting Up Ollama</h2>')
carousel_html = carousel_html.replace('<h2>Section 7: The Local AI Package</h2>', '<h2>📦 Slide 7: Complete AI Stack</h2>')
carousel_html = carousel_html.replace('<h2>Section 8: Connecting, Using & Extending Agents</h2>', '<h2>🔗 Slide 8: Building Agents</h2>')
carousel_html = carousel_html.replace('<h2>Section 9: Deployment & Cloud Hosting</h2>', '<h2>☁️ Slide 9: Going Live</h2>')
carousel_html = carousel_html.replace('<h2>Section 10: Additional Resources & Support</h2>', '<h2>📚 Slide 10: Next Steps</h2>')

# Add footer
footer = '''
<div class="footer">
  <p>🔒 <strong>Privacy First:</strong> Your data stays on your hardware</p>
  <p>💰 <strong>Cost Effective:</strong> No API fees, invest once in hardware</p>
  <p>⚡ <strong>High Performance:</strong> Local inference, instant responses</p>
  <p style="margin-top: 1.5rem;">Ready to get started? Check out the resources above!</p>
  <p style="margin-top: 1rem; font-style: italic;">#LocalAI #AIagents #Privacy #MachineLearning</p>
</div>
</body>
</html>
'''

# Combine
full_html = header + carousel_html + footer

# Save to temporary HTML file
temp_html = Path("output/ai-agents-carousel-guide.html")
with open(temp_html, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Created carousel HTML file: {temp_html}")

# Generate PDF
generator = PDFGenerator()
output_path = generator.generate_pdf(
    html_content=full_html,
    output_filename="local-ai-agents-carousel.pdf",
    page_format="A4",
    print_background=True
)

print(f"Carousel PDF generated: {output_path}")
