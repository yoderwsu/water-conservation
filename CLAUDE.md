# The Fate of Conserved Water — manuscript repo

Jon Yoder (Washington State University). A conceptual framework paper on what happens to "conserved" water: consumptive vs non-consumptive savings, the fate of freed water (protection, rebound, transfer, banking), and timing/location effects, with a typology and two-ledger Sankey diagrams. The target is a journal manuscript; it is written in LaTeX and edited in Overleaf.

## Files

- `main.tex` — the manuscript. Single file, `article` class, natbib author-year (`\citep`, `\citet`).
- `refs.bib` — bibliography. Entry `wadraft2026` is a placeholder for an unpublished 2026 Washington conservation report; replace it once Jon supplies authors and agency (see its TODO note).
- `figures/classification.tex` — TikZ classification flowchart, `\input` by main.tex.
- `figures/make_sankey.py` + `figures/sankey_data.csv` → `figures/sankey.pdf`. Edit the CSV and rerun `python figures/make_sankey.py`; commit the regenerated PDF (Overleaf can't run Python).

## Conventions

- Equations are numbered automatically. Labels: `eq:partition` (1), `eq:change` (2), `eq:freed` (3), `eq:fate` (4), `eq:routing` (5). Always refer with `Equation~\eqref{...}`; never type an equation number.
- Notation macros are defined in the preamble (`\Cb`, `\Cn`, `\Fwet`, `\Fdry`, `\Dnet`, `\ind`). Use them so notation stays consistent.
- The worked-example numbers (100-unit diversion, Table `tab:scenarios`, Figure `fig:sankey`) are illustrative, not estimates. If one number changes, recheck the table, the Sankey CSV, and the prose in sections 6–7 together: F = F_wet + F_dry, ΔD_net = −F_wet + F·Σλ_i·d_i, φ = −ΔD_net / F.
- Jon's writing standards live in the GitHub repo `yoderwsu/writing-standards`; follow them for prose edits if available.
- History: the framework was first drafted in a Claude Doc (https://claude.ai/artifact/McytXLpAynyy4Z8cc2zNWe). This repo is now the source of truth; don't edit the Doc in parallel.

## Overleaf workflow (direct git, no GitHub Sync)

Jon's Overleaf project is the copy he and co-authors edit by hand. Keep it in step with this repo over Overleaf's git bridge.

- Remote: `https://git.overleaf.com/<PROJECT_ID>` (the ID is the last part of the Overleaf project URL; ask Jon if it isn't set yet). Overleaf's branch is `master`.
- Auth: the cloud environment has a network secret for `git.overleaf.com` (username `git`, Overleaf git token as password), attached by the agent proxy. Never ask Jon to paste the token into chat. If git reports an auth failure, the secret is missing or uses the wrong secret type; tell Jon rather than working around it.

First connection (Overleaf project created blank, so it has an unrelated starter commit):

```bash
git remote add overleaf https://git.overleaf.com/<PROJECT_ID>
git fetch overleaf
git merge overleaf/master --allow-unrelated-histories -X ours -m "Merge Overleaf starter project"
# keep this repo's main.tex; delete any Overleaf starter files we don't use, then commit
git push overleaf HEAD:master
```

Every session after that:

1. `git fetch overleaf && git merge overleaf/master` first — Jon may have edited in Overleaf. Resolve conflicts in his favor unless he says otherwise.
2. Make the requested changes; compile to check (`latexmk -pdf main.tex`) if TeX is installed in the environment, otherwise rely on Overleaf's compile and say so.
3. Commit, then `git push overleaf HEAD:master` and push the session branch to GitHub.
4. Tell Jon what changed in plain terms; he reads the result in Overleaf.

Don't force-push to Overleaf.
