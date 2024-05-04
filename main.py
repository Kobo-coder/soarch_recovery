from pathlib import Path
from scripts.package_extractor import PackageExtractor
from scripts.class_extractor import ClassExtractor
import click

@click.command()
@click.argument("src_root", required=True)
@click.option("--package",
                type=bool,
                required=False,
                help="Boolean determining if package diagram should be included in output",
                default=False)
def load(
    src_root: str,
    package: bool = False
):
    # Simple method for loading source root and passing to relevant scripts
    path_to_root = Path(src_root)
    if package:
        pe: PackageExtractor = PackageExtractor(path_to_root)
        pe.print_package_structure()

    

if __name__ == "__main__":
    load()