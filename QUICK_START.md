# Quick Start Guide

Get up and running with the HTML to PDF Generator in 5 minutes!

## 🚀 One-Time Setup

### Windows

1. **Run the setup script:**
   ```cmd
   setup.bat
   ```

2. **Add your API key:**
   - Open `.env` file in Notepad
   - Replace `your_api_key_here` with your actual key
   - Save and close

### Mac/Linux

1. **Run the setup script:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

2. **Add your API key:**
   ```bash
   nano .env
   # Replace your_api_key_here with your actual key
   # Press Ctrl+X, then Y, then Enter to save
   ```

3. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

### Get Your API Key

Sign up for free at: **https://doppio.sh**

---

## 📝 Common Tasks

### Generate PDF from Default Template

**Windows:**
```cmd
python src\generator.py
```

**Mac/Linux:**
```bash
python3 src/generator.py
```

**Output:** `output/acp-101-guide.pdf`

---

### Convert All HTML Files at Once

**Windows:**
```cmd
python batch_convert.py
```

**Mac/Linux:**
```bash
python3 batch_convert.py
```

Converts all `.html` files in the `src/` folder.

---

### Run Example Templates

**Windows:**
```cmd
python example_usage.py
```

**Mac/Linux:**
```bash
python3 example_usage.py
```

Generates 5 example PDFs:
- Basic document
- Custom HTML
- Different page formats (A4, Letter, Legal, A5)
- Professional invoice
- Resume

---

## 🎨 Create Your Own PDF

### Option 1: Use HTML Template File

1. **Create your HTML file** in `src/` folder:
   ```
   src/my-document.html
   ```

2. **Run batch converter:**
   ```bash
   python batch_convert.py my-document.html
   ```

3. **Find your PDF** in `output/my-document.pdf`

---

### Option 2: Use Python Script

Create a file `my_pdf.py`:

```python
from dotenv import load_dotenv
load_dotenv()

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))
from generator import PDFGenerator

html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial; margin: 2cm; }
        h1 { color: #2c3e50; }
    </style>
</head>
<body>
    <h1>My Custom PDF</h1>
    <p>This is my content!</p>
</body>
</html>
"""

generator = PDFGenerator()
generator.generate_pdf(
    html_content=html,
    output_filename="my-custom.pdf"
)
print("✅ Done!")
```

Run it:
```bash
python my_pdf.py
```

---

## 🔧 Customize PDF Settings

```python
generator.generate_pdf(
    html_content=html,
    output_filename="custom.pdf",
    page_format="Letter",        # A4, Letter, Legal, A5, etc.
    print_background=True,       # Include background colors
    wait_for="networkidle0"      # Wait for page to fully load
)
```

### Available Page Formats

- **A4** (default) - 210mm × 297mm
- **Letter** - 8.5" × 11"
- **Legal** - 8.5" × 14"
- **A3** - 297mm × 420mm
- **A5** - 148mm × 210mm
- **Tabloid** - 11" × 17"

---

## 🎯 Tips for Better PDFs

### 1. Use Print-Specific CSS

```css
@media print {
    body {
        padding: 1.5cm;
    }
    h1 {
        page-break-after: avoid;
    }
    pre, code {
        page-break-inside: avoid;
    }
}
```

### 2. Add Page Breaks

```html
<div style="page-break-before: always;"></div>
```

Or with CSS:
```css
.new-page {
    page-break-before: always;
}
```

### 3. Control Page Margins

```css
@page {
    margin: 2cm;
}
```

### 4. Prevent Content Splitting

```css
.keep-together {
    page-break-inside: avoid;
}
```

---

## 🐛 Troubleshooting

### "DOPPIO_API_KEY environment variable is not set"

**Solution:** Add your API key to `.env` file:
```
DOPPIO_API_KEY=your_actual_key_here
```

Then reload your terminal or run:
- Windows: `set DOPPIO_API_KEY=your_key`
- Mac/Linux: `export DOPPIO_API_KEY=your_key`

---

### "Template not found"

**Solution:** Make sure your HTML file is in the `src/` directory:
```
pdfcon/
├── src/
│   ├── template.html        ✅ Correct location
│   └── your-file.html       ✅ Correct location
└── your-file.html           ❌ Wrong location
```

---

### "Request timed out"

**Solution:**
1. Check your internet connection
2. Try again (Doppio servers might be busy)
3. Reduce HTML complexity (remove large images)

---

### PDF looks different than HTML

**Solution:**
1. Use web-safe fonts or embed fonts
2. Add print-specific CSS with `@media print`
3. Test in browser print preview (Ctrl+P / Cmd+P)
4. Avoid CSS features not supported in print (animations, transforms)

---

## 📚 More Examples

### Invoice Template

```python
generator.generate_from_template(
    template_name="invoice.html",
    output_filename="invoice-2025-001.pdf",
    page_format="Letter"
)
```

### Report with Header/Footer

```html
<style>
@page {
    margin: 3cm 2cm;
    @top-center {
        content: "Company Report";
    }
    @bottom-right {
        content: counter(page);
    }
}
</style>
```

### Multi-Page Document

```html
<h1>Page 1</h1>
<p>Content for page 1...</p>

<div style="page-break-before: always;"></div>

<h1>Page 2</h1>
<p>Content for page 2...</p>
```

---

## 🔗 Useful Links

- **Doppio API Docs:** https://doppio.sh/docs
- **Get API Key:** https://doppio.sh
- **HTML Print CSS:** https://www.smashingmagazine.com/print-css-tips/
- **Project README:** See `README.md` for full documentation

---

## 💡 Pro Tips

1. **Test in Browser First**
   - Open your HTML in Chrome/Firefox
   - Press Ctrl+P (Cmd+P on Mac)
   - Check print preview before generating PDF

2. **Use Virtual Environment**
   - Keeps dependencies isolated
   - Prevents conflicts with other projects

3. **Batch Process**
   - Convert multiple files at once with `batch_convert.py`
   - Saves time and API calls

4. **Template Reusability**
   - Create template HTML files
   - Use Python to inject dynamic content
   - Generate personalized PDFs programmatically

5. **Version Control**
   - Don't commit `.env` file (API keys!)
   - Don't commit `output/*.pdf` files
   - `.gitignore` handles this automatically

---

**Need Help?** Check the full documentation in `README.md`

**Happy PDF Generation! 🎉**