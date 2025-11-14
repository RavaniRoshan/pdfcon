# content.io - Creative PDF Generator

An AI-powered creative workspace that transforms your ideas into professionally styled PDFs using natural language prompts. Perfect for LinkedIn content, blog posts, emails, and other professional content, content.io eliminates the confusion around creating styled, curated PDFs that align with your professional goals.

## 📋 Features

- **🤖 AI-Powered Content Creation**: Transform natural language prompts into structured, professional PDFs using Claude, OpenAI, or Gemini
- **🎨 Professional Styling**: Beautiful templates and professional formatting for all content types
- **📝 Dual Input Modes**: Prompt-to-PDF mode for AI assistance or Markdown mode for precise control
- **🔒 Secure & Private**: API key-based authentication with environment variable support
- **⚡ Instant Results**: Generate professional PDFs in seconds
- **📱 Responsive Interface**: Modern, user-friendly web interface optimized for all devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- AI API key (Claude, OpenAI, or Gemini)
- Doppio.sh API key for PDF generation

### Installation

1. **Clone or download this project**

2. **Navigate to the project directory**
   ```bash
   cd pdfcon
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API keys**

   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here  # or ANTHROPIC_API_KEY for Claude
   DOPPIO_API_KEY=your_doppio_api_key_here
   ```

   **Alternative**: Set the environment variables directly:

   - **Windows (Command Prompt)**:
     ```cmd
     set OPENAI_API_KEY=your_api_key_here
     set DOPPIO_API_KEY=your_api_key_here
     ```

   - **Windows (PowerShell)**:
     ```powershell
     $env:OPENAI_API_KEY="your_api_key_here"
     $env:DOPPIO_API_KEY="your_api_key_here"
     ```

   - **Linux/Mac**:
     ```bash
     export OPENAI_API_KEY=your_api_key_here
     export DOPPIO_API_KEY=your_api_key_here
     ```

### Usage

**Start the web application**:
```bash
cd web_app
python app.py
```

Access the interface at `http://localhost:5000`

**Basic API usage**:
```python
from src.generator import PDFGenerator

generator = PDFGenerator()
pdf_path = generator.generate_pdf(
    html_content="<h1>Your HTML Content</h1><p>Formatted professionally</p>",
    output_filename="my-document.pdf"
)
```

## 📁 Project Structure

```
pdfcon/
├── src/                    # Core generation logic
│   └── generator.py        # PDF generation utilities
├── web_app/               # Main web application
│   ├── app.py             # Flask application
│   ├── static/            # CSS, JavaScript, images
│   └── templates/         # HTML templates
├── output/                # Generated PDF files (created automatically)
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment configuration
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── agent.md              # Project documentation
```

## 🎨 Creative Use Cases

### LinkedIn Content PDFs
Transform your LinkedIn insights into professional, shareable PDFs that showcase your expertise.

### Blog Post Summaries
Create downloadable summaries of your blog posts for lead generation and content marketing.

### Professional Email Attachments
Generate polished document attachments that make your emails stand out.

### Educational Materials
Create curriculum materials, guides, and tutorials with professional formatting.

## 🔧 Web Interface Features

The content.io web interface includes:

- **Prompt-to-PDF Mode**: Describe what you want in natural language and let AI structure your content
- **Markdown Mode**: For precise control over formatting using markdown syntax
- **Real-time Validation**: Instant feedback on your content
- **Professional Styling**: Built-in templates for various content types
- **One-Click Generation**: Create and download PDFs instantly

### Example Prompt-to-PDF Usage:

```
Create a LinkedIn post summary PDF about AI in business:
- Professional header with title
- 3 key points about AI implementation
- Actionable insights 
- Clean, professional layout suitable for sharing
```

### Example Markdown Usage:

```markdown
# The Future of AI in Business

## Key Implementation Areas
- Customer Service Automation
- Data Analysis and Insights
- Process Optimization

## Success Metrics
- 35% reduction in response time
- 25% increase in customer satisfaction
- 20% cost savings in operations
```

## 🐛 Troubleshooting

### Error: "API key environment variable is not set"
**Solution**: Ensure your API keys are set in `.env` file or as environment variables.

### Error: "Web interface not loading"
**Solution**: Verify you're running the Flask app from the `web_app/` directory.

### Error: "PDF generation failed"
**Solution**: Check your Doppio.sh API key and internet connection.

### Error: "HTTP 401 Unauthorized"
**Solution**: Your API key is invalid. Check both AI and Doppio.sh API keys.

## 📝 Requirements

- **Python**: 3.8+
- **Dependencies**:
  - `Flask>=2.0.1` - Web framework
  - `requests>=2.31.0` - HTTP library for API calls
  - `markdown>=3.3.4` - Markdown processing
  - `python-dotenv>=1.0.0` - Environment variable management
  - `openai>=1.3.7` or `anthropic>=0.5.0` - AI service integration

## 🔐 Security Notes

- Never commit your `.env` file or expose your API keys
- The `.gitignore` file is configured to exclude sensitive files
- API keys should be treated as secrets
- All user data is processed securely

## 📄 License

This project is provided as-is for educational and commercial use. AI APIs and Doppio.sh API are subject to their own terms of service.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new creative templates
- Improve AI integration
- Enhance the user interface
- Report bugs or suggest enhancements
- Add features (batch processing, custom styling, etc.)

## 💡 Tips

1. **Be Specific in Your Prompts**: Detailed prompts generate better structured content
2. **Use Professional Tone**: Match your content tone to your target audience
3. **Preview Before Generating**: Review your content for alignment with goals
4. **Leverage Both Modes**: Use Prompt mode for creativity, Markdown for precision
5. **Test Different Outputs**: Experiment with different prompt styles for best results

---

**Transform your ideas into professional PDFs with content.io - Your all-in-one workspace for LinkedIn, blog, and email content.**