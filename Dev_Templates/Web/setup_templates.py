import os

loc = os.getcwd()
new_loc = loc.replace("\\", "/")


def get_configs(filename):
    with open(f"{new_loc}/Dev/Dev_Templates/Web/configs/HTML/{filename}", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content


def fetch_configs():
    return os.listdir(f"{new_loc}/Dev/Dev_Templates/configs/HTML/")


def setup_configs():
    flask_app = """
from flask import Flask, render_template
import Dev.Dev_Templates.setup_templates as ds
import os

app = Flask(__name__)

os.makedirs('templates', exist_ok=True)

html = ds.get_configs("general.html")
folder_path = "templates"
file_name = "index.html"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as f:
    f.write(html)
        
@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

            """

    os.makedirs('static', exist_ok=True)  # Create 'static' directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)  # Create 'templates' directory if it doesn't exist

    # Write basic Flask app code to a new Python file
    with open('app.py', 'w') as f:
        f.write(flask_app)

