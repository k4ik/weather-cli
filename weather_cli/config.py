import typer
import inquirer
from dotenv import load_dotenv, set_key
import os
import json

app = typer.Typer()


if not os.path.exists("locales"):
    os.makedirs("locales")

if not os.path.exists(".env"):
    with open(".env", "w") as f:
        pass
    set_key(".env", "TOOL_LANGUAGE", "en")

def load_translation():
    load_dotenv()
    lang = os.getenv("TOOL_LANGUAGE", "en")
    try:
        with open(f"locales/{lang}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Translation file for '{lang}' not found. Falling back to English.")
        with open("locales/en.json", "r", encoding="utf-8") as file:
            return json.load(file)

translations = load_translation()

@app.command()
def setup():
    choices = translations["menu-setup"]["choices"]
    selected = inquirer.list_input(
        message=translations["menu-setup"]["message"],
        choices=choices
    )

    if selected == translations["menu-setup"]["choices"][0]:  
        print(translations["menu-setup"]["menu-key"]["message"])
        key = inquirer.text(message=translations["menu-setup"]["menu-key"]["prompt"])
        set_key(".env", "API_KEY", key)
        print(translations["menu-setup"]["menu-key"]["confirmation"])

    elif selected == translations["menu-setup"]["choices"][1]: 
        lang_choices = ["en", "es", "fr", "de", "it", "pt", "ru", "pl", "ro", "ar", "ja", "zh"]
        lang_selected = inquirer.list_input(
            message=translations["menu-setup"]["menu-lang"]["message"],
            choices=lang_choices
        )
        set_key(".env", "TOOL_LANGUAGE", lang_selected)
        print(translations["menu-setup"]["menu-lang"]["confirmation"])

if __name__ == "__main__":
    typer.run(setup)
