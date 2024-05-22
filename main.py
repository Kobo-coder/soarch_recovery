from pathlib import Path
from scripts.hierarchy_extractor import FileHierarchyExtractor
from scripts.pyrev_runner import Pyrev
from scripts.pyan_runner import Pyan_runner
from scripts.python_to_puml import py2puml_Generator
from util.opener import Opener
from util.puml_to_svg import PUML_to_SVG
from util.dot_svg import Dot_to_PNG
import click



@click.command()
@click.argument("src_root", required=True)
@click.option("--hierarchy",
                type=bool,
                required=False,
                help="Boolean determining if package diagram should be included in output",
                default=False)
@click.option("--conv_puml",
                type=bool,
                required=False,
                help="Boolean determining if PlantUML files residing in Diagrams/ should be converted to SVG",
                default=False)
@click.option("--pyrev",
                type=bool,
                required=False,
                help="Boolean determining if pyrev should be run on given source root",
                default=False)
@click.option("--py2puml",
                type=bool,
                required=False,
                help="Boolean determining if p2puml should be run on given source root",
                default=False)
@click.option("--pyan",
                type=bool,
                required=False,
                help="Boolean determining if pyan should be run on given source root",
                default=False)
@click.option("--show",
                type=bool,
                required=False,
                help="Boolean determining if svgs in output should be opened",
                default=False)
@click.option("--dot",
                type=bool,
                required=False,
                help="Boolean determining if dot files in the diagram folder should be converted to png",
                default=False)
def load(
    src_root: str,
    hierarchy: bool = False,
    pyrev: bool = False,
    py2puml: bool = False,
    pyan: bool = False,
    conv_puml: bool = False,
    show: bool = False,
    dot: bool = False
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

    if pyan:
        pyp = Pyan_runner(path_to_root,"Diagrams","output")
        pyp.create_diagram()

    if conv_puml:
        p2s = PUML_to_SVG("output")
        p2s.generate_svgs("Diagrams")

    if dot:
        dot = Dot_to_PNG("Diagrams","output")
        dot.generate_pngs()


    # Should probably make it so output can be given as an argument rather than hard coded
    if show:
        op = Opener("output")
        op.open_figures()


if __name__ == "__main__":
    load()