import time
import pyperclip
from langchain_google_genai import GoogleGenerativeAI
import pyautogui
import paperclip
import os
import shutil
import subprocess


def remove_first_and_last_lines(paragraph):
    lines = paragraph.split("\n")
    return "\n".join(lines[1:-1])


# Retrieve text from clipboard

class Dev:
    def __init__(self, key, temperature=0.5):
        self.api_key = key
        self.llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=key, temperature=temperature)
        pass

    def debugger(self, error, prompt=None, dest="current"):
        # get code
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        copied_text = pyperclip.paste()

        # debug code
        if prompt is None:
            mcd = self.llm.invoke(f"""you are a greate programmer, and you have a job to catch the motive of given code 
                and then debug given code and if syntax is not correct of given code for approaching to motive then use 
                appropriate syntax to approach to motive you can also change values or even whole code's pattern for 
                correcting syntax, and note that do not write anything else except code I mean do not write explanations 
                but you can write explanation those changes which you make using comments in your code
                and other things, this is a code: {copied_text}
                    and this is a error {error}
                        """)

            # clear previous code
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press('backspace')

            # reformat code
            rcd = remove_first_and_last_lines(mcd)

            if dest == "current":
                # write modified code
                pyautogui.write(rcd)

                # finally format code
                pyautogui.hotkey("ctrl", "alt", "l")
                pyautogui.hotkey("ctrl", "alt", "shift", "l")
                pyautogui.press("enter")

            if dest == "separate":
                with open("debugged code.py", "w") as gene:
                    gene.write(rcd)



        else:
            mcd = self.llm.invoke(f"{prompt}, This is my code {pyperclip.paste()}")

            # clear previous code
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press('backspace')

            # reformat code
            rcd = remove_first_and_last_lines(mcd)

            if dest == "current":
                # write modified code
                pyautogui.typewrite(rcd)

                # finally format code
                pyautogui.hotkey("ctrl", "alt", "l")
                pyautogui.hotkey("ctrl", "alt", "shift", "l")
                pyautogui.press("enter")

            if dest == "separate":
                with open("debugged code.py", "w") as gene:
                    gene.write(rcd)

    def upload_git(self, gitname, reponame):
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(2)

        pyautogui.write('git init')
        pyautogui.press('enter')
        time.sleep(2)

        pyautogui.write('git commit -m "Initial commit"')
        pyautogui.press('enter')
        time.sleep(2)

        pyautogui.write(f'git remote add origin https://github.com/{gitname}/{reponame}.git')
        pyautogui.press('enter')
        time.sleep(2)

        # Push your code to the remote repository
        pyautogui.write('git push -u origin master')
        pyautogui.press('enter')

    def generate_readme(self):
        # get code
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        copied_text = pyperclip.paste()

        rd = self.llm.invoke(f"write proper readme file for this code with description and installations "
                             f"instructions and other necessary things and components: {copied_text}")

        filename = "README.md"

        with open(filename, "w") as file:
            # Optionally, write some content to the file
            file.write(rd)

    def rename_github_repo(self, old_name, new_name):
        """Renames a GitHub repo using user terminal with PyAutoGUI."""

        # Navigate to the GitHub repo directory in terminal
        pyautogui.hotkey('win', 'r')  # Open Run dialog
        time.sleep(0.5)
        pyautogui.typewrite('cmd')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('cd ' + old_name)
        pyautogui.press('enter')
        time.sleep(1)

        # Execute the git rename command
        pyautogui.typewrite('git mv ' + old_name + ' ' + new_name)
        pyautogui.press('enter')
        time.sleep(2)  # Adjust for potential delays

        # Push the changes to GitHub
        pyautogui.typewrite('git push origin master --force')
        pyautogui.press('enter')
        time.sleep(5)  # Adjust for push time

    def generate(self, prompt, dest="current"):
        cd = self.llm.invoke(prompt)

        rcd = remove_first_and_last_lines(cd)

        if dest == "current":
            # write modified code
            pyautogui.write(rcd)

            # finally format code
            pyautogui.hotkey("ctrl", "alt", "l")
            pyautogui.hotkey("ctrl", "alt", "shift", "l")
            pyautogui.press("enter")

        if dest == "separate":
            with open("generated code.py", "w") as gene:
                gene.write(rcd)

    def review(self):
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        copied_text = pyperclip.paste()

        rv = self.llm.invoke(
            f"review this code tell me some suggestions, improvements, pros and cons of this code: {copied_text}")

        filename = "review.txt"

        with open(filename, "w") as file:
            # Optionally, write some content to the file
            file.write(rv)

    def generate_requirements(self):
        # get code
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        copied_text = pyperclip.paste()

        rd = self.llm.invoke(f"write requirements.txt file for this code: {copied_text}")
        sd = remove_first_and_last_lines(rd)

        filename = "requirements.txt"

        with open(filename, "w") as file:
            # Optionally, write some content to the file
            file.write(sd)

    def generate_setup(self):
        # get code
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        copied_text = pyperclip.paste()

        rd = self.llm.invoke(f"write setup.py file for this: {copied_text}")
        sd = remove_first_and_last_lines(rd)

        filename = "setup.py"

        with open(filename, "w") as file:
            # Optionally, write some content to the file
            file.write(sd)

    def Generate_UI(self):
        # get code
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        copied_text = pyperclip.paste()

        cd = self.llm.invoke(f"Read this backend code {copied_text}, and analyze this code, and Please write HTML with "
                             f"inline css for my this code,"
                             f"and make sure that write code which connects this backend code into itself")

        filename = "index.html"

        with open(filename, "w") as file:
            # Optionally, write some content to the file
            file.write(cd)

        time.sleep(3)

        pyautogui.hotkey("ctrl", "F2")

    def Explain(self, mode="detail"):
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        copied_text = pyperclip.paste()

        cd = self.llm.invoke(
            f"Read this code {copied_text}, and analyze this code, and please explain this code in {mode}")

        filename = "explanation.txt"

        with open(filename, "w") as file:
            # Optionally, write some content to the file
            file.write(cd)

    def modify(self, prompt, dest="current"):
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        copied_text = pyperclip.paste()

        mcd = self.llm.invoke(f"""{prompt}, this is a code: {copied_text}
                        """)

        rcd = remove_first_and_last_lines(mcd)

        if dest == "current":

            # clear previous code
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press('/')
            pyautogui.leftClick()
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press('down')
            pyautogui.press("enter")

            # write modified code
            pyautogui.write(rcd)

            # finally format code
            pyautogui.hotkey("ctrl", "alt", "l")
            pyautogui.hotkey("ctrl", "alt", "shift", "l")
            pyautogui.press("enter")

        if dest == "separate":
            with open("modified code.py", "w") as gene:
                gene.write(rcd)

    def trans(self, filename, target: str = "Java"):
        # get code
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        copied_text = pyperclip.paste()

        # debug code
        mcd = self.llm.invoke(f"""you are a greate programmer, and you have a job to catch the motive of given code 
                        and then translate given code in target language and note that do not write anything else except code I mean do not write explanations 
                        but you can write explanation those changes which you make using comments in your code
                        and other things, this is a code: {copied_text}
                            target language is {target}
                                """)

        # reformat code
        rcd = remove_first_and_last_lines(mcd)

        filename = filename

        with open(filename, "w") as file:
            # Optionally, write some content to the file
            file.write(rcd)

    def setup_flask_app(self):
        flask_app = """
from flask import Flask
app = Flask(__name__)
        
@app.route('/')
def hello_world():
    return 'Hello, World!'
        """

        html = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
            
<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
            
</body>
</html>
        """

        os.makedirs('static', exist_ok=True)  # Create 'static' directory if it doesn't exist
        os.makedirs('templates', exist_ok=True)  # Create 'templates' directory if it doesn't exist

        # Write basic Flask app code to a new Python file
        with open('app.py', 'w') as f:
            f.write(flask_app)

        folder_path = "templates"
        file_name = "index.html"
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "w") as f:
            f.write(html)

    def Fetch_Version(self):
        return "v1.1.0"
