"""Draw the two-ledger Sankey figure (figures/sankey.pdf) from figures/sankey_data.csv.

Run from the repository root:  python figures/make_sankey.py
Left column  = point-of-use fate of the diversion (one node per `part`).
Right column = what the basin sees (`basin`: early / late / dep).
Colors mark the basin fate, not the practice.
"""
import csv
from collections import OrderedDict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.path import Path as MPath

HERE = Path(__file__).resolve().parent
DATA = HERE / "sankey_data.csv"
OUT = HERE / "sankey.pdf"

BASINS = OrderedDict([("early", "Early in river"),
                      ("late", "Late, via aquifer"),
                      ("dep", "Depleted (ET)")])
BLUE, GREY = "#2f6db5", "#8c8c86"
COLOR = {"early": (BLUE, 0.35, 0.18), "late": (BLUE, 0.95, 0.45), "dep": (GREY, 0.85, 0.25)}
GAP = 7.0            # vertical gap between nodes, in flow units
XL, XR, NW = 0.36, 0.64, 0.025  # left node x, right node x, node width (axes fraction)

rows = list(csv.DictReader(open(DATA, encoding="utf-8")))
for r in rows:
    r["value"] = float(r["value"])
scenarios = list(OrderedDict.fromkeys(r["scenario"] for r in rows))
base_dep = sum(r["value"] for r in rows if r["scenario"] == "base" and r["basin"] == "dep")

plt.rcParams.update({"font.family": "serif", "font.size": 7.5, "pdf.fonttype": 42})
fig, axes = plt.subplots(2, 2, figsize=(7.2, 6.2))

for ax, sc in zip(axes.flat, scenarios):
    part_rows = [r for r in rows if r["scenario"] == sc]
    total = sum(r["value"] for r in part_rows)
    height = total + GAP * (len(part_rows) - 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(height + 4, -10)
    ax.axis("off")
    ax.text(0.0, -6, part_rows[0]["label"], fontsize=8, fontweight="bold", va="bottom")

    # left nodes
    y, left_pos = 0.0, {}
    for r in part_rows:
        left_pos[r["part"]] = y
        y += r["value"] + GAP

    # right nodes (vertically centered against the left column)
    totals = OrderedDict((b, sum(r["value"] for r in part_rows if r["basin"] == b)) for b in BASINS)
    right_h = sum(totals.values()) + GAP * (len(totals) - 1)
    y = (height - right_h) / 2
    right_pos = {}
    for b, t in totals.items():
        right_pos[b] = y
        y += t + GAP

    # links
    fill_in_right = {b: right_pos[b] for b in BASINS}
    for r in part_rows:
        v = r["value"]
        if v <= 0:
            continue
        col, _, link_alpha = COLOR[r["basin"]]
        a0, a1 = left_pos[r["part"]], left_pos[r["part"]] + v
        b0 = fill_in_right[r["basin"]]; b1 = b0 + v
        fill_in_right[r["basin"]] = b1
        x0, x1, xm = XL + NW, XR, (XL + NW + XR) / 2
        verts = [(x0, a0), (xm, a0), (xm, b0), (x1, b0), (x1, b1), (xm, b1), (xm, a1), (x0, a1), (x0, a0)]
        codes = [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4, MPath.LINETO,
                 MPath.CURVE4, MPath.CURVE4, MPath.CURVE4, MPath.CLOSEPOLY]
        ax.add_patch(PathPatch(MPath(verts, codes), facecolor=col, alpha=link_alpha, lw=0))

    # left node bars and labels
    for r in part_rows:
        col, node_alpha, _ = COLOR[r["basin"]]
        v = r["value"]
        ax.add_patch(Rectangle((XL, left_pos[r["part"]]), NW, max(v, 0.6), facecolor=col, alpha=node_alpha, lw=0))
        ax.text(XL - 0.015, left_pos[r["part"]] + v / 2, f"{r['part_label']} {v:g}", ha="right", va="center",
                color="black" if v > 0 else "0.5")

    # right node bars and labels
    for b, t in totals.items():
        col, node_alpha, _ = COLOR[b]
        ax.add_patch(Rectangle((XR, right_pos[b]), NW, max(t, 0.6), facecolor=col, alpha=node_alpha, lw=0))
        label = f"{BASINS[b]} {t:g}"
        weight = "normal"
        if b == "dep":
            weight = "bold"
            if sc != "base":
                d = t - base_dep
                label += f", $\\Delta$ {'+' if d > 0 else '−'}{abs(d):g}"
        ax.text(XR + NW + 0.015, right_pos[b] + t / 2, label, ha="left", va="center", fontweight=weight)

fig.tight_layout(rect=(0, 0, 1, 0.97), h_pad=2.0, w_pad=1.0)
fig.savefig(OUT, bbox_inches="tight")
print(f"wrote {OUT}")
