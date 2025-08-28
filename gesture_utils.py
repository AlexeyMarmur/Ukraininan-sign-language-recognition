# gesture_utils.py
import os

GESTURES_FILE = "gestures.py"

def load_gestures():
    gesture_list = []
    if not os.path.exists(GESTURES_FILE):
        return gesture_list

    with open(GESTURES_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_list = False
    for line in lines:
        line = line.strip()
        if line.startswith("GESTURES"):
            in_list = True
            continue
        if in_list:
            if line.startswith("]"):
                break
            gesture = line.strip('",\'').rstrip(',').strip()
            if gesture:
                gesture_list.append(gesture)
    return gesture_list

def save_gestures(gestures):
    with open(GESTURES_FILE, "w", encoding="utf-8") as f:
        f.write("GESTURES = [\n")
        for g in gestures:
            f.write(f'    "{g}",\n')
        f.write("]\n")