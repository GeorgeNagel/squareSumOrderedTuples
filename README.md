# Ordered tuples ranked by sum of squares

This repo contains a simple script for generating an ordered list of tuples where each subsequent tuple has a non-decreasing sum of squares.

## Motivation

In the n-dimensional clamped string, the resonant frequencies are a function of the mode shape identifiers, which are integer tuples like (m, n) where m and n >= 1. [[1]](#1)

When modeling the resonant response of a clamped n-dimensional clamped string as a finited sum of sines, it may be preferable to generate lower-frequency sines first, as those are more likely to contribute to distinct timbral frequencies of the resonance. In particular, if the falloff of the amplitude of resonant frequencies is a function of the sum of the squares of the mode identifiers, it is helpful to have a pre-computed list of mode identifier tuples, ordered by the sum of squares.

## Example

For the 3-dimensional extension of the clamped string resonant frequency equation,

```
f(m,n,p)=c * sqrt( (m / Lx)^2 + (n / Ly)^2 + (p / Lz)^2)
```

We would like to calculate the resonant frequencies `f(m,n,p)` in order where (m,n,p) equals:
```
(1, 1, 1) <- sum of squares = 3
(1, 1, 2) <- sum of squares = 6
(1, 2, 1) <- sum of squares = 6
(2, 1, 1) <- sum of squares = 6
(1, 2, 2) <- sum of squares = 9
(2, 1, 2) <- sum of squares = 9
(2, 2, 1) <- sum of squares = 9
(1, 1, 3) <- sum of squares = 11
(1, 3, 1) <- sum of squares = 11
(3, 1, 1) <- sum of squares = 11
(2, 2, 2) <- sum of squares = 12
...
```

## Usage
```
# Ask for help
python ordered_squares.py --help

# Generate the first 50 list of length-4 tuples, ordered by sum of squares
python ordered_squares.py -n 50 -l 4
```

# References

<a id="1">[1]</a>
https://www.acs.psu.edu/drussell/Demos/rect-membrane/rect-mem.html