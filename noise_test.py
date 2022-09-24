import heapq
import numpy as np
import matplotlib
from collections import Counter

matplotlib.use("webAgg")


def nMax(lst: "list[float]", n: int) -> "list[float]":
    return heapq.nlargest(n, lst)


def nMin(lst: "list[float]", n: int) -> "list[float]":
    return heapq.nsmallest(n, lst)


def noise_test(img) -> dict:
    # anything more than 150k is high
    SAMPLES_NMAX = 10000
    width, height = img.shape
    gaussian = np.random.normal(0, 0, (width, height))

    noisy_img = img + gaussian
    noise_ratio = noisy_img.ravel()
    unique_noise_ratio = np.unique(noise_ratio)

    max_sample_rate = max(unique_noise_ratio)
    min_sample_rate = min(unique_noise_ratio)
    threshold_y = (max_sample_rate - min_sample_rate) / 3

    noise_map = [p for p in noise_ratio if p >= threshold_y]
    noise_map_count = len(noise_map)

    samples = dict(Counter(nMax(noise_map, SAMPLES_NMAX)))

    return noise_ratio, noise_map_count, samples, max_sample_rate, min_sample_rate


def render_noise_test(**kwargs):
    plt = kwargs["plt"]
    fig = kwargs["fig"]
    spec = kwargs["spec"]
    noise_ratio = kwargs["noise_ratio"]

    plt.subplot(312)
    plt.title("Noise Map Distribution Histogram")
    plt.hist(noise_ratio, 256, [0, 256])
    # plt.figtext(
    #     ax0.get_position().xmin + 0.075,
    #     0,
    #     "one text and next text",
    #     ha="center",
    #     fontsize=18,
    #     bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5},
    # )
