#!/usr/bin/env python3
"""Generate the analytical resource-regime figure as a native vector PDF.

Run from any directory:
    python3 generate_weight_memory_regimes.py

Canonical formulas (no fitting or simulation):
  R = w(n-k)/n.
  p_w = [sum_m binom(n-k,m) binom(k,w-m) 3^(w-m)] /
        [binom(n,w) 3^w].
  p_w^(-1) <= 3^R.
  Coherent lower-bound exponential factor = 2^[w(n-k)/(2(3n-w))].
The plotted factors omit all accuracy and confidence prefactors, ceilings,
and the logarithmic target-count cost. They are not optimal query counts.

Panel (a): n=256; every integer w=1,...,n and k=0,...,n.
           Contours R=c log2(n), c=1,2,4, are illustrative finite-n slices.
Panel (b): n=256,w=16; every integer deficit n-k=0,...,n.
           p_w is evaluated by exact integer arithmetic before taking logs.

Scientific homes: science/model.md; science/partial_bell.md (exact usability
probability and Jensen inequality); science/coherent_memory.md (Theorem C1).
"""
from fractions import Fraction
from math import comb, log2
from pathlib import Path
import argparse

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm, LinearSegmentedColormap
import numpy as np

N_QUBITS = 256
FIXED_W = 16
DEFAULT_OUTPUT = Path(__file__).resolve().parent / 'weight_memory_regimes.pdf'


def binom(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def usability(n, k, w):
    """Exact rational partial-Bell compatibility probability."""
    deficit = n - k
    numerator = sum(binom(deficit, m) * binom(k, w-m) * 3**(w-m)
                    for m in range(w+1))
    return Fraction(numerator, comb(n, w) * 3**w)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    output = args.output
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['STIXGeneral', 'Times New Roman', 'DejaVu Serif'],
        'mathtext.fontset': 'stix',
        'font.size': 9,
        'axes.labelsize': 9,
        'axes.titlesize': 9.5,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'legend.fontsize': 8,
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
        'axes.linewidth': .65,
        'lines.linewidth': 1.65,
        'xtick.major.width': .65,
        'ytick.major.width': .65,
        'savefig.facecolor': 'white',
    })
    fig = plt.figure(figsize=(7.0, 3.3), layout='constrained')
    grid = fig.add_gridspec(1, 2, width_ratios=(1.10, 1), wspace=.09)
    axa = fig.add_subplot(grid[0])
    axb = fig.add_subplot(grid[1])

    weights = np.arange(1, N_QUBITS+1)
    references = np.arange(N_QUBITS+1)
    ratio = weights[None, :] * (N_QUBITS-references[:, None]) / N_QUBITS / log2(N_QUBITS)
    norm = PowerNorm(gamma=.36, vmin=0, vmax=N_QUBITS/log2(N_QUBITS))
    # Filled analytical contours avoid the display seams of a dense vector mesh.
    levels = np.linspace(0, 1, 257)**(1/.36) * N_QUBITS/log2(N_QUBITS)
    mesh = axa.contourf(weights, references/N_QUBITS, ratio, levels=levels,
                        cmap=LinearSegmentedColormap.from_list('plmt', ['#163754', '#217E82', '#f0e3b4']), norm=norm, antialiased=False)
    mesh.set_edgecolor('face')
    mesh.set_linewidth(.35)
    axa.set_xscale('log', base=2)
    axa.set_xlim(1, N_QUBITS)
    axa.set_ylim(0, 1)
    axa.set_xticks([1, 4, 16, 64, 256], ['1', '4', '16', '64', '256'])
    axa.set_yticks([0, .25, .5, .75, 1])
    axa.set_xlabel(r'Maximum requested weight $w$')
    axa.set_ylabel(r'Coherent side-memory fraction $k/n$')
    axa.set_title(r'(a) Joint resource geometry: $n=256$', loc='left', pad=8)

    contour_styles = ('-', '--', ':')
    for c, style in zip((1, 2, 4), contour_styles):
        start = c*log2(N_QUBITS)
        wline = np.geomspace(start, N_QUBITS, 300)
        memory = 1-c*log2(N_QUBITS)/wline
        axa.plot(wline, memory, color='#ffffff', lw=1.15, ls=style)
        # Labels placed exactly on their analytical level curves.
        label_w = {1: 12, 2: 25, 4: 52}[c]
        label_y = 1-c*log2(N_QUBITS)/label_w
        axa.text(label_w, label_y+.022, rf'$c={c}$', color='white',
                 fontsize=8, ha='center', va='bottom',
                 bbox={'facecolor': '#333333', 'alpha': .65, 'edgecolor': 'none', 'pad': 1.5})
    axa.text(.97, .035, r'$R=c\log_2 n$', transform=axa.transAxes,
             ha='right', va='bottom', color='white', fontsize=8,
             bbox={'facecolor': '#333333', 'alpha': .75, 'edgecolor': 'none', 'pad': 2})
    colorbar = fig.colorbar(mesh, ax=axa, pad=.025, fraction=.045,
                            ticks=[0, 1, 2, 4, 8, 16, 32])
    colorbar.solids.set_rasterized(False)
    colorbar.solids.set_edgecolor('face')
    colorbar.set_label(r'$R/\log_2 n$', labelpad=4)
    colorbar.ax.tick_params(labelsize=7, width=.55, length=2.5)

    deficits = np.arange(N_QUBITS+1)
    exact_log2 = []
    for deficit in deficits:
        p = usability(N_QUBITS, N_QUBITS-int(deficit), FIXED_W)
        exact_log2.append(log2(p.denominator)-log2(p.numerator))
    exact_log2 = np.asarray(exact_log2)
    resource = FIXED_W*deficits/N_QUBITS
    jensen_log2 = resource*log2(3)
    coherent_log2 = FIXED_W*deficits/(2*(3*N_QUBITS-FIXED_W))
    axb.plot(deficits/N_QUBITS, jensen_log2, color='#ac782a', ls='--',
             label=r'Jensen factor $3^R$')
    axb.plot(deficits/N_QUBITS, exact_log2, color='#217e82',
             label=r'Exact construction factor $p_w^{-1}$')
    axb.plot(deficits/N_QUBITS, coherent_log2, color='#163754', ls='-.',
             label=r'Coherent converse factor')
    axb.set_xlim(0, 1)
    axb.set_ylim(0, 27)
    axb.set_xticks([0, .25, .5, .75, 1])
    axb.set_yticks([0, 5, 10, 15, 20, 25])
    axb.set_xlabel(r'Missing-memory fraction $1-k/n$')
    axb.set_ylabel(r'$\log_2$ of the indicated resource factor')
    axb.set_title(r'(b) Finite factors: $n=256,\ w=16$', loc='left', pad=8)
    axb.grid(axis='y', color='#dddddd', linewidth=.5)
    axb.set_axisbelow(True)
    axb.legend(loc='upper left', frameon=False, handlelength=2.2,
               borderaxespad=.5, labelspacing=.6)

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, metadata={
        'Title': 'Analytical weight-memory resource regimes',
        'Author': '',
        'Subject': 'Exact finite-parameter geometry and nonoptimal theorem factors',
        'Creator': 'generate_weight_memory_regimes.py; Matplotlib '+matplotlib.__version__,
        'CreationDate': None, 'ModDate': None,
    })
    assert np.max(exact_log2-jensen_log2) < 1e-11
    assert abs(exact_log2[0]) < 1e-12
    assert abs(exact_log2[-1]-FIXED_W*log2(3)) < 1e-11
    plt.close(fig)
    print('Wrote', output)
    print('n =', N_QUBITS, '; fixed w =', FIXED_W)
    print('Endpoint n-k=n: log2 exact usability factor =', exact_log2[-1])
    print('Endpoint n-k=n: log2 Jensen factor =', jensen_log2[-1])
    print('Endpoint n-k=n: log2 coherent factor =', coherent_log2[-1])
    print('Largest log2 exact-minus-Jensen =', float(np.max(exact_log2-jensen_log2)))


if __name__ == '__main__':
    main()

