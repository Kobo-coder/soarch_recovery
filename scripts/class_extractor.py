from pathlib import Path
from anytree import Node, RenderTree

class ClassExtractor:

    def __init__(self, src_root: Path):
        self.src_root: Path = src_root