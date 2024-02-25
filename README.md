# Dev: Your AI-Powered Coding Assistant

# Table of contents
- [Introduction](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#introduction)
- [Features of Dev](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#unique-features-of-dev)
- [Benefits of Dev](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#benefits-of-dev)
- [Ongoing Developments](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#ongoing-developments)
- [Basic Requirements](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#basic-requirements)
- [Get started](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#getting-started)
- [Quick Start](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#quick-start)
- [Documentation](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#checkout-documentation-of-dev)
- [Updates](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#dev-updates)
- [Latest version](https://github.com/GitCoder052023/Dev?tab=readme-ov-file#latest-version-v110)

# Introduction
Dev is a multi-purpose tool designed to streamline your coding workflow and leverage the power of large language models to enhance your productivity. It automates several common tasks and provides valuable insights through AI capabilities, making your coding experience smoother and more efficient.

# Unique Features of Dev:

- AI-powered Debugging: Stuck on a coding bug? Dev can analyze your code with the help of a large language model, identify the error, and suggest corrections. Simply provide the error message or a specific prompt for tailored debugging assistance.

- Automated README Generation: Forget manually writing READMEs! Dev can automatically generate a comprehensive README file for your project, including descriptions, installation instructions, and other essential details.

- Creative Code Generation: Need a jumpstart on your code? Dev can generate code snippets based on your instructions, offering you creative and effective solutions to overcome coding challenges.

- In-depth Code Review: Unsure about your code's quality? Dev provides a detailed code review, highlighting potential improvements, optimizations, and areas for consideration. This valuable feedback can elevate your code to the next level.

- Seamless Git Integration: Dev simplifies project management by automating Git commands. You can easily create and upload repositories, rename existing ones, and push your code with just a few function calls.
  
- Tired of manually crafting requirements.txt and setup.py files for your Python projects? Dev takes care of these essential tasks with a few simple commands, saving you time and ensuring accuracy.

- Tired of manually crafting UI interfaces for your backend code? Dev takes care of the heavy lifting, effortlessly creating a matching user interface with integrated backend functionality.

- Seeking a comprehensive understanding of your code? Dev offers clear and insightful explanations, tailored to your preferred level of detail.

- Setup Flask App: The ```setup_flask_app()``` function empowers you to effortlessly create a basic Flask application with minimal setup. This function streamlines the initial configuration process, saving you time and effort when starting new web development projects using Flask.

# Benefits of Dev:

- Increased Productivity: Automate repetitive tasks like debugging and README generation, freeing up your time for more focused development.
- Improved Code Quality: Gain valuable insights from AI-powered debugging and code review, resulting in cleaner, more efficient code.
- Enhanced Creativity: Explore new possibilities with code generation, sparking innovation and overcoming coding hurdles.
- Streamlined Workflow: Integrate seamlessly with Git for effortless project management, allowing you to focus on what matters most - writing great code.

# Ongoing Developments
- Building app templates for kivy, tkinker, PyQT
- Building API templates for building APIs using FastAPI

# Basic requirements:
- Windows 10 (Supports only windows)
- Python 3.9+


# Getting Started:
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

Get your google gemini API key from [here](https://makersuite.google.com/app/apikey)
```Bash
export GOOGLE_API_KEY=YOUR_API_KEY
```

# Quick start
```python
from Dev.Developer import Dev

assistant = Dev.Dev("YOUR GOOGLE GEMINI API KEY") # You can leave this as it is if you don't want to use debug, generate and other generation tools of Dev

assistant.generate("write a python code which can print 0 to 100")
```

# Checkout Documentation of Dev

Click on this --> [Read Documentation](https://jovian.com/k-alam93899/Dev%20Documentation) link to read documentation of Dev

# Announcements

# Dev Updates

🚀 **Introducing New Features!**

Starting from **February 13, 2024**, I am thrilled to announce a series of updates for **Dev**. These updates will enhance the platform by introducing major functionalities. Today marks the release of the **socket functionality**, an inbuilt feature that allows seamless socket connections using just one line of code in **Dev**.

## Major release

Socket Functionality: The star of this release, the socket functionality, is an inbuilt feature that simplifies socket connections using just one line of code in Dev. Whether you’re building real-time applications, chat systems, or multiplayer games, this feature streamlines communication between clients and servers.

## Socket Functionality Highlights:

- **Effortless Connectivity**: Establish socket connections effortlessly.
- **Streamlined Communication**: Communicate efficiently between clients and servers.
- **Minimal Code**: Achieve powerful socket functionality with concise code.

## Minor Improvements

- `fetch_Version()`: Fetch your current version of Dev
---

# Latest Version v1.1.0

## Description

In this latest Version v1.1.0 you got one new features which is setup group connection, setup group connection builds a server and client setup for you which allows to use build your chat applications without focusing on server setup. Basically, this feature allows multiple clients to interact between them like whatsapp, using this setup clients can send messages and recieves messages from other clients. 

**Note**: But note that this feauture only builds server and client setup and very basic user interaction so you need to customise it according to your needs!
Dev is your comprehensive coding companion. Whether you're a seasoned developer looking for a productivity boost or a beginner seeking guidance, Dev has something to offer. Embrace the power of AI and watch your coding workflow reach new heights of efficiency and effectiveness.
