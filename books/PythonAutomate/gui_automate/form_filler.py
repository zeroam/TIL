"""form_filler.py
자동으로 form 작성
"""
import pyautogui
import time

name_field = (716, 399)
another_link = (706, 271)

form_data = [
    {"name": "Alice", "fear": "eavesdroppers", "source": "wand", "robocop": 4, "comments": "Tell Bob I said hi."},
    {"name": "Bob", "fear": "bees", "source": "amulet", "robocop": 4, "comments": "n/a"},
    {"name": "Carol", "fear": "puppets", "source": "crystal ball", "robocop": 1, "comments": "Please take the puppets out of the break room"},
    {"name": "Alex Murphy", "fear": "ED-209", "source": "money", "robocop": 5, "comments": "Protect the innocent. Serve the public trust. Uphold the law."}
]

source_down_cnt = {
    "wand": 1,
    "amulet": 2,
    "crystal ball": 3,
    "money": 4,
}

pyautogui.PAUSE = 0.5
print("Ensure that the browser window is active and the form is loaded!")

for person in form_data:
    # Give the user a chance to kill the script
    print(">>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<")
    time.sleep(5)

    print(f"Entering {person['name']} info...")
    # pyautogui.write(["\t", "\t"])
    pyautogui.click(*name_field)

    # Fill out the Name Field
    pyautogui.write(person["name"] + "\t")

    # Fill out the Greatest Fear(s) field
    pyautogui.write(person["fear"] + "\t")

    # Fill out the Source of Wizard Powers field.
    source_write = ["down"] * source_down_cnt[person["source"]]
    source_write.append("enter")
    source_write.append("\t")
    pyautogui.write(source_write, 0.5)

    # Fill out the RoboCop field
    robocop_write = [" "]
    robocop_write.extend(["right"] * (person["robocop"] - 1))
    robocop_write.append("\t")
    robocop_write.append("\t")
    pyautogui.write(robocop_write, 0.5)

    # Fill out the Additional Comments field.
    pyautogui.write(person["comments"] + "\t")

    # Click Submit
    time.sleep(0.5)  # Wait for button to activate
    pyautogui.press("enter")
    # Wait until form page has loaded.
    print("Submitted form.")
    time.sleep(5)

    # Click the submit another response link
    pyautogui.click(*another_link)
