# The Fate of Conserved Water — manuscript repo

Jon Yoder (Washington State University). A conceptual framework paper on what happens to "conserved" water: consumptive vs non-consumptive savings, the fate of freed water (protection, rebound, transfer, banking), and timing/location effects, with a typology and two-ledger Sankey diagrams. The target is a journal manuscript; it is written in LaTeX and edited in Overleaf.

## Files

- `main.tex` — the manuscript. Single file, `article` class, natbib author-year (`\citep`, `\citet`).
- `refs.bib` — bibliography. Entry `wadraft2026` is a placeholder for an unpublished 2026 Washington conservation report; replace it once Jon supplies authors and agency (see its TODO note).
- `practitioner.tex` — plain-language companion (placeholder; sections are outlined with visible `\todo{}` notes). No equations or symbols in its running text: it uses the words in its glossary table, each mapped to one symbol in main.tex. Same worked-example numbers as main.tex Section 7. Shares `refs.bib` and `figures/`; compile from the root with `latexmk -pdf practitioner.tex`. When main.tex notation, typology, or example numbers change, update this file to match. Target venues (The Water Report, JCWRE) have not been checked for format yet; ucowr.org was not reachable from the cloud environment.
- `figures/classification.tex` — TikZ classification flowchart, `\input` by main.tex.
- `figures/make_sankey.py` + `figures/sankey_data.csv` → `figures/sankey.pdf`. Edit the CSV and rerun `python figures/make_sankey.py`; commit the regenerated PDF (Overleaf can't run Python).

## Conventions

- Equations are numbered automatically. Labels: `eq:partition` (1), `eq:change` (2), `eq:freed` (3), `eq:fate` (4), `eq:routing` (5). Always refer with `Equation~\eqref{...}`; never type an equation number.
- Notation macros are defined in the preamble (`\Cb`, `\Cn`, `\Fwet`, `\Fdry`, `\dtau`, `\ind`). Use them so notation stays consistent.
- States: 0 (before), τ (practice in place, freed water not yet used; counterfactual), 1 (after disposition). `\dtau X` = X^τ − X^0; plain Δ is state 1 minus state 0. F ≡ −Δ^τW, F_wet ≡ −Δ^τD, F_dry ≡ −Δ^τR. There is no F_X family and no ΔD_net; the net basin effect is ΔD.
- Typology: Type A if Δ^τC_b < 0 (service cut); otherwise B if F_wet > F_dry, C if F_dry > F_wet; D if F ≈ 0.
- The worked-example numbers (100-unit diversion, Table `tab:scenarios`, Figure `fig:sankey`) are illustrative, not estimates. If one number changes, recheck the table, the Sankey CSV, and the prose in sections 6–7 together: F = F_wet + F_dry, ΔD = −F_wet + F·Σλ_i·d_i, φ = −ΔD / F.
- Jon's writing standards live in the GitHub repo `yoderwsu/writing-standards`; follow them for prose edits if available.
- The interactive what-if tool lives in its own repo, `yoderwsu/water-conservation-tool`. Its model mirrors these equations and its tests pin Table `tab:scenarios`; change both together.
- History: the framework was first drafted in a Claude Doc (https://claude.ai/artifact/McytXLpAynyy4Z8cc2zNWe). This repo is now the source of truth; don't edit the Doc in parallel.

## Overleaf workflow (direct git, no GitHub Sync)

Jon's Overleaf project is the copy he and co-authors edit by hand. Keep it in step with this repo over Overleaf's git bridge.

- Remote: `https://git.overleaf.com/6b073d3b2eeea9deb5f6f6ef`. Overleaf's branch is `main` (not `master`).
- Auth: the cloud environment has a network secret for `git.overleaf.com` (type Basic, username `git`, Overleaf git token `olp_…` as password), attached by the agent proxy. Never ask Jon to paste the token into chat.
- Git won't send a request until it has credentials, so give it placeholders that the proxy overwrites. Each new container needs this once (it lives in the local git config, not the repo):

```bash
git remote add overleaf https://git.overleaf.com/6b073d3b2eeea9deb5f6f6ef   # if missing
git config credential.https://git.overleaf.com.helper '!f() { echo username=git; echo password=proxy-injected; }; f'
```

- If git still reports `Authentication failed`, the secret is wrong: missing, wrong type, username not `git`, or a bad token. Tell Jon rather than working around it.

First connection was done 2026-11-25 (Overleaf starter commit merged with `-X ours`; this repo's files kept).

Every session after that:

1. `git fetch overleaf && git merge overleaf/main` first — Jon may have edited in Overleaf. Resolve conflicts in his favor unless he says otherwise.
2. Make the requested changes; compile to check (`latexmk -pdf main.tex`) if TeX is installed in the environment, otherwise rely on Overleaf's compile and say so.
3. Commit, then `git push overleaf HEAD:main`, push the session branch to GitHub, and also update GitHub's `main` with `git push origin HEAD:main` (Jon approved this so GitHub `main` stays a current copy of the Overleaf version). If that push is rejected because GitHub `main` has commits this session lacks, fetch and merge `origin/main`, then push again; never force-push.
4. Tell Jon what changed in plain terms; he reads the result in Overleaf.

Don't force-push to Overleaf.
