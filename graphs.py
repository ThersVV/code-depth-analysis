
from matplotlib import pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

red_patch = mpatches.Patch(color='red', label='Changed tickets', alpha=0.5)
green_patch = mpatches.Patch(color='green', label='Unchanged tickets', alpha=0.5)

def chart(indents: list[int], name: str, reals: list[bool]):

    # Mapping bools to categories
    x_labels = ["Real" if b else "Unreal" for b in reals]

    # Creating the plot
    plt.figure(figsize=(1, 4))
    plt.scatter(x_labels, indents, color=["green" if y else "red" for y in reals], s=50)

    # Labels and title
    plt.ylabel("Indentation deviation")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.show()
