import subprocess

def install_spacy_model():
    try:
        # Install the SpaCy model using the CLI tool
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"], check=True)
        print("SpaCy model en_core_web_sm installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing SpaCy model:", e)
        raise e