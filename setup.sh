#!/bin/bash
# HTML to PDF Generator - Unix/Linux/Mac Setup Script
# This script sets up the project environment

set -e  # Exit on error

echo "============================================================"
echo "HTML to PDF Generator - Setup"
echo "============================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR]${NC} Python 3 is not installed"
    echo "Please install Python 3.8+ from your package manager:"
    echo "  - Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  - macOS: brew install python3"
    echo "  - Fedora: sudo dnf install python3"
    exit 1
fi

echo -e "${GREEN}[OK]${NC} Python is installed"
python3 --version
echo ""

# Check if pip is available
if ! command -v pip3 &> /dev/null && ! python3 -m pip --version &> /dev/null; then
    echo -e "${RED}[ERROR]${NC} pip is not available"
    echo "Please install pip for Python 3"
    exit 1
fi

echo -e "${GREEN}[OK]${NC} pip is available"
echo ""

# Create virtual environment (optional but recommended)
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}[OK]${NC} Virtual environment created"
    echo ""
fi

# Activate virtual environment
if [ -f "venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
    echo -e "${GREEN}[OK]${NC} Virtual environment activated"
    echo ""
fi

# Upgrade pip
echo "Upgrading pip..."
python3 -m pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing dependencies..."
echo "============================================================"
if [ -f "requirements.txt" ]; then
    python3 -m pip install -r requirements.txt
    echo ""
    echo -e "${GREEN}[OK]${NC} Dependencies installed successfully"
else
    echo -e "${RED}[ERROR]${NC} requirements.txt not found"
    exit 1
fi

echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo ""
        echo -e "${YELLOW}[IMPORTANT]${NC} Please edit .env file and add your Doppio API key"
        echo "1. Open .env file in a text editor: nano .env"
        echo "2. Replace 'your_api_key_here' with your actual API key"
        echo "3. Get a free API key at: https://doppio.sh"
        echo ""
    else
        echo -e "${RED}[ERROR]${NC} .env.example not found"
        exit 1
    fi
else
    echo -e "${GREEN}[OK]${NC} .env file already exists"
    echo ""
fi

# Ensure output directory exists
if [ ! -d "output" ]; then
    mkdir -p output
    echo -e "${GREEN}[OK]${NC} Created output directory"
else
    echo -e "${GREEN}[OK]${NC} output directory exists"
fi
echo ""

# Make scripts executable
if [ -f "src/generator.py" ]; then
    chmod +x src/generator.py
fi
if [ -f "example_usage.py" ]; then
    chmod +x example_usage.py
fi
if [ -f "batch_convert.py" ]; then
    chmod +x batch_convert.py
fi

echo "============================================================"
echo "Setup Complete!"
echo "============================================================"
echo ""
echo "Next steps:"
echo ""
echo "1. Edit .env file and add your DOPPIO_API_KEY"
echo "   Get a free key at: https://doppio.sh"
echo "   Edit command: nano .env"
echo ""
echo "2. Activate virtual environment (if not already active):"
echo "   source venv/bin/activate"
echo ""
echo "3. Run the generator:"
echo "   python3 src/generator.py"
echo ""
echo "4. Check examples:"
echo "   python3 example_usage.py"
echo ""
echo "5. Batch convert all HTML files:"
echo "   python3 batch_convert.py"
echo ""
echo "Generated PDFs will be saved in the 'output' folder"
echo "============================================================"
echo ""

# Check if .env has the default placeholder
if grep -q "your_api_key_here" .env 2>/dev/null; then
    echo -e "${YELLOW}⚠️  WARNING:${NC} Don't forget to update your API key in .env file!"
    echo ""
fi
