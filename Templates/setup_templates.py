import os

loc = os.getcwd()
n = loc.replace("\\", "/")


def get_configs(filename):
    with open(f"{n}/Templates/configs/HTML/{filename}", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content


def fetch_configs():
    return os.listdir(f"{n}/Templates/configs/HTML/")

