# AI-Powered Code Debugger

This tool leverages Google AI's language model to assist with code debugging. It automatically analyzes code, identifies errors, and generates potential fixes using AI-powered suggestions.

## Description
This project provides a powerful tool for developers to streamline their debugging process. It is designed to automate the process of debugging code, making it more efficient and less time-consuming.

**Benefits for Developers:**
- Automated Debugging: This tool automates the process of debugging, saving developers valuable time and effort. It eliminates the need for manual debugging, making the process more efficient.
- Error Correction: The tool not only identifies errors in the code but also corrects them automatically. This ensures that the code is always in the best possible state.
- Customizable: The tool can be customized to suit the needs of individual developers. It can be used with or without a prompt, giving developers flexibility in how they use the tool.
- Easy to Use: The tool is easy to use, with a simple and intuitive interface. This makes it accessible to developers of all skill levels.  

**Key Features:**

- Leverages Google's Gemini Pro language model for intelligent code analysis.
- Automatically retrieves code from the clipboard for seamless debugging.
- Generates potential fixes based on AI-powered insights.
- Automatically apply fixes within the code editor.

**Key Components:**

- **Debugger Class:** Encapsulates the debugging functionality.
- **debugger() Method:**
    - Retrieves code from the clipboard.
    - Utilizes GoogleGenerativeAI to generate potential fixes.
    - Applies fixes using PyAutoGUI.
- **remove_first_and_last_lines() Function:** Cleans up AI-generated code formatting.

## Installation Instructions

1. **Prerequisites:**
    - Python 3.x: https://www.python.org/downloads/](https://www.python.org/downloads/
    - Required libraries:
      - ```pip install requirements.txt```
      - Obtain a Google API key: https://makersuite.google.com/app/apikey

2. **Clone or Download:**
    - Clone this repository: `git clone https://github.com/GitCoder052023/Debugger`
    - Or download the code as a ZIP file.

## Usage

1. **Import the Debugger Class:**
   ```python
   from debugger import Debugger
   ```

2. **Create a Debugger Instance with Your API Key:**
   ```python
   debugger = Debugger(your_google_api_key)
   ```

3. **Initiate Debugging:**
   - **When an error occurs:**
     ```python
     debugger.debugger(error)  # Pass the error message as an argument
     ```
   - **To provide a specific prompt for guidance:**
     ```python
     debugger.debugger(error, prompt="Add a comment explaining this line of code")
     ```

## Sample code
```python
from Debugger import self_debugger
from key import key # please create a new python file "key" then paste your key inside their 

debugger = self_debugger.Debugger(key) # you can directly paste your api key

try:
    def greet_user(name):
        print("Hello, " + uname + "!")  # Typo: uname instead of name

    greet_user("Alice")

except Exception as e:
    self_debugger.Debugger(e)
```


**Contribute:** Feel free to contribute to this project by opening issues or pull requests!
