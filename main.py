from pathlib import Path
from scripts.hierarchy_extractor import FileHierarchyExtractor
from scripts.pyrev_runner import Pyrev
from scripts.python_to_puml import py2puml_Generator
from util.puml_to_svg import PUML_to_SVG
#from scripts.class_extractor import ClassExtractor
import click



@click.command()
@click.argument("src_root", required=True)
@click.option("--hierarchy",
                type=bool,
                required=False,
                help="Boolean determining if package diagram should be included in output",
                default=False)
@click.option("--pyrev",
                type=bool,
                required=False,
                help="Boolean determining if pyrev should be run",
                default=False)
@click.option("--py2puml",
                type=bool,
                required=False,
                help="Boolean determining if p2puml should be run",
                default=False)
def load(
    src_root: str,
    hierarchy: bool = False,
    pyrev: bool = False,
    py2puml: bool = False
):
    # Simple method for loading source root and passing to relevant scripts
    path_to_root = Path(src_root)
    if hierarchy:
        he: FileHierarchyExtractor = FileHierarchyExtractor(path_to_root)
        he.print_file_structure()
    
    if pyrev:
        pyr = Pyrev(src_root,"Diagrams")
        pyr.run()
    
    if py2puml:
        p2p = py2puml_Generator(path_to_root,"Diagrams")
        p2p.create_diagram()

    p2s = PUML_to_SVG("output")
    p2s.generate_svgs("Diagrams")

if __name__ == "__main__":
    load()