# 🚀 START HERE - HTML to PDF Generator

Welcome! This is your complete HTML to PDF conversion toolkit. Everything is organized and ready to use.

## ⚠️ GETTING API KEY ERROR? READ THIS FIRST!

If you see **"DOPPIO_API_KEY environment variable is not set"**, follow these steps:

### 🔥 QUICK FIX (30 seconds):

**Windows:** Double-click `set_api_key.bat`  
**Mac/Linux:** Run `python3 set_api_key.py`

Then follow the prompts! That's it!

**Or see detailed instructions in:** `FIX_API_KEY.md`

---

## ✨ What This Project Does

Converts HTML documents to professional PDF files using the Doppio API. Perfect for:
- Invoices and receipts
- Reports and documentation
- Resumes and CVs
- Certificates
- Any HTML content you want as PDF

## 📦 What's Included

```
pdfcon/
├── 📄 Core Files
│   ├── src/generator.py          ← Main PDF generator
│   └── src/template.html         ← Sample HTML template
│
├── 🛠️ Utilities
│   ├── example_usage.py          ← 5 ready-to-use examples
│   ├── batch_convert.py          ← Convert multiple files
│   ├── setup.bat                 ← Windows setup (1-click)
│   └── setup.sh                  ← Mac/Linux setup (1-click)
│
├── 📚 Documentation
│   ├── START_HERE.md             ← This file
│   ├── README.md                 ← Full documentation
│   ├── QUICK_START.md            ← Quick reference
│   ├── PROJECT_STRUCTURE.md      ← Project details
│   └── CHANGELOG.md              ← Version history
│
├── ⚙️ Configuration
│   ├── requirements.txt          ← Python packages
│   ├── .env.example              ← API key template
│   └── .gitignore                ← Git exclusions
│
└── 📂 output/                    ← Your PDFs go here
```

## 🎯 Quick Setup (Choose Your OS)

### Windows Users

1. **Double-click `setup.bat`** (or run in Command Prompt)
2. **Get API Key**: Go to https://doppio.sh (free signup)
3. **Set up API key**: 
   - **Easy way**: Double-click `set_api_key.bat`
   - **Manual way**: Edit `.env` file in Notepad
     - Replace `your_api_key_here` with your actual key
     - Save as `.env` (NOT .env.txt!)
4. **Done!** Now run: `python src\generator.py`

💡 **Having issues?** See `FIX_API_KEY.md` for detailed help!

### Mac/Linux Users

1. **Open Terminal** in this folder
2. **Run setup**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
3. **Get API Key**: Go to https://doppio.sh (free signup)
4. **Set up API key**:
   - **Easy way**: Run `python3 set_api_key.py`
   - **Manual way**: Edit `.env` file:
     ```bash
     nano .env
     # Replace your_api_key_here with actual key
     # Press Ctrl+X, Y, Enter to save
     ```
5. **Activate environment**:
   ```bash
   source venv/bin/activate
   ```
6. **Done!** Now run: `python3 src/generator.py`

💡 **Having issues?** See `FIX_API_KEY.md` for detailed help!

## 🎬 Try It Now!

### ✅ Test the API Fix (Recommended First!)

If you encountered the 404 error earlier, test that it's fixed:

**Windows:**
```cmd
python test_fix.py
```

**Mac/Linux:**
```bash
python3 test_fix.py
```

This creates a simple test PDF to verify the API is working!

### Generate Your First PDF

**Windows:**
```cmd
python src\generator.py
```

**Mac/Linux:**
```bash
python3 src/generator.py
```

✅ **Your PDF is in `output/acp-101-guide.pdf`**
✅ Look in `output/` folder for `acp-101-guide.pdf`

### See 5 Example PDFs

**Windows:**
```cmd
python example_usage.py
```

**Mac/Linux:**
```bash
python3 example_usage.py
```

This creates:
- ✅ Basic document
- ✅ Custom HTML example
- ✅ Different page formats (A4, Letter, Legal, A5)
- ✅ Professional invoice
- ✅ Resume template

### Convert All Your HTML Files

**Windows:**
```cmd
python batch_convert.py
```

**Mac/Linux:**
```bash
python3 batch_convert.py
```

Converts every `.html` file in `src/` folder!

## 🎨 Create Your Own PDF (3 Ways)

### Method 1: HTML File (Easiest)

1. Create `src/my-document.html`:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <style>
           body { font-family: Arial; margin: 2cm; }
           h1 { color: #2c3e50; }
       </style>
   </head>
   <body>
       <h1>Hello World!</h1>
       <p>My first PDF!</p>
   </body>
   </html>
   ```

2. Convert it:
   ```bash
   python batch_convert.py my-document.html
   ```

3. Find PDF: `output/my-document.pdf`

### Method 2: Python Script

Create `my_pdf.py`:
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
        h1 { color: #e74c3c; }
    </style>
</head>
<body>
    <h1>My Custom PDF</h1>
    <p>Generated from Python!</p>
</body>
</html>
"""

generator = PDFGenerator()
generator.generate_pdf(html_content=html, output_filename="my-custom.pdf")
print("✅ PDF created!")
```

Run: `python my_pdf.py`

### Method 3: Interactive Python

```python
from dotenv import load_dotenv
load_dotenv()

import sys
from pathlib import Path
sys.path.insert(0, "src")
from generator import PDFGenerator

# Initialize
gen = PDFGenerator()

# Generate from template
gen.generate_from_template("template.html", "output.pdf")

# Or from HTML string
html = "<h1>Quick PDF</h1><p>So easy!</p>"
gen.generate_pdf(html, "quick.pdf")
```

## 🔧 Customize Your PDFs

```python
generator.generate_pdf(
    html_content=your_html,
    output_filename="custom.pdf",
    
    # Page size options
    page_format="Letter",        # A4, Letter, Legal, A5, A3, Tabloid
    
    # Appearance
    print_background=True,       # Include colors & backgrounds
    
    # Loading
    wait_for="networkidle0"      # networkidle0, load, domcontentloaded
)
```

## 💡 Pro Tips

### 1. Test in Browser First
- Open HTML in Chrome/Firefox
- Press `Ctrl+P` (or `Cmd+P` on Mac)
- Check print preview
- Adjust CSS as needed

### 2. Use Print-Specific CSS
```css
@media print {
    body { padding: 1.5cm; }
    h1 { page-break-after: avoid; }
    .no-print { display: none; }
}
```

### 3. Add Page Breaks
```html
<div style="page-break-before: always;"></div>
```

### 4. Control Page Size
```css
@page {
    size: A4;
    margin: 2cm;
}
```

## 🐛 Troubleshooting

### "DOPPIO_API_KEY not set"
- ✅ Create `.env` file from `.env.example`
- ✅ Add your API key from https://doppio.sh
- ✅ Restart terminal/command prompt

### "Template not found"
- ✅ Put HTML files in `src/` folder
- ✅ Check filename spelling
- ✅ Use `.html` extension

### "Request timed out"
- ✅ Check internet connection
- ✅ Try again (servers might be busy)
- ✅ Reduce HTML size/complexity

### Import errors
- ✅ Run setup script again
- ✅ Activate virtual environment (Mac/Linux)
- ✅ Check Python version (need 3.8+)

## 📖 Documentation Files

| File | Purpose |
|------|---------|
| **START_HERE.md** | You are here! Quick overview |
| **QUICK_START.md** | Command reference & recipes |
| **README.md** | Complete documentation |
| **PROJECT_STRUCTURE.md** | Technical details |
| **CHANGELOG.md** | Version history |

## 🎓 Learning Path

1. **Beginner**: 
   - Run `setup.bat` / `setup.sh`
   - Generate default PDF
   - Try examples

2. **Intermediate**:
   - Create custom HTML file
   - Use batch converter
   - Customize page formats

3. **Advanced**:
   - Use Python API directly
   - Integrate with your app
   - Create templates with variables

## 🔗 Important Links

- **Get API Key**: https://doppio.sh (required, free tier available)
- **Doppio Docs**: https://doppio.sh/docs
- **HTML Print CSS**: https://www.smashingmagazine.com/print-css-tips/

## 📋 Quick Command Reference

### Windows
```cmd
python src\generator.py              # Generate from template
python example_usage.py              # Run all examples
python batch_convert.py              # Convert all HTML files
python batch_convert.py file.html   # Convert specific file
```

### Mac/Linux
```bash
source venv/bin/activate             # Activate environment (first time)
python3 src/generator.py             # Generate from template
python3 example_usage.py             # Run all examples
python3 batch_convert.py             # Convert all HTML files
python3 batch_convert.py file.html  # Convert specific file
```

## ✅ Checklist

Before you start:
- [ ] Python 3.8+ installed
- [ ] Ran setup script (`setup.bat` or `setup.sh`)
- [ ] Got API key from https://doppio.sh
- [ ] Added key to `.env` file
- [ ] Tested with: `python src/generator.py`

## 🎉 You're Ready!

Everything is set up and ready to use. Pick a method above and start creating PDFs!

**Need help?** Check:
1. `QUICK_START.md` for common tasks
2. `README.md` for full documentation
3. `example_usage.py` for code examples

**Happy PDF generating!** 🚀📄

---

**Version**: 1.0.0  
**Last Updated**: January 2025  
**Project**: HTML to PDF Generator