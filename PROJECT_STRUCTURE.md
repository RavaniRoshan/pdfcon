# Project Structure Documentation

## Overview

This is a complete HTML to PDF conversion system using the Doppio API. The project is organized for ease of use, maintainability, and extensibility.

## Directory Structure

```
pdfcon/
├── src/                          # Source files
│   ├── generator.py              # Main PDF generator class
│   └── template.html             # Default HTML template (ACP guide)
│
├── output/                       # Generated PDF files (auto-created)
│   ├── .gitkeep                  # Keeps directory in git
│   └── *.pdf                     # Your generated PDFs
│
├── .env.example                  # Environment variable template
├── .env                          # Your API key (create this, not in git)
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── README.md                     # Full documentation
├── QUICK_START.md                # Quick reference guide
├── PROJECT_STRUCTURE.md          # This file
│
├── setup.bat                     # Windows setup script
├── setup.sh                      # Unix/Linux/Mac setup script
│
├── example_usage.py              # Example scripts with 5 templates
└── batch_convert.py              # Batch conversion utility
```

## File Descriptions

### Core Files

#### `src/generator.py`
The main PDF generation engine.

**Key Classes:**
- `PDFGenerator`: Handles all PDF generation operations

**Key Methods:**
- `__init__(api_key)`: Initialize with API key
- `load_html_template(name)`: Load HTML from file
- `generate_pdf(html, filename, **options)`: Convert HTML to PDF
- `generate_from_template(template, output)`: Quick template conversion

**Features:**
- Environment variable support
- Error handling and validation
- Progress reporting
- Configurable output directory

#### `src/template.html`
Professional HTML template for the Agent Client Protocol guide.

**Features:**
- 7-page comprehensive guide
- Modern CSS styling with CSS variables
- Print-optimized layouts
- Page break controls
- Responsive typography
- Code highlighting
- Tables and blockquotes

### Utility Scripts

#### `example_usage.py`
Demonstrates various PDF generation use cases.

**Examples Included:**
1. Basic usage with default template
2. Custom HTML string conversion
3. Different page formats (A4, Letter, Legal, A5)
4. Professional invoice template
5. Resume/CV template

**Usage:**
```bash
python example_usage.py
```

#### `batch_convert.py`
Batch processing utility for converting multiple HTML files.

**Features:**
- Convert all HTML files in a directory
- Convert specific files by name
- Progress tracking
- Success/failure reporting
- Custom PDF options per batch

**Usage:**
```bash
# Convert all HTML files in src/
python batch_convert.py

# Convert specific files
python batch_convert.py file1.html file2.html
```

### Setup Scripts

#### `setup.bat` (Windows)
Automated setup for Windows users.

**Actions:**
- Checks Python installation
- Installs dependencies via pip
- Creates .env file from template
- Creates output directory
- Provides next steps

**Usage:**
```cmd
setup.bat
```

#### `setup.sh` (Unix/Linux/Mac)
Automated setup for Unix-based systems.

**Actions:**
- Checks Python 3 installation
- Creates virtual environment
- Installs dependencies
- Creates .env file
- Makes scripts executable
- Provides colored output and guidance

**Usage:**
```bash
chmod +x setup.sh
./setup.sh
source venv/bin/activate
```

### Configuration Files

#### `requirements.txt`
Python package dependencies.

**Packages:**
- `requests>=2.31.0` - HTTP library for API calls
- `python-dotenv>=1.0.0` - Environment variable management

#### `.env.example`
Template for environment variables.

**Variables:**
- `DOPPIO_API_KEY` - Your Doppio API key

**Setup:**
```bash
cp .env.example .env
# Edit .env and add your key
```

#### `.gitignore`
Prevents sensitive and generated files from being committed.

**Excluded:**
- Python cache files (`__pycache__`, `*.pyc`)
- Virtual environments (`venv/`, `env/`)
- Environment files (`.env`)
- Generated PDFs (`output/*.pdf`, `*.pdf`)
- IDE settings (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)

### Documentation

#### `README.md`
Comprehensive project documentation.

**Sections:**
- Features overview
- Installation instructions
- Usage examples
- API reference
- Customization guide
- Troubleshooting
- Security notes
- Contributing guidelines

#### `QUICK_START.md`
Quick reference for common tasks.

**Sections:**
- One-time setup (Windows/Mac/Linux)
- Common tasks with commands
- Creating custom PDFs
- Customization examples
- Troubleshooting quick fixes
- Pro tips

## Workflow

### Initial Setup
1. Run setup script (`setup.bat` or `setup.sh`)
2. Get API key from https://doppio.sh
3. Add key to `.env` file
4. Test with basic generation

### Development Workflow
1. Create HTML template in `src/`
2. Test in browser (Ctrl+P for print preview)
3. Run generator or batch converter
4. Check output in `output/` directory
5. Iterate on template as needed

### Production Usage
1. Import `PDFGenerator` class
2. Load or create HTML content
3. Call `generate_pdf()` with options
4. Handle success/error responses
5. Deliver PDF to user

## Extension Points

### Adding New Templates
1. Create HTML file in `src/`
2. Add custom CSS for print styling
3. Test with batch converter
4. Optional: Create dedicated generation script

### Custom PDF Options
```python
generator.generate_pdf(
    html_content=html,
    output_filename="custom.pdf",
    page_format="A4",           # Page size
    print_background=True,      # Backgrounds
    wait_for="networkidle0"     # Wait condition
)
```

### Integration with Web Apps
```python
from flask import Flask, request, send_file
from generator import PDFGenerator

app = Flask(__name__)
generator = PDFGenerator()

@app.route('/generate-pdf', methods=['POST'])
def generate():
    html = request.json.get('html')
    pdf_path = generator.generate_pdf(html, 'temp.pdf')
    return send_file(pdf_path, as_attachment=True)
```

## Best Practices

### HTML Templates
- Use semantic HTML5
- Include print-specific CSS (`@media print`)
- Test in browser print preview first
- Use page-break controls
- Optimize images before embedding

### Python Code
- Always load environment variables
- Handle exceptions gracefully
- Validate input before API calls
- Use meaningful output filenames
- Check API key before batch operations

### Security
- Never commit `.env` file
- Keep API keys in environment variables
- Validate user input for dynamic content
- Use `.gitignore` properly
- Rotate API keys periodically

### Performance
- Batch similar conversions together
- Reuse `PDFGenerator` instance
- Cache HTML templates when possible
- Optimize HTML/CSS before conversion
- Use appropriate `wait_for` conditions

## Dependencies

### Runtime Dependencies
- Python 3.8+
- requests library
- Doppio API access

### Optional Dependencies
- python-dotenv (environment management)
- Virtual environment (venv)

### External Services
- Doppio API (https://doppio.sh)
  - Free tier available
  - Handles PDF rendering
  - Returns high-quality PDFs

## Testing

### Manual Testing
```bash
# Test basic generation
python src/generator.py

# Test all examples
python example_usage.py

# Test batch conversion
python batch_convert.py
```

### Validation Checklist
- [ ] Python 3.8+ installed
- [ ] Dependencies installed
- [ ] API key configured
- [ ] Output directory exists
- [ ] Basic generation works
- [ ] Templates render correctly
- [ ] PDFs open without errors

## Troubleshooting

### Common Issues

**API Key Not Set**
- Check `.env` file exists
- Verify key is correct
- Reload terminal/environment

**Template Not Found**
- Ensure file is in `src/` directory
- Check filename spelling
- Verify file extension is `.html`

**PDF Quality Issues**
- Use higher resolution images
- Enable `print_background=True`
- Add print-specific CSS
- Test in browser first

**Import Errors**
- Activate virtual environment
- Reinstall dependencies
- Check Python version

## Future Enhancements

### Potential Features
- [ ] Custom headers/footers
- [ ] Watermark support
- [ ] PDF encryption/passwords
- [ ] Multiple files to single PDF
- [ ] HTML to multiple page formats
- [ ] Template variable substitution
- [ ] CLI with arguments
- [ ] Progress bars for batch
- [ ] PDF metadata customization
- [ ] Web interface

### Integration Ideas
- Flask/Django web app
- Automated report generation
- Invoice/receipt generation
- Documentation export
- Certificate generation
- Email attachments

## Support

### Resources
- **Full Documentation**: `README.md`
- **Quick Start**: `QUICK_START.md`
- **Doppio Docs**: https://doppio.sh/docs
- **Example Code**: `example_usage.py`

### Getting Help
1. Check documentation files
2. Review example scripts
3. Test with simple HTML first
4. Check Doppio API status
5. Verify API key is valid

---

**Last Updated**: January 2025
**Version**: 1.0.0
**License**: MIT (or as specified)