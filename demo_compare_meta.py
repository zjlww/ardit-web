from dominate.tags import *
from dominate.util import raw
from pathlib import Path


systems = [
    ("Prompt", "prompt"),
    ("ARDiT (DMD, B=1)", "ardit_dmd_b1"),
    ("VoiceBox", "voicebox"),
    ("SpeechFlow", "speechflow"),
]


samples = [
    (
        "5639-40744-0020",
        """Thus did this humane and right minded father comfort his unhappy daughter, and her mother embracing her again, did all she could to soothe her feelings.""",
    ),
    (
        "61-70970-0024",
        """They moved thereafter cautiously about the hut groping before and about them to find something to show that warrenton had fulfilled his mission.""",
    ),
    (
        "908-157963-0027",
        """And lay me down in thy cold bed and leave my shining lot.""",
    ),
    (
        "672-122797-0040",
        """And the whole night the tree stood still and in deep thought.""",
    ),
    (
        "1284-1180-0002",
        """Instead of shoes, the old man wore boots with turnover tops, and his blue coat had wide cuffs of gold braid.""",
    ),
    (
        "4077-13754-0000",
        """The army found the people in poverty, and left them in comparative wealth.""",
    ),
    (
        "1221-135767-0014",
        """Yea his honourable worship is within, but he hath a godly minister or two with him, and likewise a leech.""",
    ),
    (
        "61-70970-0007",
        """He was in deep converse with the clerk and entered the hall holding him by the arm.""",
    ),
    (
        "1089-134686-0004",
        """Number ten fresh nelly is waiting on you, good night husband.""",
    ),
    (
        "6432-63722-0047",
        """Rather a hypothetical question colonel, but I should say it might be a fifty fifty proposition.""",
    ),
    (
        "5_1",
        """How much wood could a woodchuck chuck if a woodchuck could chuck wood.""",
    ),
    (
        "18_1",
        """When feline magicians enchant the city and crafty canine illusionists work to restore balance, don't miss the uproarious clash in 'magic and mischief: the paws of mystery.'""",
    ),
    ("8_1", """Peter piper picked a peck of pickled peppers."""),
    (
        "29_0",
        """Voicebox is the swiss army knife of text to speech acing multiple languages, changing voice styles, and dishing out custom samples.""",
    ),
    (
        "21_0",
        """In a land where cat pirates sail the high seas and dog buccaneers chase their tails, embark on a swashbuckling comedy adventure in 'furry buccaneers: the quest for the golden bone.'""",
    ),
]


def get_table(
    web_root: str = "/ardit-web",
    root: str = "samples/demo_compare_meta",
    control_width_px=240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(
        table(cls="table table-sm")
    )
    with _div:
        with thead():
            with tr():
                th("#", scope="col")
                for idx, _ in samples:
                    th(idx, scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, text in samples:
                    td(p(text))

            for sys_name, sys_id in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for idx, _ in samples:
                        wav_path = Path(f"{root}/{sys_id}/{idx}.wav")
                        if wav_path.exists():
                            td(
                                audio(
                                    source(
                                        src=f"{web_root}/{root}/{sys_id}/{idx}.wav",
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
