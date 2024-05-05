#for generation of plantuml diagrams
import os
from pathlib import Path
import subprocess

# Inspired from:
# https://stackoverflow.com/questions/62980868/how-to-create-multiple-plantuml-diagrams-from-a-python-script

class Pyrev:

    def __init__(self,src_root: Path,diagram_dir: str) -> None:
        self.src_root = src_root
        self.diagram_dir = diagram_dir
        if not Path("Diagrams/").exists():
            os.mkdir("Diagrams")
        
    def run(self):
        command_string = f"pyreverse {str(self.src_root)} -o puml --colorized -d {self.diagram_dir}"
        subprocess.run(command_string,shell=True)
