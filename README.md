# Plot Digits of Pi

Visualize the distribution of digits in pi to verify its randomness properties.

![Pi Distribution](example.png)

## Features

- Compute any number of digits of pi using arbitrary-precision arithmetic
- Generate bar charts showing digit frequency distribution
- Compare actual distribution against expected uniform distribution

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python plot_digits_of_pi.py
```

The script will prompt you for the number of digits to analyze, then display the distribution plot.

## Example Output

```
How many digits of pi to analyze? 10000
Computing 10000 digits of pi...

Distribution of first 10000 digits of pi:
-----------------------------------
  0:  968 ( 9.68%)
  1: 1026 (10.26%)
  2: 1021 (10.21%)
  3:  974 ( 9.74%)
  4: 1012 (10.12%)
  5: 1046 (10.46%)
  6: 1021 (10.21%)
  7:  970 ( 9.70%)
  8:  947 ( 9.47%)
  9: 1015 (10.15%)
-----------------------------------
  Expected per digit: 1000.0 (10.00%)
```

## Dependencies

- `matplotlib` - Plotting
- `mpmath` - Arbitrary-precision arithmetic
