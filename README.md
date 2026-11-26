# The Fate of Conserved Water

LaTeX source for a framework paper by Jonathan Yoder (School of Economic Sciences, Washington State University). The paper traces what happens to water that a conservation program reports as saved. It separates savings that reduce depletion ("wet") from savings that only remove return flow ("dry"), follows the freed water to its destinations (protection, rebound, transfer, banking), and places the gains and losses in space and time. The paper then derives a typology of practices and draws each case as a two-ledger Sankey diagram.

Status: working draft for a journal submission.

## Where to edit

The Overleaf project is the copy that Jon and co-authors edit by hand. This repository mirrors it through Overleaf's git bridge, so the two stay in step. If you edit here, merge Overleaf's latest version first and push the result back to Overleaf (see `CLAUDE.md`).

## Files

| Path | Contents |
| --- | --- |
| `main.tex` | The manuscript: one file, `article` class, natbib author-year citations. |
| `practitioner.tex` | Placeholder for a plain-language companion: the same framework in words, with no equations, for water managers and program staff. Candidate venues: *The Water Report* and the *Journal of Contemporary Water Research & Education*. Shares `refs.bib` and `figures/`. |
| `refs.bib` | Bibliography. `wadraft2026` is a placeholder for an unpublished 2026 Washington conservation report. |
| `figures/classification.tex` | TikZ flowchart that assigns a practice code (Figure 1). |
| `figures/sankey_data.csv` | Flow values for the Sankey panels. |
| `figures/make_sankey.py` | Script that draws `figures/sankey.pdf` from the CSV. |
| `figures/sankey.pdf` | Two-ledger Sankey figure (Figure 2), committed because Overleaf cannot run Python. |
| `CLAUDE.md` | Conventions and the Overleaf sync workflow for Claude Code sessions. |

## Build

Overleaf compiles one main document at a time; choose `main.tex` or `practitioner.tex` under Menu → Main document. To compile locally with TeX Live, run from the project root:

```bash
latexmk -pdf main.tex
```

```bash
latexmk -pdf practitioner.tex
```

To redraw the Sankey figure after editing `figures/sankey_data.csv` (needs Python with matplotlib):

```bash
python figures/make_sankey.py
```

Commit the regenerated `figures/sankey.pdf` so that Overleaf picks it up.

## Notation at a glance

| Symbol | Meaning |
| --- | --- |
| $W = D + R$ | Withdrawal splits into depletion and recoverable return flow (Equation 1). |
| $D = C_b + C_n + N$ | Depletion: beneficial consumption, non-beneficial consumption, non-recoverable outflow. |
| States 0, τ, 1 | Before the practice; practice in place with freed water unused; after the freed water reaches its destinations. |
| $F = -\Delta^{\tau}W$ | Freed withdrawal, the saving programs usually report (Equation 3). |
| $F_{\mathrm{wet}} = -\Delta^{\tau}D$, $F_{\mathrm{dry}} = -\Delta^{\tau}R$ | The parts of $F$ that reduce depletion and that only remove return flow. |
| $\lambda_s, \lambda_u, \lambda_t, \lambda_b$ | Shares of $F$ that are protected, re-applied (rebound), transferred, and banked. |
| $\Delta D = -F_{\mathrm{wet}} + F\sum_i \lambda_i d_i$ | Change in basin depletion (Equation 4). |
| $\varphi = -\Delta D / F$ | Efficacy ratio: the share of the reported saving that becomes basin water. |

The preamble of `main.tex` defines macros for this notation (`\Cb`, `\Cn`, `\Fwet`, `\Fdry`, `\dtau`, `\ind`). Use them so that notation stays consistent.

## Worked example

Section 7 uses an illustrative 100-unit irrigation diversion; the numbers are not estimates. The scenario table (`tab:scenarios`), the Sankey CSV, and the prose in Sections 6 and 7 share these numbers. If one changes, update all three.

## Related repositories

- [`yoderwsu/water-conservation-tool`](https://github.com/yoderwsu/water-conservation-tool): the Conserved Water Ledger, an interactive what-if tool built on the paper's equations. Its tests reproduce the scenario table (`tab:scenarios`), so a change to the paper's model or numbers needs a matching change there.
- [`yoderwsu/writing-standards`](https://github.com/yoderwsu/writing-standards): the writing standard and style checker used for the manuscript's prose.
