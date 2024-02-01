# Dev: Your AI-Powered Coding Assistant

Dev is a multi-purpose tool designed to streamline your coding workflow and leverage the power of large language models to enhance your productivity. It automates several common tasks and provides valuable insights through AI capabilities, making your coding experience smoother and more efficient.

# Table of Contents

- [Dev: Your AI-Powered Coding Assistant](#dev-your-ai-powered-coding-assistant)
- [Features of Dev](#features-of-dev)
  - [AI-powered Debugging](#ai-powered-debugging)
  - [Automated README Generation](#automated-readme-generation)
  - [Creative Code Generation](#creative-code-generation)
  - [In-depth Code Review](#in-depth-code-review)
  - [Seamless Git Integration](#seamless-git-integration)
- [Benefits of Dev](#benefits-of-dev)
- [Getting Started](#getting-started)
- [Deep Dive in Dev](#deep-dive-in-dev)


## Features of Dev:

- AI-powered Debugging: Stuck on a coding bug? Dev can analyze your code with the help of a large language model, identify the error, and suggest corrections. Simply provide the error message or a specific prompt for tailored debugging assistance.

- Automated README Generation: Forget manually writing READMEs! Dev can automatically generate a comprehensive README file for your project, including descriptions, installation instructions, and other essential details.

- Creative Code Generation: Need a jumpstart on your code? Dev can generate code snippets based on your instructions, offering you creative and effective solutions to overcome coding challenges.

- In-depth Code Review: Unsure about your code's quality? Dev provides a detailed code review, highlighting potential improvements, optimizations, and areas for consideration. This valuable feedback can elevate your code to the next level.

- Seamless Git Integration: Dev simplifies project management by automating Git commands. You can easily create and upload repositories, rename existing ones, and push your code with just a few function calls.
  
- Tired of manually crafting requirements.txt and setup.py files for your Python projects? Dev takes care of these essential tasks with a few simple commands, saving you time and ensuring accuracy.

## Benefits of Dev:

- Increased Productivity: Automate repetitive tasks like debugging and README generation, freeing up your time for more focused development.
- Improved Code Quality: Gain valuable insights from AI-powered debugging and code review, resulting in cleaner, more efficient code.
- Enhanced Creativity: Explore new possibilities with code generation, sparking innovation and overcoming coding hurdles.
- Streamlined Workflow: Integrate seamlessly with Git for effortless project management, allowing you to focus on what matters most - writing great code.

## Getting Started:
**Clone repo:**
1: clone repo
```bash
git clone https://github.com/GitCoder052023/Dev.git
```

2: Install the required libraries:

```Bash
pip install -r requirements.txt
```

3: Obtain a Google API key for Google Generative AI and set it as an environment variable:

```Bash
export GOOGLE_API_KEY=YOUR_API_KEY
```

**Download package locally:**
```bash
pip install git+https://github.com/GitCoder052023/Dev.git
```

Dev is your comprehensive coding companion. Whether you're a seasoned developer looking for a productivity boost or a beginner seeking guidance, Dev has something to offer. Embrace the power of AI and watch your coding workflow reach new heights of efficiency and effectiveness.

# Deep Dive in Dev:

## Debugger
Debugger provides a powerful tool for developers to streamline their debugging process. It is designed to automate the process of debugging code, making it more efficient and less time-consuming.

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

## Usage

1. **Import the Debugger Class:**
  ```python
  from Dev.Developer import Dev
  ```

2. **Create a Debugger Instance with Your API Key:**
  ```python
  debugger = Dev.Dev(your-key)
  ```

3. **Initiate Debugging:**
  - **When an error occurs:**
   ```python
   debugger.Debugger(error) # Pass the error message as an argument
   ```
  - **To provide a specific prompt for guidance:**
   ```python
   debugger.Debugger(error, prompt="Add a comment explaining this line of code")
   ```

## Sample code
```python
from Dev.Developer import Dev
from key import key # please create a new python file "key" then paste your key inside their 

debugger = Dev.Dev(key) # you can directly paste your api key

try:
  def greet_user(name):
    print("Hello, " + uname + "!") # Typo: uname instead of name

  greet_user("Alice")

except Exception as e:
  debugger.Debugger(e)
```

## README Generator
The README Generator empowers you to effortlessly create detailed and informative READMEs for your projects. Forget spending time manually crafting these essential documents – this feature does the heavy lifting for you.

**Usage:**

1: Import the Dev Class:

```Python
from Dev.Developer import Dev
```

```Python
dev = Dev(your-key)
```

```Python
dev.generate_readme()
```

```Python
from Dev.Developer import Dev
from key import key

dev = Dev.Dev(key)

dev.generate_readme()

print("Your README is generated! Check out the 'README.md' file.")
```

## Upload Git:

This functionality simplifies Git repository management by automating commands

**Usage:**

1: Import the Dev Class:

```Python
from Dev.Developer import Dev
```

```Python
dev = Dev(your-key)
```

2: Upload your code to a new repository:

```Python
dev.upload_git("your-git-username", "your-repository-name")
```

**Sample Code:**

```Python
from Dev.Developer import Dev
from key import key

dev = Dev.Dev(key)

dev.upload_git("Bard-Dev", "my-awesome-project")

print("Your code is uploaded to your GitHub repository!")
```

## Rename GitHub Repo:

This feature allows you to easily rename your existing GitHub repository directly from your code editor.

**Usage:**

1: Import the Dev Class:

```Python
from Dev.Developer import Dev
```

2: Create a Dev Instance:

```Python
dev = Dev.Dev(your-key)
```

3: Rename your repository:

```Python
dev.rename_github_repo("old-repo-name", "new-repo-name")
```

**Sample Code:**

```Python
from Dev.Developer import Dev
from key import key

dev = Dev.Dev(key)

dev.rename_github_repo("my-old-repo", "my-new-repo)
```

## Create GitHub Repo:

This function helps you quickly create a new GitHub repository through your web browser.

**Usage:**

1: Import the Dev Class:

```Python
from Dev.Developer import Dev
```

2: Create a Dev Instance:

```Python
dev = Dev(your-key)
```

3: Create a new repository:

```Python
dev.create_github_repo("my-shiny-new-project")
```

**Sample Code:**

```Python
from Dev.Developer import Dev
from key import key

dev = Dev.Dev(key)

dev.create_github_repo("amazing-code-collection")

print("Your new repository is ready on GitHub!")
```

## Generate:

This functionality leverages the language model to generate code based on your instructions or prompts.

**Usage:**

1: Import the Dev Class:

```Python
from Dev.Developer import Dev
```

2: reate a Dev Instance:

```Python
dev = Dev.Dev(your-key)
```

3: Generate code based on a prompt:

```Python
dev.generate("create a python code to print 0 to 100")
```

## Review
The Review function provides valuable insights into your code, helping you refine its quality and identify potential areas for improvement.

**Usage:**

1: Import the Dev Class:

```Python
from Dev.Developer import Dev
```

2: Create a Dev Instance:

```Python
dev = Dev(your-key)
```

3: Run the Review:

```Python
dev.review()
```

**Output:**

The review report will be saved to a file named "review.txt". This file will contain detailed feedback on your code, including:

- Potential improvements: Suggestions for optimizing code structure, performance, and readability.
- Alternative approaches: Different ways to achieve the same functionality, potentially offering advantages in specific situations.
- Warnings and errors: Identification of potential bugs, code smells, and best practices violations.
- Overall comments: General observations and recommendations for enhancing your code.

**Sample Code:**

```Python
from Dev.Developer import Dev
from key import key

dev = Dev.Dev(key)

dev.review()

print("Your code review is saved in 'review.txt'!")
```

## Generate Requirements Files:

**Key Features:**

- Automatically analyzes your code to identify required dependencies.
- Creates a comprehensive requirements.txt file listing those dependencies.
- Ensures compatibility and reproducibility for project setup.

**Usage:**

```Python
dev.generate_requirements()
```

**Output:**
A requirements.txt file is generated in your project directory, ready for use.

## Generate Setup Files:

**Key Features:**

- Automates the creation of setup.py files for Python projects.
- Streamlines the packaging and distribution process.
- Simplifies installation for others who want to use your project.

**Usage:**

```Python
dev.generate_setup()
```

**Output:**
A setup.py file is generated in your project directory, ready for deployment.

