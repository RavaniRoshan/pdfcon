# Changelog

All notable changes to the HTML to PDF Generator project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2025-01-16

### Fixed
- **API Endpoint**: Corrected Doppio API endpoint from incorrect `/v1/render/pdf` to proper `/v1/render/pdf/direct`
- **Request Format**: Updated request structure to use proper Doppio API format with base64-encoded HTML and Bearer authentication
- **Authentication**: Changed from basic auth to Bearer token in headers
- **HTTP 404 Error**: Resolved "Cannot POST /v1/render/pdf" 404 error by using correct endpoint and request body structure
- **Base64 Encoding**: Added proper base64 encoding for HTML content as required by Doppio API

### Added
- **Test Script**: Added `test_fix.py` for verifying API integration
- **Better Error Handling**: Improved error messages with troubleshooting guidance
- **Automatic .env Loading**: Enhanced environment variable loading with fallbacks

## [1.0.0] - 2025-01-15

### Added
- Initial release of HTML to PDF Generator
- Core `PDFGenerator` class with full API integration
- Professional HTML template (Agent Client Protocol guide)
- Batch conversion utility (`batch_convert.py`)
- Example usage script with 5 different templates:
  - Basic document generation
  - Custom HTML string conversion
  - Multiple page format examples (A4, Letter, Legal, A5)
  - Professional invoice template
  - Resume/CV template
- Automated setup scripts:
  - `setup.bat` for Windows
  - `setup.sh` for Unix/Linux/Mac
- Comprehensive documentation:
  - `README.md` - Full project documentation
  - `QUICK_START.md` - Quick reference guide
  - `PROJECT_STRUCTURE.md` - Project organization details
- Configuration files:
  - `requirements.txt` - Python dependencies
  - `.env.example` - Environment variable template
  - `.gitignore` - Git exclusion rules
- Virtual environment support
- Environment variable management with python-dotenv
- Error handling and validation
- Progress reporting and status messages
- File size reporting for generated PDFs
- Configurable PDF options:
  - Page format (A4, Letter, Legal, etc.)
  - Background printing
  - Wait conditions for rendering

### Features
- **Template-Based Generation**: Load HTML from files
- **Direct HTML Conversion**: Convert HTML strings to PDF
- **Batch Processing**: Convert multiple files at once
- **Security**: API key protection via environment variables
- **Cross-Platform**: Works on Windows, Mac, and Linux
- **Professional Output**: High-quality PDF generation
- **Customizable**: Full control over page format and rendering
- **User-Friendly**: Clear error messages and guidance
- **Well-Documented**: Extensive documentation and examples

### Technical Details
- Python 3.8+ support
- Doppio API integration
- JSON-RPC based PDF rendering
- Automatic output directory creation
- Path handling with pathlib
- HTTP requests with timeout protection
- UTF-8 encoding support
- Virtual environment ready

### Documentation
- Complete API reference
- Step-by-step setup instructions
- Common use case examples
- Troubleshooting guide
- Best practices for HTML/CSS
- Security recommendations
- Pro tips for PDF optimization

## [Unreleased]

### Planned Features
- CLI interface with argument parsing
- Template variable substitution
- Custom headers and footers
- PDF encryption and password protection
- Merge multiple PDFs
- Progress bars for batch operations
- Web interface (Flask/Django)
- Docker support
- Automated testing suite
- More built-in templates
- PDF metadata customization
- Watermark support

---

## Version History

- **1.0.0** (2025-01-15) - Initial release with core features
- **0.1.0** (Development) - Pre-release development

---

## How to Read This Changelog

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

---

**Project**: HTML to PDF Generator  
**Repository**: Local Development  
**Maintainer**: Development Team  
**License**: MIT (or as specified)