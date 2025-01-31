from pathlib import Path
from os import scandir
""" 
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
 """""" 
red_patch = mpatches.Patch(color='red', label='Changed tickets', alpha=0.5)
green_patch = mpatches.Patch(color='green', label='Unchanged tickets', alpha=0.5)
 """
pulled_repos_path = "C:\\D_Drive\\Trojan_horse\\jupyter\\python_repos_analysis\\pulled_repos"

# A function that generates a graph of the indentation in the files. Probably a lot of them overlayed?

def analyse_file(path_to_file: str) -> float:
    """Return the average indentation level in spaces per line (tabs counted as 4 spaces)."""
    total_indent = 0
    total_lines = 0

    with open(path_to_file, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.lstrip()
            if not stripped:  # Skip empty lines
                continue
            indent_size = len(line.expandtabs(4)) - len(stripped.expandtabs(4))
            total_indent += indent_size
            total_lines += 1

    return total_indent / total_lines if total_lines > 0 else 0

""" 
def chart1(xs: list[int], ys: list[bool]):
    _fig, ax = plt.subplots(figsize=(10, 3))
    ax.legend(handles=[red_patch, green_patch])

    # Mapping bools to categories
    x_labels = ["real" if b else "unreal" for b in ys]

    # Creating the plot
    plt.figure(figsize=(5, 6))
    plt.scatter(x_labels, xs, color=["green" if y else "red" for y in ys], s=50)

    # Labels and title
    plt.xlabel("Category")
    plt.ylabel("Values")
    plt.title("Real vs Unreal Values")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.show()
 """
def run():
    subfolders = [f.path for f in scandir(pulled_repos_path) if f.is_dir()]
    indentations = []
    is_real = []
    for folder in subfolders:
        pathlist = Path(folder).rglob("*.py")

        total_indentation = 0.0
        file_count = 0

        for path in pathlist:
            total_indentation += analyse_file(str(path))
            file_count += 1

        average_indentation = total_indentation / file_count if file_count > 0 else 0

        # Correct path handling for result file
        result_file = Path(folder) / "result"
        is_real_project = result_file.exists() and result_file.read_text().strip() == "True"
        indentations.append(average_indentation)
        is_real.append(is_real_project)
        print(f"average_indentation = {average_indentation}")
        print(f"is_real_project = {is_real_project}")

        with open(Path(folder) / "identation", "w") as file:
            file.write(f"average_indentation = {average_indentation}\n")
            #file.write(f"is_real_project = {is_real_project}")
    # chart1(indentations, is_real)
run()