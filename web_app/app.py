#!/usr/bin/env python3
"""
Flask web application for PDF generation with Claude-style interface
"""

import os
import sys
import markdown
from pathlib import Path
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename

# Add parent directory to path to import existing modules
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.generator import PDFGenerator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-change-in-production'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize PDF generator
pdf_generator = PDFGenerator()

# Ensure output directory exists
output_dir = Path(__file__).parent.parent / "output"
output_dir.mkdir(exist_ok=True)

def process_markdown_content(content, mode="markdown"):
    """
    Process content based on input mode and convert to HTML

    Args:
        content: Input content (markdown or prompt)
        mode: "markdown" or "prompt"

    Returns:
        HTML content ready for PDF generation
    """
    if mode == "markdown":
        # Direct markdown processing
        html_content = markdown.markdown(content)
    else:
        # For prompt mode, treat as simple markdown for now
        # In a real implementation, you might use AI to enhance formatting
        html_content = markdown.markdown(content)

    # Apply professional styling (similar to existing template)
    css = '''<style>
        :root {
          --bg: #ffffff;
          --text: #1a1a1a;
          --accent: #10b981;
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
      </style>'''

    # Create header
    header = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Generated PDF Document</title>
  {css}
</head>
<body>
<h1>📄 Generated Document</h1>
<p style="text-align: center; font-size: 1.2rem; color: #666; margin-bottom: 3rem;">Created with PDF Generation Agent</p>
'''

    # Add footer
    footer = '''
<div class="footer">
  <p>Generated by PDF Generation Agent</p>
  <p>Powered by Doppio API</p>
</div>
</body>
</html>
'''

    # Combine
    full_html = header + html_content + footer
    return full_html

@app.route('/')
def index():
    """Render the main PDF generation app interface as the default page"""
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    """Generate PDF from user input"""
    try:
        # Get form data
        content = request.form.get('content', '').strip()
        mode = request.form.get('mode', 'markdown')

        if not content:
            return jsonify({'error': 'Content is required'}), 400

        # Process content based on mode
        html_content = process_markdown_content(content, mode)

        # Generate unique filename
        import uuid
        filename = f"generated_{uuid.uuid4().hex[:8]}.pdf"

        # Generate PDF
        output_path = pdf_generator.generate_pdf(
            html_content=html_content,
            output_filename=filename,
            page_format="A4",
            print_background=True
        )

        return jsonify({
            'success': True,
            'filename': filename,
            'download_url': f'/download/{filename}'
        })

    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        return jsonify({'error': 'Failed to generate PDF. Please try again.'}), 500

@app.route('/download/<filename>')
def download_file(filename):
    """Serve the generated PDF file"""
    try:
        file_path = output_dir / filename
        if file_path.exists():
            return send_file(
                file_path,
                as_attachment=True,
                download_name=filename,
                mimetype='application/pdf'
            )
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Download failed'}), 500

@app.errorhandler(413)
def too_large(e):
    return jsonify({'error': 'File too large. Maximum size is 16MB.'}), 413

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
