from dominate.tags import *
from dominate.util import raw
from pathlib import Path

systems = [
    ("Prompt", "prompt"),
    ("ARDiT (DMD, B=1)", "ardit_dmd_b1"),
    ("MegaTTS", "megatts"),
    ("CLaM-TTS", "clamtts"),
]

samples = [
    (
        "caine",
        "Michael Caine",
        "And sometimes, in both realms, it's not just about shining the brightest, but enduring the longest.",
    ),
    (
        "jessie",
        "Jessie Eisenberg",
        "So here we are, trying to catch up, and hoping this day turns around soon.",
    ),
    (
        "optimusprime",
        "Optimus Prime",
        "We must unite and harness our strengths, for the fate of our world hangs in the balance.",
    ),
    (
        "rachel",
        "Rachel McAdams",
        "But to those who knew her well, it was a symbol of her unwavering determination and spirit.",
    ),
    (
        "robert",
        "Robert Downey Jr.",
        "We have the responsibility to ensure power and technology are used for the greater good.",
    ),
    (
        "sherlock",
        "Benedict Cumberbatch",
        "However, if you choose to stay, know that the truth I unveil may forever alter the course of your journey.",
    ),
    (
        "zuck",
        "Mark Zuckerberg",
        "Our goal is to bridge communication gaps and preserve the richness of these unique languages.",
    ),
    (
        "dwarf",
        "Dwarf from Warcraft",
        "Good afternoon everyone. Today, we are super excited to introduce you all to Introduction to Deep Learning, the course of Carnegie Mellon University.",
    ),
    (
        "obama",
        "Barack Obama",
        "Good afternoon everyone. Today, we are super excited to introduce you all to Introduction to Deep Learning, the course of Carnegie Mellon University.",
    ),
    (
        "may",
        "Theresa May",
        "Good afternoon everyone. Today, we are super excited to introduce you all to Introduction to Deep Learning, the course of Carnegie Mellon University.",
    ),
]


def get_table(
    web_root: str = "/ardit-web",
    root: str = "samples/celeb",
    control_width_px=240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(
        table(cls="table table-sm")
    )
    with _div:
        with thead():
            with tr():
                th("#", scope="col")
                for _, name, _ in samples:
                    th(name, scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for nick, _, _ in samples:
                        wav_path = Path(f"{root}/{sys_id}/{nick}.wav")
                        if wav_path.exists():
                            td(
                                audio(
                                    source(
                                        src=f"{web_root}/{root}/{sys_id}/{nick}.wav",
                                        type="audio/wav",
                                    ),
                                    controls="",
                                    style=f"width: {control_width_px:d}px",
                                    preload="none",
                                )
                            )
                        else:
                            td("—", cls="center-text")
    return _div
