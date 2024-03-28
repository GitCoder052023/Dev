from setuptools import setup, find_packages

setup(
    name='Dev',  # Name of the package
    version='1.1.0',  # Initial version
    author='GitCoder052023',  # Author's name
    author_email='K.alam93899@gmail.com',  # Author's email (replace with yours)
    description='Dev is a multi-purpose tool designed to streamline your coding workflow and leverage the power of '
                'large language models to enhance your productivity. It automates several common tasks and provides '
                'valuable insights through AI capabilities, making your coding experience smoother and more efficient.',
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'pyperclip',
        'langchain_google_genai',
        'pyautogui',
        'paperclip',
        'pymongo'
    ],  # List of dependencies
)
