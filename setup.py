from setuptools import setup, find_packages

setup(
    name='Debugger',  # Name of the package
    version='0.1.0',  # Initial version
    author='GitCoder052023',  # Author's name
    author_email='K.alam93899@gmail.com',  # Author's email (replace with yours)
    description='A tool to debug your code using AI',
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'pyperclip',
        'langchain_google_genai',
        'pyautogui',
        'paperclip',
        'pymongo'
    ],  # List of dependencies
)
