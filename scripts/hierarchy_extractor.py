from pathlib import Path
from anytree import Node, RenderTree

_ignored_files = Path("util/ignored_files.txt")

class FileHierarchyExtractor:

    def __init__(self, src_root: Path):
        self.src_root: Path = src_root
        self.ignored_types = self._get_ignored_file_types()
        self.tree = self._init_tree()
    
    def print_file_structure(self):
        # Idea from following: https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python
        for pre, _, node in RenderTree(self.tree):
            print("%s%s" % (pre, node.name))

    def _init_tree(self) -> Node:
        # Consider if there is a better way to ensure that we always account for parent nodes
        # find better way to get suffix along with file name
        root = Node(f"{self.src_root.stem}")
        if self.src_root.is_file():
            root.name = root.name+self.src_root.suffix
            return root
        if self.src_root.is_dir():
            for p in self.src_root.iterdir():
                # Should return be used for anything?
                self._populate_tree(p,root)
        return root

        
    def _populate_tree(self,path: Path,parent: Node) -> Node:
        if self._check_ignored(path):
            return None
        if path.is_file():
            return Node(f"{path.stem+path.suffix}",parent=parent)
        if path.is_dir():
            node = Node(f"{path.stem}",parent=parent)
            for p in path.iterdir():
                self._populate_tree(p,node)


    def _check_ignored(self,path: Path) -> bool:
        for ignore in self.ignored_types:
                if path.match(ignore):
                    return True
        return False

    def _get_ignored_file_types(self):
        # Inspired from own bachelor project
        ignored_files = []
        if not _ignored_files.exists():
            return ignored_files

        with _ignored_files.open("r") as file:
            for line in file:
                ignored_files.append(line.rstrip())

        return ignored_files