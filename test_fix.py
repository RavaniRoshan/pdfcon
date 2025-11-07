#!/usr/bin/env python3
"""
Quick Test Script - Verify Doppio API Fix
Tests the corrected Doppio API integration with a simple HTML example.
"""

import os
import sys
from pathlib import Path

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Add src to path
base_dir = Path(__file__).parent
sys.path.insert(0, str(base_dir / "src"))

from generator import PDFGenerator


def test_simple_html():
    """Test with a very simple HTML page."""
    print("=" * 70)
    print("TESTING DOPPIO API FIX")
    print("=" * 70)

    # Simple test HTML
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Test PDF</title>
    <style>
        body { font-family: Arial; margin: 2cm; }
        h1 { color: #2c3e50; }
    </style>
</head>
<body>
    <h1>Doppio API Test</h1>
    <p>This is a simple test to verify the API integration is working.</p>
    <ul>
        <li>Testing PDF generation</li>
        <li>Verifying API connection</li>
        <li>Checking base64 encoding</li>
    </ul>
</body>
</html>"""

    print("HTML to render:")
    print("-" * 40)
    print(html_content[:200] + "..." if len(html_content) > 200 else html_content)
    print("-" * 40)

    try:
        # Initialize generator
        print("\n🔍 Initializing PDF Generator...")
        generator = PDFGenerator()
        print("✅ Generator initialized successfully")

        # Test PDF generation
        print("\n🚀 Testing PDF generation...")
        output_path = generator.generate_pdf(
            html_content=html_content,
            output_filename="test_fix_output.pdf",
            page_format="A4",
            print_background=True,
        )

        print("\n" + "=" * 70)
        print("🎉 SUCCESS! Doppio API is working correctly!")
        print("=" * 70)
        print(f"✅ PDF generated: {output_path}")
        print(f"✅ File size: {output_path.stat().st_size:,} bytes")

        if output_path.stat().st_size > 1000:  # Should be at least 1KB for a valid PDF
            print("✅ File size looks reasonable for a PDF")
        else:
            print("⚠️  File size is very small - PDF might be empty")

        print("
📂 Check the 'output/' folder for your PDF!"        return True

    except Exception as e:
        print("\n" + "=" * 70)
        print("❌ TEST FAILED")
        print("=" * 70)
        print(f"Error: {str(e)}")

        print("\n🔍 TROUBLESHOOTING:")
        print("-" * 40)

        if "API key" in str(e).lower():
            print("• API key issue:")
            print("  1. Go to https://doppio.sh")
            print("  2. Sign up for free account")
            print("  3. Copy your API key")
            print("  4. Run: python set_api_key.py")
            print("  5. Or edit .env file manually")

        elif "timeout" in str(e).lower():
            print("• Network timeout:")
            print("  • Check internet connection")
            print("  • Try again in a moment")
            print("  • Doppio servers might be busy")

        elif "connection" in str(e).lower():
            print("• Network issue:")
            print("  • Check internet connection")
            print("  • Verify firewall/proxy settings")

        elif "400" in str(e):
            print("• Bad request (400):")
            print("  • API key format might be wrong")
            print("  • Check your .env file")

        elif "401" in str(e) or "unauthorized" in str(e).lower():
            print("• Unauthorized (401):")
            print("  • API key is invalid")
            print("  • Get new key from doppio.sh")

        else:
            print("• Unknown error:")
            print("  • Run: python check_setup.py")
            print("  • Check: FIX_API_KEY.md")

        return False


def main():
    """Run the test."""
    print("PDF GENERATOR - API FIX TEST")
    print("This script tests if the Doppio API integration is working.")
    print()

    success = test_simple_html()

    print("\n" + "=" * 70)
    if success:
        print("RESULT: ✅ TEST PASSED - API is working!")
        print("=" * 70)
        print("\n🎯 Next steps:")
        print("• Try the full template: python src/generator.py")
        print("• Run examples: python example_usage.py")
        print("• Batch process: python batch_convert.py")
    else:
        print("RESULT: ❌ TEST FAILED - Check errors above")
        print("=" * 70)
        print("\n🔧 Common fixes:")
        print("• Run: python set_api_key.py (or double-click set_api_key.bat)")
        print("• Run: python check_setup.py (for full diagnosis)")
        print("• Read: FIX_API_KEY.md (complete troubleshooting)")

    print("\n" + "=" * 70)
    input("Press Enter to exit...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest cancelled by user.")
        sys.exit(1)
