from dominate.tags import *
from dominate.util import raw
from templates import audio_table

audio_root = "/samples/rate_control"


samples = [
    ("Very Slow", f"{audio_root}/9s.wav"),
    ("Slow", f"{audio_root}/8s.wav"),
    ("Normal", f"{audio_root}/7s.wav"),
    ("Normal", f"{audio_root}/6s.wav"),
    ("Fast", f"{audio_root}/5s.wav"),
    ("Very Fast", f"{audio_root}/4s.wav"),
]


def get_table():
    audio_table(["/samples/rate_control/prompt.wav"], audio_names=["Prompt"], cols=1, audio_control_width_px=250)
    p(raw("<strong>Text: </strong>The examination and testimony of the experts, enabled the commission to conclude, that five shots may have been fired."), cls="lead")
    audio_table([f for _, f in samples], audio_names=[n for n, _ in samples], cols=3, audio_control_width_px=250)
