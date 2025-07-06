from pathlib import Path
from os import scandir

import numpy as np

pulled_repos_path = "/home/vojtechnovotny/school/code-depth-analysis/pulled_repos"
indentations_counts = []
is_real = []
# A function that generates a graph of the indentation in the files. Probably a lot of them overlayed?

def analyse_file(path_to_file: str, indents: list[int]) -> float:
    """Return the average indentation level in spaces per line (tabs counted as 4 spaces)."""

    with open(path_to_file, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.lstrip()
            if not stripped:  # Skip empty lines
                continue
            indent_size = len(line.expandtabs(4)) - len(stripped.expandtabs(4))
            indents.append(indent_size)

def calculate_indentations():
    subfolders = [f.path for f in scandir(pulled_repos_path) if f.is_dir()]
    for folder in subfolders:
        pathlist = Path(folder).rglob("*.py")

        indents_total = []
        for path in pathlist:
            indents = []
            analyse_file(str(path), indents)
            indents_total.extend(indents)
        indentations_counts.append(np.array(indents_total))

def read_results():
    global is_real

    subfolders = [f.path for f in scandir(pulled_repos_path) if f.is_dir()]
    for folder in subfolders:
        # Correct path handling for result file
        result_file = Path(folder) / "result"
        is_real_project = result_file.exists() and result_file.read_text().strip().lower() == "true"
        is_real.append(is_real_project)
