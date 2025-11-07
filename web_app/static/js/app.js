// PDF Generation Agent - Frontend JavaScript

// DOM Elements
const promptTab = document.getElementById('prompt-tab');
const markdownTab = document.getElementById('markdown-tab');
const promptInstructions = document.getElementById('prompt-instructions');
const markdownInstructions = document.getElementById('markdown-instructions');
const contentInput = document.getElementById('content-input');
const modeInput = document.getElementById('mode-input');
const pdfForm = document.getElementById('pdf-form');
const generateBtn = document.getElementById('generate-btn');
const loadingDiv = document.getElementById('loading');
const resultDiv = document.getElementById('result');
const errorDiv = document.getElementById('error');
const downloadLink = document.getElementById('download-link');
const errorText = document.getElementById('error-text');

// Current mode
let currentMode = 'prompt';

// Initialize the app
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    updateUI();
});

// Setup event listeners
function setupEventListeners() {
    // Tab switching
    promptTab.addEventListener('click', () => switchMode('prompt'));
    markdownTab.addEventListener('click', () => switchMode('markdown'));

    // Form submission
    pdfForm.addEventListener('submit', handleFormSubmit);

    // Content input validation
    contentInput.addEventListener('input', validateInput);
}

// Switch between input modes
function switchMode(mode) {
    currentMode = mode;
    modeInput.value = mode;

    // Update tab buttons
    promptTab.classList.toggle('active', mode === 'prompt');
    markdownTab.classList.toggle('active', mode === 'markdown');

    // Update instructions
    promptInstructions.classList.toggle('hidden', mode !== 'prompt');
    markdownInstructions.classList.toggle('hidden', mode !== 'markdown');

    // Update placeholder
    if (mode === 'prompt') {
        contentInput.placeholder = 'Describe what you want in your PDF...\n\nExample: Create a professional resume with contact information, skills section, and work experience.';
    } else {
        contentInput.placeholder = 'Enter your markdown content here...\n\n# My Document\n\nThis is **bold** text.\n\n- List item 1\n- List item 2\n\n```javascript\nconsole.log("Hello World!");\n```';
    }

    updateUI();
}

// Update UI based on current state
function updateUI() {
    // Update generate button text
    generateBtn.innerHTML = currentMode === 'prompt'
        ? '🚀 Generate PDF'
        : '📄 Convert to PDF';

    // Validate input
    validateInput();
}

// Validate input content
function validateInput() {
    const content = contentInput.value.trim();
    const isValid = content.length > 0;

    generateBtn.disabled = !isValid;

    if (isValid) {
        generateBtn.style.opacity = '1';
    } else {
        generateBtn.style.opacity = '0.6';
    }
}

// Handle form submission
async function handleFormSubmit(event) {
    event.preventDefault();

    const content = contentInput.value.trim();
    if (!content) {
        showError('Please enter some content');
        return;
    }

    // Show loading state
    showLoading();

    try {
        // Prepare form data
        const formData = new FormData();
        formData.append('content', content);
        formData.append('mode', currentMode);

        // Send request
        const response = await fetch('/generate-pdf', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showSuccess(data.download_url);
        } else {
            showError(data.error || 'Failed to generate PDF');
        }

    } catch (error) {
        console.error('Error:', error);
        showError('Network error. Please check your connection and try again.');
    }
}

// Show loading state
function showLoading() {
    hideAllStates();
    loadingDiv.classList.remove('hidden');
    generateBtn.disabled = true;
    generateBtn.innerHTML = '⏳ Generating...';
}

// Show success state
function showSuccess(downloadUrl) {
    hideAllStates();
    resultDiv.classList.remove('hidden');
    downloadLink.href = downloadUrl;

    // Reset button
    generateBtn.disabled = false;
    generateBtn.innerHTML = currentMode === 'prompt'
        ? '🚀 Generate PDF'
        : '📄 Convert to PDF';
}

// Show error state
function showError(message) {
    hideAllStates();
    errorDiv.classList.remove('hidden');
    errorText.textContent = message;

    // Reset button
    generateBtn.disabled = false;
    generateBtn.innerHTML = currentMode === 'prompt'
        ? '🚀 Generate PDF'
        : '📄 Convert to PDF';
}

// Hide error (for retry button)
function hideError() {
    errorDiv.classList.add('hidden');
}

// Hide all states
function hideAllStates() {
    loadingDiv.classList.add('hidden');
    resultDiv.classList.add('hidden');
    errorDiv.classList.add('hidden');
}

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
    // Ctrl/Cmd + Enter to submit
    if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
        event.preventDefault();
        if (!generateBtn.disabled) {
            pdfForm.dispatchEvent(new Event('submit'));
        }
    }

    // Tab switching with keyboard
    if (event.altKey) {
        if (event.key === '1') {
            event.preventDefault();
            switchMode('prompt');
        } else if (event.key === '2') {
            event.preventDefault();
            switchMode('markdown');
        }
    }
});

// Auto-resize textarea
contentInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 600) + 'px';
});

// Initialize textarea height
contentInput.style.height = 'auto';
contentInput.style.height = Math.min(contentInput.scrollHeight, 600) + 'px';

// Service worker for offline functionality (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // Register service worker for caching (if implemented)
        // navigator.serviceWorker.register('/sw.js');
    });
}
