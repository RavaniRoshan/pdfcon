# HTML to PDF Generator

A Python-based HTML to PDF conversion tool using the [Doppio API](https://doppio.sh). This project converts professionally styled HTML templates into high-quality PDF documents with support for custom styling, page breaks, and print-optimized layouts.

## 📋 Features

- **🎨 Professional Styling**: Modern, clean design with CSS variables and print-optimized layouts
- **📄 Template-Based**: Separate HTML templates for easy content management
- **🔒 Secure**: API key-based authentication with environment variable support
- **⚡ Fast**: Efficient PDF rendering with configurable wait conditions
- **🛠️ Flexible**: Customizable page formats, backgrounds, and rendering options
- **📊 Detailed Output**: File size reporting and clear status messages

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Doppio API key (sign up for free at [doppio.sh](https://doppio.sh))

### Installation

1. **Clone or download this project**

2. **Navigate to the project directory**
   ```bash
   cd pdfcon
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**

   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your Doppio API key:
   ```
   DOPPIO_API_KEY=your_actual_api_key_here
   ```

   **Alternative**: Set the environment variable directly:
   
   - **Windows (Command Prompt)**:
     ```cmd
     set DOPPIO_API_KEY=your_api_key_here
     ```
   
   - **Windows (PowerShell)**:
     ```powershell
     $env:DOPPIO_API_KEY="your_api_key_here"
     ```
   
   - **Linux/Mac**:
     ```bash
     export DOPPIO_API_KEY=your_api_key_here
     ```

### Usage

**Basic usage** (generates PDF from default template):
```bash
python src/generator.py
```

**Using python-dotenv** (automatically loads .env file):
```python
from dotenv import load_dotenv
load_dotenv()

from generator import PDFGenerator

generator = PDFGenerator()
generator.generate_from_template(
    template_name="template.html",
    output_filename="my-document.pdf"
)
```

The generated PDF will be saved in the `output/` directory.

## 📁 Project Structure

```
pdfcon/
├── src/
│   ├── generator.py       # Main PDF generation script
│   └── template.html      # HTML template (ACP 101 Guide)
├── output/                # Generated PDF files (created automatically)
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment configuration
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🎨 Customization

### Using Custom HTML Templates

1. **Create a new HTML file** in the `src/` directory:
   ```html
   <!-- src/my-template.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>My Document</title>
       <style>
           /* Your custom styles */
       </style>
   </head>
   <body>
       <!-- Your content -->
   </body>
   </html>
   ```

2. **Generate PDF from your template**:
   ```python
   from src.generator import PDFGenerator
   
   generator = PDFGenerator()
   generator.generate_from_template(
       template_name="my-template.html",
       output_filename="my-output.pdf"
   )
   ```

### Customizing PDF Options

```python
generator.generate_from_template(
    template_name="template.html",
    output_filename="custom.pdf",
    page_format="Letter",        # A4, Letter, Legal, etc.
    print_background=True,       # Include background colors/images
    wait_for="networkidle0"      # Wait condition: networkidle0, load, domcontentloaded
)
```

### Using Direct HTML Content

```python
html_content = """
<!DOCTYPE html>
<html>
<body>
    <h1>Hello, World!</h1>
    <p>This is a simple PDF.</p>
</body>
</html>
"""

generator = PDFGenerator()
generator.generate_pdf(
    html_content=html_content,
    output_filename="hello.pdf"
)
```

## 🔧 API Reference

### `PDFGenerator` Class

#### `__init__(api_key: Optional[str] = None)`
Initialize the PDF generator.
- **api_key**: Doppio API key (defaults to `DOPPIO_API_KEY` environment variable)

#### `load_html_template(template_name: str) -> str`
Load HTML content from a template file.
- **template_name**: Name of the template file in `src/` directory
- **Returns**: HTML content as string

#### `generate_pdf(html_content: str, output_filename: str, **kwargs) -> Path`
Generate PDF from HTML content.
- **html_content**: HTML string to convert
- **output_filename**: Name of output PDF file
- **page_format**: Page size (default: "A4")
- **print_background**: Print backgrounds (default: True)
- **wait_for**: Wait condition (default: "networkidle0")
- **Returns**: Path to generated PDF file

#### `generate_from_template(template_name: str, output_filename: str, **kwargs) -> Path`
Generate PDF from a template file.
- **template_name**: Template filename (default: "template.html")
- **output_filename**: Output PDF filename (default: "output.pdf")
- **Returns**: Path to generated PDF file

## 📖 Example: Current Template

The included `template.html` generates a comprehensive guide about the **Agent Client Protocol (ACP)**, featuring:

- Modern, professional styling
- Responsive typography with system fonts
- Code syntax highlighting
- Tables and blockquotes
- Page breaks for printing
- Print-optimized CSS media queries

**Output**: `output/acp-101-guide.pdf` (7 pages)

## 🐛 Troubleshooting

### Error: "DOPPIO_API_KEY environment variable is not set"
**Solution**: Ensure your API key is set in `.env` file or as an environment variable.

### Error: "Template not found"
**Solution**: Verify the template file exists in the `src/` directory with the correct filename.

### Error: "Request timed out"
**Solution**: Check your internet connection. Large HTML files may take longer to render.

### Error: "HTTP 401 Unauthorized"
**Solution**: Your API key is invalid. Get a new key from [doppio.sh](https://doppio.sh).

### Error: "HTTP 429 Too Many Requests"
**Solution**: You've exceeded your API rate limit. Wait a moment or upgrade your plan.

## 📝 Requirements

- **Python**: 3.8+
- **Dependencies**:
  - `requests>=2.31.0` - HTTP library for API calls
  - `python-dotenv>=1.0.0` - Environment variable management (optional)

## 🔐 Security Notes

- Never commit your `.env` file or expose your API key
- The `.gitignore` file is configured to exclude sensitive files
- API keys should be treated as secrets

## 📄 License

This project is provided as-is for educational and commercial use. The Doppio API is subject to its own terms of service.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new HTML templates
- Improve error handling
- Add features (batch processing, custom fonts, etc.)
- Report bugs or suggest enhancements

## 🔗 Resources

- **Doppio API Documentation**: [https://doppio.sh/docs](https://doppio.sh)
- **Sign Up for API Key**: [https://doppio.sh](https://doppio.sh)
- **HTML to PDF Best Practices**: Consider using print-specific CSS with `@media print`

## 💡 Tips

1. **Use semantic HTML** for better PDF structure
2. **Test print styles** with browser print preview (Ctrl+P / Cmd+P)
3. **Optimize images** before embedding in HTML
4. **Use `page-break-before` and `page-break-after`** CSS for page control
5. **Set explicit page sizes** in CSS for consistent output

---

**Made with ❤️ for developers who need beautiful PDFs**