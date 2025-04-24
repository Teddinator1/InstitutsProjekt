import subprocess
import os

# Aktuellen Pfad ermitteln (wo start.py liegt)
base_path = os.path.dirname(os.path.abspath(__file__))

# Pfade zu den anderen Skripten
sender_path = os.path.join(base_path, "erster.py")
receiver_path = os.path.join(base_path, "zweiter.py")

# Beide Streamlit-Apps starten
subprocess.Popen(["streamlit", "run", sender_path])
subprocess.Popen(["streamlit", "run", receiver_path])