#for generation of plantuml diagrams
import os
from pathlib import Path
import pyan

# Inspired from:
# https://stackoverflow.com/questions/62980868/how-to-create-multiple-plantuml-diagrams-from-a-python-script

class Pyan_runner:

    def __init__(self,src_root: Path,diagram_dir: str,output_dir: str) -> None:
        self.src_root: Path = src_root
        self.diagram_dir = diagram_dir
        self.output_dir = output_dir
        #Consider if the code duplication here and in pyrev_runner can be reduced.
        if not Path("Diagrams/").exists():
            os.mkdir("Diagrams")
        
        self.file_info = []
        self._collect_file_info_from_root()

    #The structure of this is repeated several times. Possible to remove duplication?
    def _collect_file_info_from_root(self) -> None:
        if self.src_root.is_file():
            if self.src_root.suffix == ".py":
                self.file_info.append(str(self.src.root))
        if self.src_root.is_dir():
            for file in self.src_root.iterdir():
                self._collect_file_info(file)
        return None
    
    def _collect_file_info(self,path: Path) -> str:
        if path.is_file():
            if path.suffix == ".py":
                self.file_info.append(str(path))
        if path.is_dir():
            for file in path.iterdir():
                self._collect_file_info(file)
        return None

    def create_diagram(self):
        print(self.file_info)
        callgraph = pyan.create_callgraph(self.file_info, format='svg')
        with open(f'{self.output_dir+"/pyan.svg"}', 'w') as svg:
            svg.write(callgraph)