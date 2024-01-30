import time
import pyperclip
from langchain_google_genai import GoogleGenerativeAI
import pyautogui
import paperclip

def remove_first_and_last_lines(paragraph):
    lines = paragraph.split("\n")
    return "\n".join(lines[1:-1])


# Retrieve text from clipboard

class Debugger:
    def __init__(self, key):
        self.api_key = key
        self.llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=key)
        pass

    def debugger(self, error, prompt=None):
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

            # write modified code
            pyautogui.write(rcd)

            # finally format code
            pyautogui.hotkey("ctrl", "alt", "l")
            pyautogui.hotkey("ctrl", "alt", "shift", "l")
            pyautogui.press("enter")

        else:
            mcd = self.llm.invoke(f"{prompt}, This is my code {pyperclip.paste()}")

            # clear previous code
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press('backspace')

            # reformat code
            rcd = remove_first_and_last_lines(mcd)

            # write modified code
            pyautogui.typewrite(rcd)

            # finally format code
            pyautogui.hotkey("ctrl", "alt", "l")
            pyautogui.hotkey("ctrl", "alt", "shift", "l")
            pyautogui.press("enter")
