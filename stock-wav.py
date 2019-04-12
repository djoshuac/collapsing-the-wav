import pandas as pd
from scipy.io import wavfile
import numpy as np
import argparse


def stock_to_wav(filename):
    prices = pd.read_csv(f"{filename}.csv").Close.values
    prices = np.diff(prices)
    scale = (2**15) * 0.8 / max(map(abs, [prices.max(), prices.min()]))
    prices = (prices * scale)
    mx, mn = prices.max(), prices.min()
    prices = prices.astype(np.int16)
    assert abs(mx - prices.max()) < 2
    assert abs(mn - prices.min()) < 2
    wavfile.write(f"{filename}.wav", 2_000, prices)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert historical stock prices to audio file')
    parser.add_argument(
        'filename', type=str,
        help='stock in {stock}.csv'
    )
    args = parser.parse_args()
    stock_to_wav(args.filename)
