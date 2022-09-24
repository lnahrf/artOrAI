import numpy as np
import cv2


def cord_to_dict(x1: float, y1: float, x2: float, y2: float) -> dict:
    return {"start": {"x": x1, "y": y1}, "end": {"x": x2, "y": y2}}


def line_test(img) -> dict:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 1, 300)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 25, minLineLength=80, maxLineGap=50)

    hough = np.zeros(img.shape, np.uint8)

    horizontal_line_threshold = 1
    vertical_line_threshold = 1

    horizontal_lines = []
    vertical_lines = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        th_threshold = y2 + horizontal_line_threshold
        bh_threshold = y2 - horizontal_line_threshold

        tv_threshold = x2 + vertical_line_threshold
        bv_threshold = x2 - vertical_line_threshold

        if bh_threshold <= y1 <= th_threshold:
            cv2.line(hough, (x1, y1), (x2, y2), (255, 255, 255), 2)
            horizontal_lines.append(cord_to_dict(x1, y1, x2, y2))
        if bv_threshold <= x1 <= tv_threshold:
            cv2.line(hough, (x1, y1), (x2, y2), (255, 0, 0), 2)
            vertical_lines.append(cord_to_dict(x1, y1, x2, y2))

    return hough, horizontal_lines, vertical_lines


def render_line_test(**kwargs):
    fig = kwargs["fig"]
    spec = kwargs["spec"]
    hough = kwargs["hough"]
    ax = fig.add_subplot(spec[6])
    ax.imshow(hough)
