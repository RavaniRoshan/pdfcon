#!/usr/bin/env python3
"""
API Key Setup Helper
This script helps you set up your Doppio API key easily.
"""

import os
from pathlib import Path


def main():
    print("=" * 70)
    print("API KEY SETUP HELPER")
    print("=" * 70)
    print()

    # Get the project directory
    project_dir = Path(__file__).parent
    env_file = project_dir / ".env"
    env_example = project_dir / ".env.example"

    print("📝 Setting up your Doppio API key...")
    print()

    # Step 1: Check if .env already exists
    if env_file.exists():
        print("⚠️  .env file already exists!")
        print(f"   Location: {env_file}")
        print()
        response = input("Do you want to update it? (y/n): ").strip().lower()
        if response != "y":
            print("Cancelled. No changes made.")
            return

    # Step 2: Get API key from user
    print()
    print("=" * 70)
    print("GET YOUR API KEY")
    print("=" * 70)
    print()
    print("1. Go to: https://doppio.sh")
    print("2. Sign up for a FREE account")
    print("3. Copy your API key (starts with 'dp_')")
    print()
    print("-" * 70)

    api_key = input("\nPaste your API key here: ").strip()

    if not api_key:
        print()
        print("❌ No API key provided. Setup cancelled.")
        return

    # Validate key format
    if not api_key.startswith("dp_") and not api_key.startswith("test_"):
        print()
        print("⚠️  WARNING: Your API key doesn't look like a Doppio key")
        print("   (Doppio keys usually start with 'dp_')")
        print()
        response = input("Continue anyway? (y/n): ").strip().lower()
        if response != "y":
            print("Cancelled.")
            return

    # Step 3: Create .env file
    env_content = f"""# Doppio API Configuration
# Sign up for a free API key at: https://doppio.sh

# Your Doppio API Key
DOPPIO_API_KEY={api_key}
"""

    try:
        with open(env_file, "w", encoding="utf-8") as f:
            f.write(env_content)

        print()
        print("=" * 70)
        print("✅ SUCCESS!")
        print("=" * 70)
        print()
        print(f"✓ Created: {env_file}")
        print("✓ API key saved securely")
        print()
        print("=" * 70)
        print("NEXT STEPS")
        print("=" * 70)
        print()
        print("You're ready to generate PDFs! Try these commands:")
        print()

        if os.name == "nt":  # Windows
            print("  python src\\generator.py           # Generate from template")
            print("  python example_usage.py           # Try 5 examples")
            print("  python batch_convert.py           # Batch convert HTML files")
        else:  # Mac/Linux
            print("  python3 src/generator.py          # Generate from template")
            print("  python3 example_usage.py          # Try 5 examples")
            print("  python3 batch_convert.py          # Batch convert HTML files")

        print()
        print("📂 PDFs will be saved in: output/")
        print()
        print("🎉 Happy PDF generating!")
        print("=" * 70)

    except Exception as e:
        print()
        print(f"❌ Error creating .env file: {str(e)}")
        print()
        print("Manual setup instructions:")
        print("-" * 70)
        print("1. Create a file named '.env' in this directory")
        print("2. Add this line to the file:")
        print(f"   DOPPIO_API_KEY={api_key}")
        print("3. Save and close the file")
        return 1

    return 0


if __name__ == "__main__":
    try:
        exit_code = main()
        input("\nPress Enter to exit...")
        exit(exit_code if exit_code else 0)
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        exit(1)
