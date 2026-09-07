from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np


# Salary structure data for KIG (B.E. 2569 / 2026), Job Grade 2-16
GRADES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

DATA = {
    "5 days/week": {
        "Probation": [10710, 12200, 13900, 15800, 17100, 20700, 25100, 28700, 35900, 53900, 71800, 97000, 140100, 183300, 256700],
        "Permanent": [11300, 12800, 14600, 16600, 18000, 21700, 26500, 30200, 37800, 56700, 75600, 102100, 147500, 193000, 270200],
        "Max": [19800, 22400, 25600, 29000, 31400, 43500, 52900, 60500, 75600, 113400, 151200, 229600, 331900, 434200, 607900],
    },
    "5.5 days/week": {
        "Probation": [11300, 12800, 14600, 16600, 18100, 21800, 26500, 30300, 37900, 56900, 75800, 102300, 147900, 193500, 270900],
        "Permanent": [11900, 13500, 15400, 17500, 19000, 22900, 27900, 31900, 39900, 59800, 79800, 107700, 155700, 203700, 285200],
        "Max": [20800, 23600, 27000, 30600, 33200, 45900, 55900, 63800, 79800, 119700, 159600, 242400, 350300, 458300, 641700],
    },
    "6 days/week": {
        "Probation": [12000, 13500, 15400, 17500, 19000, 23000, 27900, 31900, 39900, 59800, 79800, 107700, 155700, 203700, 285200],
        "Permanent": [12600, 14200, 16200, 18400, 20000, 24200, 29400, 33600, 42000, 63000, 84000, 113400, 163900, 214400, 300200],
        "Max": [22000, 24800, 28400, 32200, 34900, 48300, 58800, 67200, 84000, 126000, 168000, 255200, 368800, 482400, 675400],
    },
}

PANEL_COLORS = ["#A5D6A7", "#B39DDB", "#FFCC80"]
POINT_COLOR = "#0D47A1"


def money_fmt(x, _):
    return f"{int(x):,}"


def create_infographic(output_file: str) -> None:
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(1, 3, figsize=(16, 9), dpi=100, sharey=True)
    fig.patch.set_facecolor("#F7F9FC")

    ordered_grades = list(reversed(GRADES))
    y = np.arange(len(ordered_grades))

    for idx, (title, values) in enumerate(DATA.items()):
        ax = axes[idx]
        trial = np.array(list(reversed(values["Probation"])))
        regular = np.array(list(reversed(values["Permanent"])))
        maxv = np.array(list(reversed(values["Max"])))
        span = maxv - trial

        ax.barh(
            y,
            span,
            left=trial,
            color=PANEL_COLORS[idx],
            edgecolor="#546E7A",
            linewidth=0.8,
            alpha=0.9,
        )
        ax.scatter(regular, y, s=22, color=POINT_COLOR, zorder=3)

        ax.set_title(title, fontsize=15, weight="bold", pad=12)
        ax.set_yticks(y)
        ax.set_yticklabels([f"Grade {g}" for g in ordered_grades], fontsize=11)
        ax.xaxis.set_major_formatter(FuncFormatter(money_fmt))
        ax.tick_params(axis="x", labelsize=9)
        ax.grid(axis="x", linestyle="--", alpha=0.25)
        ax.set_axisbelow(True)
        ax.set_facecolor("#FFFFFF")

        for spine in ax.spines.values():
            spine.set_color("#CFD8DC")

        ax.text(
            0.02,
            0.02,
            "Range: Probation to Max\nBlue dot: Permanent",
            transform=ax.transAxes,
            fontsize=9,
            color="#455A64",
            va="bottom",
        )

    axes[0].set_ylabel("Job Grade", fontsize=12, weight="bold")

    fig.suptitle(
        "KIG Salary Structure (B.E. 2569 / 2026)",
        fontsize=24,
        weight="bold",
        y=0.975,
        color="#1A237E",
    )
    fig.text(
        0.5,
        0.925,
        "By Work Schedule",
        ha="center",
        fontsize=22,
        weight="bold",
        color="#1A237E",
    )
    fig.text(
        0.5,
        0.885,
        "Infographic: Salary Ranges by Job Grade (Probation / Permanent / Max)",
        ha="center",
        fontsize=13,
        color="#37474F",
    )
    fig.text(
        0.99,
        0.02,
        "Source: KIG salary structure table (B.E. 2569)",
        ha="right",
        fontsize=10,
        color="#607D8B",
    )

    plt.tight_layout(rect=[0.02, 0.06, 0.98, 0.83])
    fig.savefig(output_file, dpi=100)


if __name__ == "__main__":
    create_infographic("/workspace/salary-structure-infographic-1600x900.png")
