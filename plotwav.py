import matplotlib.pyplot as plt
import scipy.io.wavfile
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert historical stock prices to audio file')
    parser.add_argument(
        'filename', type=str,
        help='file name of a wav'
    )
    args = parser.parse_args()
    filename = args.filename

    sample_rate, signal = scipy.io.wavfile.read(filename)
    if len(signal.shape) > 1:
        signal = signal[:, 0]
    fig, axs = plt.subplots(1)
    plt.title(filename)
    axs.plot(signal, c='k')
    plt.show()
