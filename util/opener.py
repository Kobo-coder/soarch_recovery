from pathlib import Path
import subprocess
import os


class Opener:
      
    def __init__(self,output_dir: str) -> None:
        self.output_dir = output_dir
        if not Path("output/").exists():
            os.mkdir("output")


    def open_figures(self):
        #should not check if the folder has been made. Assumes this is done (maybe not the best decision)
        for file in Path(self.output_dir).iterdir():
            if file.suffix == ".svg":
                p = f'{self.output_dir+"/"+file.stem+".svg"}'
                #Does this work for all OS or just unix based ones??? -> More likely the latter
                subprocess.run(["open", p])