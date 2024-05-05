from pathlib import Path
import subprocess
import os


class PUML_to_SVG:
      
    def __init__(self,output_dir: str) -> None:
        self.output_dir = output_dir
        if not Path("output/").exists():
            os.mkdir("output")


    def generate_svgs(self,diagram_path: Path):
        #should not check if the folder has been made. Assumes this is done (maybe not the best decision)
        for file in Path(diagram_path).iterdir():
            if file.suffix == ".puml":
                with file.open("rb") as f:
                    jarpath = "jar/plantuml.jar"
                    res = subprocess.run(["java", "-jar", jarpath, "-tsvg", "-pipe"],input=f.read(),capture_output=True)
                    with open(f'{self.output_dir+"/"+file.stem+".svg"}', 'w') as svg:
                        towrite = str(res.stdout)
                        start_index = towrite.find('<svg')
                        end_index = towrite.find('</svg>') + len('</svg>')
                        content = towrite[start_index:end_index]
                        svg.write(content)
                    p = f'{self.output_dir+"/"+file.stem+".svg"}'
                    subprocess.run(["open", p])