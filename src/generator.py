#!/usr/bin/env python3
"""
HTML to PDF Generator using Doppio API
Converts HTML templates to professionally formatted PDF documents.
"""

import os
import sys
import requests
import base64
from pathlib import Path
from typing import Optional

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # python-dotenv not installed, will use system environment variables only
    pass


class PDFGenerator:
    """Handles PDF generation using the Doppio API."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the PDF generator.

        Args:
            api_key: Doppio API key. If None, reads from DOPPIO_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("DOPPIO_API_KEY")
        if not self.api_key:
            raise EnvironmentError(
                "DOPPIO_API_KEY environment variable is not set.\n"
                "Please set your API key or sign up for free at https://doppio.sh\n\n"
                "Quick Fix:\n"
                "  1. Get free API key: https://doppio.sh\n"
                "  2. Windows: Run set_api_key.bat\n"
                "     Mac/Linux: Run python3 set_api_key.py\n"
                "  3. Or see FIX_API_KEY.md for detailed help"
            )

        self.api_url = "https://api.doppio.sh/v1/render/pdf/direct"
        self.base_dir = Path(__file__).parent.parent
        self.template_dir = self.base_dir / "src"
        self.output_dir = self.base_dir / "output"

        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)

    def load_html_template(self, template_name: str = "template.html") -> str:
        """
        Load HTML content from a template file.

        Args:
            template_name: Name of the template file to load.

        Returns:
            HTML content as a string.

        Raises:
            FileNotFoundError: If template file doesn't exist.
        """
        template_path = self.template_dir / template_name

        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()

    def generate_pdf(
        self,
        html_content: str,
        output_filename: str = "output.pdf",
        page_format: str = "A4",
        print_background: bool = True,
        wait_for: str = "networkidle0",
    ) -> Path:
        """
        Generate a PDF from HTML content using Doppio API.

        Args:
            html_content: HTML content to convert.
            output_filename: Name of the output PDF file.
            page_format: Page format (A4, Letter, etc.).
            print_background: Whether to print background graphics.
            wait_for: Wait condition before rendering (networkidle0, load, domcontentloaded).

        Returns:
            Path to the generated PDF file.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        output_path = self.output_dir / output_filename

        print(f"🚀 Sending HTML to Doppio.sh for PDF rendering...")
        print(f"   Format: {page_format}")
        print(f"   Output: {output_path}")
        print(f"   HTML size: {len(html_content):,} characters")

        try:
            # Encode HTML as base64 for Doppio API
            encoded_html = base64.b64encode(html_content.encode("utf-8")).decode(
                "utf-8"
            )

            response = requests.post(
                self.api_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "page": {
                        "pdf": {
                            "printBackground": print_background,
                            "format": page_format,
                        },
                        "setContent": {"html": encoded_html},
                    }
                },
                timeout=60,
            )

            # Check if response is successful
            if response.status_code == 200:
                # Doppio direct render returns raw PDF binary on success
                if len(response.content) > 0:
                    # Save PDF content
                    with open(output_path, "wb") as f:
                        f.write(response.content)

                    file_size = output_path.stat().st_size / 1024  # KB
                    print(f"✅ Success! PDF generated ({file_size:.1f} KB)")
                    print(f"   Saved to: {output_path}")

                    return output_path
                else:
                    print("❌ Error: Empty response from Doppio API")
                    raise Exception("Empty response from API")
            else:
                # Handle error responses
                try:
                    # Try to parse JSON error response
                    error_data = response.json()
                    print(f"❌ Error: HTTP {response.status_code}")
                    print(f"   Message: {error_data.get('message', 'Unknown error')}")
                    if "error" in error_data:
                        print(f"   Error: {error_data['error']}")
                except:
                    # If not JSON, show text response
                    print(f"❌ Error: HTTP {response.status_code}")
                    print(f"   Response: {response.text[:500]}")  # Limit output length

                raise Exception(f"Doppio API error: HTTP {response.status_code}")

        except requests.exceptions.Timeout:
            print("❌ Error: Request timed out after 60 seconds")
            raise
        except requests.exceptions.ConnectionError:
            print("❌ Error: Could not connect to Doppio API")
            print("   Check your internet connection")
            raise
        except requests.exceptions.RequestException as e:
            print(f"❌ Error: Request failed: {str(e)}")
            raise
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            raise

    def generate_from_template(
        self,
        template_name: str = "template.html",
        output_filename: str = "output.pdf",
        **kwargs,
    ) -> Path:
        """
        Generate PDF from a template file.

        Args:
            template_name: Name of the template file.
            output_filename: Name of the output PDF file.
            **kwargs: Additional arguments passed to generate_pdf().

        Returns:
            Path to the generated PDF file.
        """
        print(f"📄 Loading template: {template_name}")
        html_content = self.load_html_template(template_name)

        return self.generate_pdf(html_content, output_filename, **kwargs)


def main():
    """Main entry point for the script."""
    try:
        # Initialize generator
        generator = PDFGenerator()

        # Generate PDF from template
        output_path = generator.generate_from_template(
            template_name="template.html",
            output_filename="acp-101-guide.pdf",
            page_format="A4",
            print_background=True,
        )

        print(f"\n🎉 PDF generation complete!")
        print(f"   Open: {output_path.absolute()}")

        return 0

    except EnvironmentError as e:
        print(f"\n⚠️  Configuration Error:")
        print(f"   {str(e)}")
        return 1
    except FileNotFoundError as e:
        print(f"\n⚠️  File Error:")
        print(f"   {str(e)}")
        return 1
    except Exception as e:
        print(f"\n❌ Generation failed:")
        print(f"   {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
