import cv2


def artifacts_test(img) -> dict:
    artifacts = cv2.Canny(img, 10, 40, apertureSize=3)
    return artifacts


def render_artifacts_test(**kwargs):
    fig = kwargs["fig"]
    spec = kwargs["spec"]
    artifacts = kwargs["artifacts"]
    ax = fig.add_subplot(spec[7])
    ax.imshow(artifacts)
