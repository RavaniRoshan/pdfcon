#!/usr/bin/env python3
"""
Batch PDF Generator
Converts multiple HTML files to PDF in one operation.
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # python-dotenv not installed, will use system environment variables only
    pass

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))
from generator import PDFGenerator


class BatchPDFGenerator:
    """Handles batch conversion of HTML files to PDF."""

    def __init__(self):
        """Initialize the batch generator."""
        self.generator = PDFGenerator()
        self.base_dir = Path(__file__).parent
        self.src_dir = self.base_dir / "src"
        self.output_dir = self.base_dir / "output"
        self.success_count = 0
        self.failure_count = 0
        self.results = []

    def find_html_files(self, directory: Path = None) -> List[Path]:
        """
        Find all HTML files in a directory.

        Args:
            directory: Directory to search (defaults to src/)

        Returns:
            List of HTML file paths
        """
        if directory is None:
            directory = self.src_dir

        html_files = list(directory.glob("*.html"))
        return sorted(html_files)

    def convert_file(
        self, html_file: Path, output_name: str = None, **kwargs
    ) -> Tuple[bool, str]:
        """
        Convert a single HTML file to PDF.

        Args:
            html_file: Path to HTML file
            output_name: Optional custom output filename
            **kwargs: Additional arguments for PDF generation

        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            # Generate output filename
            if output_name is None:
                output_name = html_file.stem + ".pdf"

            print(f"\n📄 Processing: {html_file.name}")

            # Read HTML content
            with open(html_file, "r", encoding="utf-8") as f:
                html_content = f.read()

            # Generate PDF
            output_path = self.generator.generate_pdf(
                html_content=html_content, output_filename=output_name, **kwargs
            )

            self.success_count += 1
            message = f"✅ Success → {output_path.name}"
            return True, message

        except Exception as e:
            self.failure_count += 1
            message = f"❌ Failed: {str(e)}"
            return False, message

    def batch_convert(
        self, html_files: List[Path] = None, **kwargs
    ) -> List[Tuple[str, bool, str]]:
        """
        Convert multiple HTML files to PDF.

        Args:
            html_files: List of HTML files to convert (defaults to all in src/)
            **kwargs: Additional arguments for PDF generation

        Returns:
            List of tuples (filename, success, message)
        """
        if html_files is None:
            html_files = self.find_html_files()

        if not html_files:
            print("⚠️  No HTML files found to convert")
            return []

        print(f"\n🚀 Starting batch conversion of {len(html_files)} file(s)...")
        print("=" * 70)

        results = []

        for html_file in html_files:
            success, message = self.convert_file(html_file, **kwargs)
            results.append((html_file.name, success, message))
            self.results.append((html_file.name, success, message))
            print(f"   {message}")

        return results

    def print_summary(self):
        """Print conversion summary."""
        print("\n" + "=" * 70)
        print("BATCH CONVERSION SUMMARY")
        print("=" * 70)
        print(f"Total files processed: {self.success_count + self.failure_count}")
        print(f"✅ Successful: {self.success_count}")
        print(f"❌ Failed: {self.failure_count}")

        if self.failure_count > 0:
            print("\nFailed conversions:")
            for filename, success, message in self.results:
                if not success:
                    print(f"  - {filename}: {message}")

        print("=" * 70)


def convert_specific_files(filenames: List[str], **kwargs):
    """
    Convert specific HTML files by name.

    Args:
        filenames: List of HTML filenames to convert
        **kwargs: Additional PDF generation options
    """
    batch_gen = BatchPDFGenerator()
    src_dir = batch_gen.src_dir

    html_files = []
    for filename in filenames:
        file_path = src_dir / filename
        if file_path.exists():
            html_files.append(file_path)
        else:
            print(f"⚠️  File not found: {filename}")

    if html_files:
        batch_gen.batch_convert(html_files, **kwargs)
        batch_gen.print_summary()


def convert_all_in_directory(directory: str = None, **kwargs):
    """
    Convert all HTML files in a directory.

    Args:
        directory: Directory path (defaults to src/)
        **kwargs: Additional PDF generation options
    """
    batch_gen = BatchPDFGenerator()

    if directory:
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"❌ Directory not found: {directory}")
            return
        html_files = batch_gen.find_html_files(dir_path)
    else:
        html_files = batch_gen.find_html_files()

    if html_files:
        print(f"Found {len(html_files)} HTML file(s):")
        for f in html_files:
            print(f"  - {f.name}")

        batch_gen.batch_convert(html_files, **kwargs)
        batch_gen.print_summary()
    else:
        print("⚠️  No HTML files found")


def main():
    """Main entry point for batch conversion."""
    print("\n" + "=" * 70)
    print("BATCH PDF GENERATOR")
    print("=" * 70)

    # Check for API key
    if not os.getenv("DOPPIO_API_KEY"):
        print("\n❌ Error: DOPPIO_API_KEY not set")
        print("   Set it in .env file or as environment variable")
        print("   Sign up at: https://doppio.sh")
        return 1

    # Check command line arguments
    if len(sys.argv) > 1:
        # Convert specific files
        filenames = sys.argv[1:]
        print(f"\nConverting {len(filenames)} specified file(s)...")
        convert_specific_files(filenames)
    else:
        # Convert all HTML files in src/
        print("\nConverting all HTML files in src/ directory...")
        convert_all_in_directory()

    return 0


# Example usage patterns
def example_custom_batch():
    """Example: Custom batch conversion with specific options."""
    batch_gen = BatchPDFGenerator()

    # Find all HTML files
    html_files = batch_gen.find_html_files()

    # Convert with custom options
    batch_gen.batch_convert(
        html_files, page_format="Letter", print_background=True, wait_for="load"
    )

    batch_gen.print_summary()


def example_selective_conversion():
    """Example: Convert only specific files."""
    filenames = ["template.html", "custom-doc.html"]
    convert_specific_files(filenames, page_format="A4")


if __name__ == "__main__":
    # Usage:
    #   python batch_convert.py                    # Convert all HTML in src/
    #   python batch_convert.py file1.html file2.html  # Convert specific files

    sys.exit(main())
