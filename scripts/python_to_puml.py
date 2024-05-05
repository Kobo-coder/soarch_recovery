#for generation of plantuml diagrams
import os
from pathlib import Path
from py2puml.py2puml import py2puml
import subprocess

import py2puml.py2puml

# Inspired from:
# https://stackoverflow.com/questions/62980868/how-to-create-multiple-plantuml-diagrams-from-a-python-script

class py2puml_Generator:

    def __init__(self,src_root: Path,diagram_dir: str) -> None:
        self.src_root: Path = src_root
        self.diagram_dir = diagram_dir
        #Consider if the code duplication here and in pyrev_runner can be reduced.
        if not Path("Diagrams/").exists():
            os.mkdir("Diagrams")
        
        self.file_info = ""
        self._collect_file_info_from_root()

    def _collect_file_info_from_root(self) -> None:
        if self.src_root.is_file():
            if self.src_root.suffix == ".py":
                with self.src_root.open("r") as f:
                    self.file_info += f.read() + "\n"
        if self.src_root.is_dir():
            for file in self.src_root.iterdir():
                self._collect_file_info(file)
        return None
    
    def _collect_file_info(self,path: Path) -> str:
        if path.is_file():
            if path.suffix == ".py":
                with path.open("r") as f:
                    self.file_info += f.read() + "\n"
        if path.is_dir():
            for file in path.iterdir():
                self._collect_file_info(file)
        return None

    def create_diagram(self):
        p2p = py2puml(self.file_info)
        plantuml_code = p2p.get_puml()
        print(plantuml_code)