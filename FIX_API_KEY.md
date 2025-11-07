# 🔧 FIX: API Key Error - Complete Guide

## ❌ Error You're Seeing

```
Configuration Error:
   DOPPIO_API_KEY environment variable is not set.
```

---

## ✅ SOLUTION (Choose Your Method)

### 🚀 **METHOD 1: Quick Setup (Easiest - Recommended)**

#### Windows
1. **Double-click** `set_api_key.bat` (or run in Command Prompt)
2. **Follow the prompts** to enter your API key
3. **Done!** Try running your script again

#### Mac/Linux
```bash
python3 set_api_key.py
```

---

### 📝 **METHOD 2: Manual Setup**

#### Step 1: Get Your API Key
1. Go to **https://doppio.sh**
2. Click **"Sign Up"** or **"Get Started"**
3. Create a free account
4. **Copy your API key** (looks like: `dp_xxxxxxxxxxxxx`)

#### Step 2: Create .env File

**Windows (Notepad):**
1. Open Notepad
2. Type this (replace with YOUR key):
   ```
   DOPPIO_API_KEY=dp_your_actual_key_here
   ```
3. Save as: `.env` (include the dot!)
4. Save location: Inside the `pdfcon` folder
5. File type: **All Files** (not .txt!)

**Mac/Linux (Terminal):**
```bash
cd pdfcon
echo "DOPPIO_API_KEY=dp_your_actual_key_here" > .env
```

**Or use nano editor:**
```bash
cd pdfcon
nano .env
```
Then type:
```
DOPPIO_API_KEY=dp_your_actual_key_here
```
Press `Ctrl+X`, then `Y`, then `Enter` to save.

---

### 💻 **METHOD 3: Set Environment Variable (Temporary)**

This sets the key for your current terminal session only.

#### Windows (Command Prompt)
```cmd
set DOPPIO_API_KEY=dp_your_actual_key_here
python src\generator.py
```

#### Windows (PowerShell)
```powershell
$env:DOPPIO_API_KEY="dp_your_actual_key_here"
python src\generator.py
```

#### Mac/Linux
```bash
export DOPPIO_API_KEY=dp_your_actual_key_here
python3 src/generator.py
```

**Note**: You'll need to do this every time you open a new terminal.

---

### 🔐 **METHOD 4: Set System Environment Variable (Permanent)**

#### Windows (GUI Method)
1. Press `Win + R`
2. Type: `sysdm.cpl` and press Enter
3. Go to **Advanced** tab
4. Click **Environment Variables**
5. Under **User variables**, click **New**
6. Variable name: `DOPPIO_API_KEY`
7. Variable value: `dp_your_actual_key_here`
8. Click **OK** on all windows
9. **Restart** Command Prompt/PowerShell
10. Run your script

#### Mac/Linux (Permanent)
Add to your shell profile:

**For bash (~/.bashrc or ~/.bash_profile):**
```bash
echo 'export DOPPIO_API_KEY=dp_your_actual_key_here' >> ~/.bashrc
source ~/.bashrc
```

**For zsh (~/.zshrc):**
```bash
echo 'export DOPPIO_API_KEY=dp_your_actual_key_here' >> ~/.zshrc
source ~/.zshrc
```

---

## 🔍 Verify It's Working

After setting up, test with:

**Windows:**
```cmd
python src\generator.py
```

**Mac/Linux:**
```bash
python3 src/generator.py
```

You should see:
```
🚀 Sending HTML to Doppio.sh for PDF rendering...
✅ Success! PDF generated...
```

---

## 🐛 Still Not Working?

### Check #1: Is .env File Created?

**Windows:**
```cmd
dir .env
```

**Mac/Linux:**
```bash
ls -la .env
```

Should show the file exists. If not, it wasn't created properly.

### Check #2: Is the Key in .env?

**Windows:**
```cmd
type .env
```

**Mac/Linux:**
```bash
cat .env
```

Should show:
```
DOPPIO_API_KEY=dp_xxxxxxxxxxxxx
```

### Check #3: File Location

Make sure `.env` is in the **pdfcon** folder, not inside `src/` or `output/`.

```
pdfcon/
├── .env          ← Should be HERE
├── src/
│   └── generator.py
└── output/
```

### Check #4: File Name is Correct

Common mistakes:
- ❌ `env` (missing the dot)
- ❌ `.env.txt` (has .txt extension)
- ❌ `.env.example` (that's the template, not the real file)
- ✅ `.env` (correct!)

**Windows users**: Make sure "Hide extensions for known file types" is OFF in File Explorer.

### Check #5: API Key is Valid

Your key should:
- Start with `dp_` (usually)
- Be long (20+ characters)
- Have no spaces before/after
- Be on a NEW Doppio account (free tier available)

### Check #6: Restart Terminal

After creating `.env`:
1. Close your terminal/command prompt
2. Open a new one
3. Navigate back to the project folder
4. Try again

---

## 🆘 Emergency Workaround

If nothing else works, edit the Python file directly (NOT RECOMMENDED for production):

1. Open `src/generator.py` in a text editor
2. Find line ~24 that says:
   ```python
   self.api_key = api_key or os.getenv("DOPPIO_API_KEY")
   ```
3. Change it to:
   ```python
   self.api_key = api_key or os.getenv("DOPPIO_API_KEY") or "dp_your_actual_key_here"
   ```
4. Save the file
5. Run your script

**⚠️ WARNING**: This hardcodes your API key in the source code. Don't commit this to Git!

---

## 📞 Get Help

If you're still stuck:

1. **Check file location again**:
   - Run: `python set_api_key.py` (easier setup)

2. **Verify you have a valid Doppio account**:
   - Go to https://doppio.sh
   - Log in
   - Copy your API key again

3. **Try the temporary method first**:
   ```cmd
   # Windows
   set DOPPIO_API_KEY=dp_your_key
   python src\generator.py
   ```
   If this works, the issue is with your `.env` file.

4. **Check if python-dotenv is installed**:
   ```bash
   pip list | findstr dotenv    # Windows
   pip list | grep dotenv       # Mac/Linux
   ```
   If not found, install it:
   ```bash
   pip install python-dotenv
   ```

---

## ✅ Quick Checklist

- [ ] I have a Doppio account (https://doppio.sh)
- [ ] I have copied my API key
- [ ] I created a `.env` file (with the dot!)
- [ ] The `.env` file is in the `pdfcon` folder
- [ ] The file contains: `DOPPIO_API_KEY=my_actual_key`
- [ ] There are NO spaces around the `=` sign
- [ ] The file is NOT named `.env.txt`
- [ ] I restarted my terminal/command prompt
- [ ] I'm in the correct folder when running commands

---

## 🎯 Recommended Solution

**Use the helper script** - it's the easiest way:

**Windows:**
```cmd
set_api_key.bat
```

**Mac/Linux:**
```bash
python3 set_api_key.py
```

This will guide you through the entire setup process!

---

**Good luck! You'll have PDFs generating in no time! 🚀📄**