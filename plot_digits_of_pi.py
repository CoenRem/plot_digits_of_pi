#!/usr/bin/env python3
"""
Plot the distribution of the first X digits of pi.
"""

import matplotlib.pyplot as plt
from collections import Counter
from mpmath import mp


def get_pi_digits(num_digits: int) -> str:
    """
    Compute the first num_digits of pi (after the decimal point).

    Args:
        num_digits: Number of digits to compute

    Returns:
        String of pi digits (without "3.")
    """
    # Set precision high enough to get the required digits
    # We need extra precision to avoid rounding errors
    mp.dps = num_digits + 10
    pi_str = mp.nstr(mp.pi, num_digits + 1, strip_zeros=False)
    # Remove "3." and return the requested number of digits
    return pi_str.replace("3.", "")[:num_digits]


def plot_pi_distribution(num_digits: int) -> None:
    """
    Plot the distribution of the first num_digits of pi.

    Args:
        num_digits: Number of digits to analyze
    """
    print(f"Computing {num_digits} digits of pi...")
    digits = get_pi_digits(num_digits)
    digit_counts = Counter(digits)
    
    # Prepare data for plotting
    labels = [str(i) for i in range(10)]
    counts = [digit_counts.get(str(i), 0) for i in range(10)]
    expected = num_digits / 10  # Expected count if uniformly distributed
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.bar(labels, counts, color='steelblue', edgecolor='black', alpha=0.8)
    ax.axhline(y=expected, color='red', linestyle='--', linewidth=2, label=f'Expected (uniform): {expected:.1f}')
    
    # Add count labels on top of bars
    for bar, count in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                str(count), ha='center', va='bottom', fontsize=10)
    
    ax.set_xlabel('Digit', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title(f'Distribution of the First {num_digits} Digits of Pi', fontsize=14)
    ax.legend()
    ax.set_ylim(0, max(counts) * 1.15)
    
    plt.tight_layout()
    plt.savefig('pi_distribution.png', dpi=150)
    plt.close()
    
    # Print summary statistics
    print(f"\nDistribution of first {num_digits} digits of pi:")
    print("-" * 35)
    for digit in range(10):
        count = digit_counts.get(str(digit), 0)
        percentage = (count / num_digits) * 100
        print(f"  {digit}: {count:4d} ({percentage:5.2f}%)")
    print("-" * 35)
    print(f"  Expected per digit: {expected:.1f} ({10:.2f}%)")


if __name__ == "__main__":
    # You can change this value to analyze different numbers of digits
    NUM_DIGITS = 500
    plot_pi_distribution(NUM_DIGITS)
    print(f"\nPlot saved to pi_distribution.png")
