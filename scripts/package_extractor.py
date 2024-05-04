from pathlib import Path
from anytree import Node, RenderTree

class PackageExtractor:

    def __init__(self, src_root: Path):
        self.src_root: Path = src_root
        print(str(src_root))
        self.tree = self._init_tree()
    
    def print_package_structure(self):
        for pre, _, node in RenderTree(self.tree):
            print("%s%s" % (pre, node.name))

    def _init_tree(self) -> Node:
        # Consider if there is a better way to ensure that we always account for parent nodes
        root = Node(f"{self.src_root.stem}")
        if self.src_root.is_file():
            return root
        if self.src_root.is_dir():
            for p in self.src_root.iterdir():
                # Should return be used for anything?
                self._populate_tree(p,root)
        return root

        
    def _populate_tree(self,path: Path,parent: Node) -> Node:
        node = Node(f"{path.stem}",parent=parent)
        if path.is_file():
            return node
        if path.is_dir():
            for p in path.iterdir():
                self._populate_tree(p,node)

        return None