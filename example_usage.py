#!/usr/bin/env python3
"""
Example Usage Script for PDF Generator
Demonstrates various ways to use the PDFGenerator class.
"""

import os
from pathlib import Path

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # python-dotenv not installed, will use system environment variables only
    pass

# Import the generator
import sys

sys.path.insert(0, str(Path(__file__).parent / "src"))
from generator import PDFGenerator


def example_1_basic_usage():
    """Example 1: Basic usage with default template."""
    print("\n" + "=" * 60)
    print("Example 1: Basic Usage")
    print("=" * 60)

    generator = PDFGenerator()
    output_path = generator.generate_from_template(
        template_name="template.html", output_filename="example1_basic.pdf"
    )
    print(f"✓ Generated: {output_path}")


def example_2_custom_html():
    """Example 2: Generate PDF from custom HTML string."""
    print("\n" + "=" * 60)
    print("Example 2: Custom HTML String")
    print("=" * 60)

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Custom Document</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 2cm;
                line-height: 1.6;
            }
            h1 {
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }
            .highlight {
                background-color: #fff3cd;
                padding: 15px;
                border-left: 4px solid #ffc107;
                margin: 20px 0;
            }
            code {
                background-color: #f4f4f4;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }
        </style>
    </head>
    <body>
        <h1>Custom HTML to PDF Example</h1>
        <p>This PDF was generated from a custom HTML string.</p>

        <div class="highlight">
            <strong>Note:</strong> You can use any HTML and CSS to style your documents!
        </div>

        <h2>Features</h2>
        <ul>
            <li>Full HTML5 support</li>
            <li>CSS styling with <code>@media print</code></li>
            <li>Web fonts and custom typography</li>
            <li>Images and SVG graphics</li>
        </ul>

        <h2>Code Example</h2>
        <pre><code>def hello_world():
    print("Hello from PDF!")
    return True</code></pre>
    </body>
    </html>
    """

    generator = PDFGenerator()
    output_path = generator.generate_pdf(
        html_content=html_content, output_filename="example2_custom_html.pdf"
    )
    print(f"✓ Generated: {output_path}")


def example_3_different_formats():
    """Example 3: Generate PDFs in different page formats."""
    print("\n" + "=" * 60)
    print("Example 3: Different Page Formats")
    print("=" * 60)

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 2cm;
                font-family: Arial;
            }
            h1 { color: #e74c3c; }
        </style>
    </head>
    <body>
        <h1>Page Format Test</h1>
        <p>This document demonstrates different page sizes.</p>
    </body>
    </html>
    """

    generator = PDFGenerator()

    formats = ["A4", "Letter", "Legal", "A5"]

    for fmt in formats:
        output_path = generator.generate_pdf(
            html_content=html,
            output_filename=f"example3_{fmt.lower()}.pdf",
            page_format=fmt,
        )
        print(f"✓ Generated {fmt}: {output_path.name}")


def example_4_invoice_template():
    """Example 4: Generate a professional invoice."""
    print("\n" + "=" * 60)
    print("Example 4: Invoice Template")
    print("=" * 60)

    invoice_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Invoice</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                padding: 20mm;
                color: #333;
            }
            .header {
                display: flex;
                justify-content: space-between;
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 3px solid #2c3e50;
            }
            .company-name {
                font-size: 28px;
                font-weight: bold;
                color: #2c3e50;
            }
            .invoice-title {
                font-size: 24px;
                color: #7f8c8d;
                text-align: right;
            }
            .info-section {
                margin: 20px 0;
            }
            .info-label {
                font-weight: bold;
                color: #2c3e50;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 30px 0;
            }
            th {
                background-color: #2c3e50;
                color: white;
                padding: 12px;
                text-align: left;
            }
            td {
                padding: 10px 12px;
                border-bottom: 1px solid #ddd;
            }
            .total-row {
                background-color: #ecf0f1;
                font-weight: bold;
                font-size: 18px;
            }
            .footer {
                margin-top: 50px;
                padding-top: 20px;
                border-top: 1px solid #ddd;
                text-align: center;
                color: #7f8c8d;
                font-size: 12px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <div>
                <div class="company-name">ACME Corporation</div>
                <p>123 Business Street<br>New York, NY 10001<br>Phone: (555) 123-4567</p>
            </div>
            <div class="invoice-title">INVOICE</div>
        </div>

        <div class="info-section">
            <p><span class="info-label">Invoice #:</span> INV-2025-001</p>
            <p><span class="info-label">Date:</span> January 15, 2025</p>
            <p><span class="info-label">Due Date:</span> February 15, 2025</p>
        </div>

        <div class="info-section">
            <p class="info-label">Bill To:</p>
            <p>John Smith<br>456 Client Avenue<br>Los Angeles, CA 90001</p>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Description</th>
                    <th style="text-align: right;">Quantity</th>
                    <th style="text-align: right;">Unit Price</th>
                    <th style="text-align: right;">Total</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Web Development Services</td>
                    <td style="text-align: right;">40 hrs</td>
                    <td style="text-align: right;">$150.00</td>
                    <td style="text-align: right;">$6,000.00</td>
                </tr>
                <tr>
                    <td>UI/UX Design</td>
                    <td style="text-align: right;">20 hrs</td>
                    <td style="text-align: right;">$100.00</td>
                    <td style="text-align: right;">$2,000.00</td>
                </tr>
                <tr>
                    <td>API Integration</td>
                    <td style="text-align: right;">15 hrs</td>
                    <td style="text-align: right;">$150.00</td>
                    <td style="text-align: right;">$2,250.00</td>
                </tr>
                <tr class="total-row">
                    <td colspan="3" style="text-align: right;">TOTAL DUE:</td>
                    <td style="text-align: right;">$10,250.00</td>
                </tr>
            </tbody>
        </table>

        <div class="footer">
            <p>Thank you for your business!</p>
            <p>Payment terms: Net 30 days | Bank Transfer or Check</p>
        </div>
    </body>
    </html>
    """

    generator = PDFGenerator()
    output_path = generator.generate_pdf(
        html_content=invoice_html, output_filename="example4_invoice.pdf"
    )
    print(f"✓ Generated: {output_path}")


def example_5_resume():
    """Example 5: Generate a professional resume."""
    print("\n" + "=" * 60)
    print("Example 5: Professional Resume")
    print("=" * 60)

    resume_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Resume</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Helvetica', Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }
            .container { max-width: 800px; margin: 0 auto; padding: 20mm; }
            .header {
                text-align: center;
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 2px solid #2c3e50;
            }
            .name {
                font-size: 32px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 5px;
            }
            .contact {
                color: #7f8c8d;
                font-size: 14px;
            }
            .section {
                margin: 25px 0;
            }
            .section-title {
                font-size: 20px;
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 5px;
                margin-bottom: 15px;
                font-weight: bold;
            }
            .job-title {
                font-weight: bold;
                color: #2c3e50;
                font-size: 16px;
            }
            .company {
                color: #3498db;
                font-style: italic;
            }
            .date {
                color: #7f8c8d;
                font-size: 14px;
            }
            .description {
                margin: 10px 0 20px 20px;
            }
            ul { margin-left: 20px; }
            li { margin: 5px 0; }
            .skills {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }
            .skill-tag {
                background-color: #ecf0f1;
                padding: 5px 15px;
                border-radius: 15px;
                font-size: 14px;
                color: #2c3e50;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="name">JANE DOE</div>
                <div class="contact">
                    Email: jane.doe@email.com | Phone: (555) 987-6543 | LinkedIn: linkedin.com/in/janedoe
                </div>
            </div>

            <div class="section">
                <div class="section-title">PROFESSIONAL SUMMARY</div>
                <p>Results-driven Software Engineer with 5+ years of experience in full-stack development.
                Expertise in building scalable web applications and leading cross-functional teams.
                Passionate about clean code and innovative solutions.</p>
            </div>

            <div class="section">
                <div class="section-title">EXPERIENCE</div>

                <div class="job-title">Senior Software Engineer</div>
                <div class="company">Tech Innovations Inc.</div>
                <div class="date">Jan 2022 - Present</div>
                <div class="description">
                    <ul>
                        <li>Led development of microservices architecture serving 1M+ users</li>
                        <li>Improved application performance by 40% through optimization</li>
                        <li>Mentored junior developers and conducted code reviews</li>
                    </ul>
                </div>

                <div class="job-title">Software Engineer</div>
                <div class="company">StartUp Solutions</div>
                <div class="date">Jun 2019 - Dec 2021</div>
                <div class="description">
                    <ul>
                        <li>Built RESTful APIs using Python/Django and Node.js</li>
                        <li>Implemented CI/CD pipelines reducing deployment time by 60%</li>
                        <li>Collaborated with UX team to deliver responsive web applications</li>
                    </ul>
                </div>
            </div>

            <div class="section">
                <div class="section-title">EDUCATION</div>
                <div class="job-title">Bachelor of Science in Computer Science</div>
                <div class="company">University of Technology</div>
                <div class="date">2015 - 2019</div>
            </div>

            <div class="section">
                <div class="section-title">SKILLS</div>
                <div class="skills">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">JavaScript</span>
                    <span class="skill-tag">React</span>
                    <span class="skill-tag">Node.js</span>
                    <span class="skill-tag">Docker</span>
                    <span class="skill-tag">AWS</span>
                    <span class="skill-tag">PostgreSQL</span>
                    <span class="skill-tag">Git</span>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    generator = PDFGenerator()
    output_path = generator.generate_pdf(
        html_content=resume_html, output_filename="example5_resume.pdf"
    )
    print(f"✓ Generated: {output_path}")


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("PDF GENERATOR - EXAMPLE USAGE")
    print("=" * 60)

    try:
        # Check if API key is set
        if not os.getenv("DOPPIO_API_KEY"):
            print("\n⚠️  WARNING: DOPPIO_API_KEY not found!")
            print("   Please set it in .env file or environment variable")
            print("   Sign up at: https://doppio.sh")
            return 1

        # Run examples
        example_1_basic_usage()
        example_2_custom_html()
        example_3_different_formats()
        example_4_invoice_template()
        example_5_resume()

        print("\n" + "=" * 60)
        print("✅ All examples completed successfully!")
        print("=" * 60)
        print(f"\nCheck the 'output/' directory for generated PDFs")

        return 0

    except Exception as e:
        print(f"\n❌ Error running examples: {str(e)}")
        return 1


if __name__ == "__main__":
    import sys

    sys.exit(main())
