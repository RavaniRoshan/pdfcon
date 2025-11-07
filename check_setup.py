#!/usr/bin/env python3
"""
Setup Checker - Diagnoses and fixes common setup issues
Run this script first to check if everything is configured correctly.
"""

import os
import sys
from pathlib import Path


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def print_status(check_name, passed, message=""):
    """Print a check status."""
    status = "✅" if passed else "❌"
    print(f"{status} {check_name}")
    if message:
        print(f"   {message}")


def check_python_version():
    """Check if Python version is adequate."""
    print_header("Python Version Check")
    version = sys.version_info
    passed = version.major == 3 and version.minor >= 8

    print(f"   Python {version.major}.{version.minor}.{version.micro}")

    if passed:
        print_status("Python Version", True, "Python 3.8+ detected")
    else:
        print_status(
            "Python Version", False, "Need Python 3.8 or higher. Please upgrade!"
        )

    return passed


def check_dependencies():
    """Check if required packages are installed."""
    print_header("Dependencies Check")

    all_passed = True

    # Check requests
    try:
        import requests

        print_status("requests library", True, f"Version {requests.__version__}")
    except ImportError:
        print_status("requests library", False, "Run: pip install requests")
        all_passed = False

    # Check python-dotenv (optional but recommended)
    try:
        import dotenv

        print_status("python-dotenv", True, "Installed (recommended)")
    except ImportError:
        print_status(
            "python-dotenv",
            False,
            "Optional but recommended. Run: pip install python-dotenv",
        )

    return all_passed


def check_project_structure():
    """Check if project structure is correct."""
    print_header("Project Structure Check")

    base_dir = Path(__file__).parent
    all_passed = True

    # Check critical directories
    src_dir = base_dir / "src"
    if src_dir.exists():
        print_status("src/ directory", True, str(src_dir))
    else:
        print_status("src/ directory", False, "Missing!")
        all_passed = False

    output_dir = base_dir / "output"
    if output_dir.exists():
        print_status("output/ directory", True, str(output_dir))
    else:
        print_status("output/ directory", False, "Creating...")
        output_dir.mkdir(exist_ok=True)
        print_status("output/ directory", True, "Created successfully")

    # Check critical files
    generator_file = src_dir / "generator.py"
    if generator_file.exists():
        print_status("generator.py", True, "Found")
    else:
        print_status("generator.py", False, "Missing core file!")
        all_passed = False

    template_file = src_dir / "template.html"
    if template_file.exists():
        print_status("template.html", True, "Found")
    else:
        print_status("template.html", False, "Warning: No template found")

    return all_passed


def check_api_key():
    """Check if API key is configured."""
    print_header("API Key Configuration Check")

    base_dir = Path(__file__).parent
    env_file = base_dir / ".env"

    # Check if .env file exists
    if env_file.exists():
        print_status(".env file", True, str(env_file))

        # Try to read the API key
        try:
            with open(env_file, "r") as f:
                content = f.read()

            if "DOPPIO_API_KEY" in content:
                print_status(".env contains key", True, "DOPPIO_API_KEY found")

                # Check if it's still the placeholder
                if "your_api_key_here" in content:
                    print_status(
                        "API key set",
                        False,
                        "Still using placeholder! Update with real key.",
                    )
                    return False
                else:
                    # Try to get the actual key
                    for line in content.split("\n"):
                        if line.strip().startswith("DOPPIO_API_KEY"):
                            key_part = line.split("=", 1)[1].strip()
                            if key_part and len(key_part) > 10:
                                masked_key = key_part[:7] + "..." + key_part[-4:]
                                print_status("API key set", True, f"Key: {masked_key}")
                                return True
                            else:
                                print_status("API key set", False, "Key looks invalid")
                                return False
            else:
                print_status(
                    ".env contains key", False, "DOPPIO_API_KEY not found in .env file"
                )
                return False

        except Exception as e:
            print_status(".env readable", False, f"Error reading file: {e}")
            return False

    else:
        print_status(".env file", False, "Not found!")

        # Check if .env.example exists
        env_example = base_dir / ".env.example"
        if env_example.exists():
            print_status(".env.example", True, "Template found")
            print("\n   💡 Quick Fix:")
            print("      1. Copy .env.example to .env")
            print("      2. Edit .env and add your API key")
            print("      OR run: set_api_key.bat (Windows) / python3 set_api_key.py")

        return False


def check_environment_variable():
    """Check if API key is set as environment variable."""
    print_header("Environment Variable Check")

    api_key = os.getenv("DOPPIO_API_KEY")

    if api_key:
        if api_key == "your_api_key_here":
            print_status(
                "DOPPIO_API_KEY env var", False, "Set but using placeholder value"
            )
            return False
        else:
            masked_key = (
                api_key[:7] + "..." + api_key[-4:] if len(api_key) > 11 else "***"
            )
            print_status("DOPPIO_API_KEY env var", True, f"Set: {masked_key}")
            return True
    else:
        print_status("DOPPIO_API_KEY env var", False, "Not set in environment")
        return False


def provide_solutions():
    """Provide solutions for common issues."""
    print_header("How to Fix Issues")

    print("\n📋 SETUP CHECKLIST:")
    print("\n1. Install Dependencies:")
    print("   pip install -r requirements.txt")

    print("\n2. Get API Key:")
    print("   • Go to: https://doppio.sh")
    print("   • Sign up (FREE)")
    print("   • Copy your API key")

    print("\n3. Configure API Key (Choose ONE method):")
    print("\n   METHOD A - Automated Setup (EASIEST):")
    if os.name == "nt":
        print("      Double-click: set_api_key.bat")
    else:
        print("      Run: python3 set_api_key.py")

    print("\n   METHOD B - Manual .env file:")
    print("      1. Create file named: .env")
    print("      2. Add line: DOPPIO_API_KEY=your_actual_key")
    print("      3. Save in this folder")

    print("\n   METHOD C - Environment Variable:")
    if os.name == "nt":
        print("      Windows CMD: set DOPPIO_API_KEY=your_key")
        print('      PowerShell:  $env:DOPPIO_API_KEY="your_key"')
    else:
        print("      Terminal: export DOPPIO_API_KEY=your_key")

    print("\n4. Test Installation:")
    if os.name == "nt":
        print("   python src\\generator.py")
    else:
        print("   python3 src/generator.py")

    print("\n📚 HELP RESOURCES:")
    print("   • FIX_API_KEY.md - Complete troubleshooting guide")
    print("   • START_HERE.md - Quick start guide")
    print("   • README.md - Full documentation")


def test_pdf_generation():
    """Test if PDF generation works."""
    print_header("PDF Generation Test")

    try:
        # Add src to path
        base_dir = Path(__file__).parent
        src_dir = base_dir / "src"
        sys.path.insert(0, str(src_dir))

        # Try to import
        from generator import PDFGenerator

        print_status("Import generator", True, "Successfully imported")

        # Try to initialize (this will check API key)
        try:
            generator = PDFGenerator()
            print_status("Initialize generator", True, "API key loaded")

            # Check if template exists
            if (src_dir / "template.html").exists():
                print("\n   ✨ Everything looks good! Ready to generate PDFs!")
                print("\n   Try running:")
                if os.name == "nt":
                    print("      python src\\generator.py")
                else:
                    print("      python3 src/generator.py")
                return True
            else:
                print_status("Template check", False, "template.html not found")
                return False

        except EnvironmentError as e:
            print_status("Initialize generator", False, "API key not configured")
            return False

        except Exception as e:
            print_status("Initialize generator", False, str(e))
            return False

    except ImportError as e:
        print_status("Import generator", False, f"Cannot import: {e}")
        return False


def main():
    """Run all checks."""
    print("\n" + "🔍 " * 35)
    print("        PDF GENERATOR - SETUP DIAGNOSTIC TOOL")
    print("🔍 " * 35)

    print("\nThis tool will check if your environment is properly configured.")

    # Run all checks
    checks = {
        "Python Version": check_python_version(),
        "Dependencies": check_dependencies(),
        "Project Structure": check_project_structure(),
        "API Key (.env file)": check_api_key(),
        "API Key (environment)": check_environment_variable(),
    }

    # Summary
    print_header("Summary")

    passed = sum(1 for v in checks.values() if v)
    total = len(checks)

    print(f"\n   Checks Passed: {passed}/{total}")

    # Check if API key is configured in either way
    api_configured = checks["API Key (.env file)"] or checks["API Key (environment)"]

    if all(
        [
            checks["Python Version"],
            checks["Dependencies"],
            checks["Project Structure"],
            api_configured,
        ]
    ):
        print("\n   ✅ All essential checks passed!")
        test_pdf_generation()
    else:
        print("\n   ❌ Some checks failed. See solutions below:")
        provide_solutions()

    print("\n" + "=" * 70)
    print("\nFor detailed help, see:")
    print("  • FIX_API_KEY.md")
    print("  • START_HERE.md")
    print("  • README.md")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    try:
        main()
        input("\nPress Enter to exit...")
    except KeyboardInterrupt:
        print("\n\nDiagnostic cancelled.")
        sys.exit(1)
