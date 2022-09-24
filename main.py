import cv2
from artifacts_test import artifacts_test, render_artifacts_test
from line_test import line_test, render_line_test
from noise_test import noise_test, render_noise_test
from matplotlib import pyplot as plt
from matplotlib import gridspec


def main():
    path = "research/images/drawn_3.jpg"
    grayscale_img = cv2.imread(path, 0)
    img = cv2.imread(path)
    (
        noise_ratio,
        noise_map_count,
        samples,
        max_sample_rate,
        min_sample_rate,
    ) = noise_test(grayscale_img)
    hough, horizontal_lines, vertical_lines = line_test(img)
    artifacts = artifacts_test(grayscale_img)

    render(
        img=img,
        noise_ratio=noise_ratio,
        horizontal_lines=horizontal_lines,
        vertical_lines=vertical_lines,
        hough=hough,
        artifacts=artifacts,
    )


def render(**kwargs):
    img = kwargs["img"]
    noise_ratio = kwargs["noise_ratio"]
    hough = kwargs["hough"]
    artifacts = kwargs["artifacts"]

    fig = plt.figure(figsize=(12, 12))
    spec = gridspec.GridSpec(ncols=2, nrows=4)

    plt.subplot(311)
    plt.imshow(img)
    render_noise_test(plt=plt, fig=fig, spec=spec, noise_ratio=noise_ratio)

    render_line_test(fig=fig, spec=spec, hough=hough)

    render_artifacts_test(fig=fig, spec=spec, artifacts=artifacts)

    plt.show()


if __name__ == "__main__":
    main()
