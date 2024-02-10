import os

loc = os.getcwd()
new_loc = loc.replace("\\", "/")


def get_configs(filename):
    with open(f"{new_loc}/Dev/Templates/configs/HTML/{filename}", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content


def fetch_configs():
    return os.listdir(f"{new_loc}/Templates/configs/HTML/")

