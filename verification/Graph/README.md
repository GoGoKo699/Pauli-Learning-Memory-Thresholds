# Weight and coherent-memory figure

The [vector plot](weight_memory_regimes.pdf) shows the joint resource parameter $`R=w(n-k)/n`$ and the finite factors in the learning bounds. Here $`n`$ is the number of queried qubits, $`k`$ is the coherent side width at each invocation, and $`w`$ is the maximum requested Pauli weight. The missing reference width is written $`n-k`$; $`D`$ is reserved for the complete processor dimension in the no-reset comparison.

## Reproduce

From the repository root:

```bash
python3 -m pip install -r verification/Graph/requirements.txt
python3 verification/Graph/generate_weight_memory_regimes.py
```

The default output is `verification/Graph/weight_memory_regimes.pdf`, independent of the working directory. Use `--output PATH` for another destination. The dependencies are pinned to NumPy 2.3.5 and Matplotlib 3.10.8. PDF creation/modification dates are omitted for reproducible output.

## Panels and values

Panel (a) fixes $`n=256`$ and evaluates $`R/\log_2n`$ for every integer $`1\le w\le n`$ and $`0\le k\le n`$. The curves $`R=c\log_2n`$, $`c=1,2,4`$, are illustrative finite-parameter levels of the asymptotic polynomial-query condition $`R=O(\log n)`$.

Panel (b) fixes $`n=256,w=16`$ and varies $`n-k`$. Its exact construction factor is the reciprocal of

```math
p_w=\frac{\sum_{m=0}^w\binom{n-k}{m}\binom{k}{w-m}3^{w-m}}
           {\binom nw3^w}.
```

An out-of-range binomial coefficient is zero. The generator evaluates this expression with exact integers and rational reduction before taking logarithms. It compares $`\log_2(p_w^{-1})`$ with $`R\log_2 3`$ and the coherent-converse exponent $`w(n-k)/[2(3n-w)]`$. The full query bounds also include accuracy, confidence, ceilings and target-count factors; these curves display the indicated factors.

At $`k=n`$, all three displayed logarithms vanish. At $`k=0`$, the construction and Jensen factors both have logarithm $`16\log_2 3\approx25.3594`$, while the coherent factor has logarithm $`128/47\approx2.7234`$.

## Scientific sources and checks

- [Model and tasks](../../science/model.md): the complete later-requested family and coherent-width resource.
- [Partial-Bell construction](../../science/partial_bell.md): the exact usability probability, Jensen bound, unbiased estimator and concentration.
- [Coherent converse](../../science/coherent_memory.md): the finite exponential factor and the polynomial-query threshold.
- [Finite diagnostics](../README.md): independent matrix, likelihood and syndrome checks.

The plotting function `usability(n,k,w)` agrees with `compatibility_probability(n,k,w)` in `verification/verify_syndromes.py`. The two expressions condition respectively on unpaired target positions and paired target positions. They agree as exact rational numbers for all 257 plotted settings. The [supplementary overview](../../figures/README.md) retains an independent rendering of the same analytical factors.
