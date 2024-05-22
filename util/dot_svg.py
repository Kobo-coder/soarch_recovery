from pathlib import Path
import subprocess
import os


class Dot_to_PNG:
      
    def __init__(self,diagram_dir: str,output_dir: str) -> None:
        self.diagram_dir = diagram_dir
        if not Path(diagram_dir).exists():
            os.mkdir(diagram_dir)
        self.output_dir = output_dir
        if not Path(output_dir).exists():
            os.mkdir(output_dir)


    def generate_pngs(self):
        #should not check if the folder has been made. Assumes this is done (maybe not the best decision)
        for file in Path(self.diagram_dir).iterdir():
            if file.suffix == ".dot":
                subprocess.run(["dot", "-Tpng", f"{self.diagram_dir}/{file.name}","-o", f"output/pyrev_{file.stem}.png"])