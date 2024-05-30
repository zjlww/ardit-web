from dominate.tags import *
from dominate.util import raw
from pathlib import Path


systems = [
    ("Prompt", "prompt"),
    ("ARDiT (DMD, B=1)", "ardit_dmd_b1"),
    ("NaturalSpeech 3", "ns3"),
    ("NaturalSpeech 2", "ns2"),
    ("MegaTTS 2", "megatts2"),
    ("UniAudio", "uniaudio"),
    ("CLaM-TTS", "clamtts"),
    ("VoiceBox", "voicebox"),
    ("VALL-E", "valle"),
    ("Ground Truth", "gt"),
]


samples = [
    ("1", """It is this that is of interest to theory of knowledge."""),
    ("2", """For, like as not, they must have thought him a prince when they saw his fine cap."""),
    ("3", """What you had best do, my child, is to keep it and pray to it that since it was a witness to your undoing, it will deign to vindicate your cause by its righteous judgment."""),
    ("4", """The strong position held by the Edison system under the strenuous competition that was already springing up was enormously improved by the introduction of the three wire system and it gave an immediate impetus to incandescent lighting."""),
    ("5", """They moved thereafter cautiously about the hut groping before and about them to find something to show that Warrenton had fulfilled his mission."""),
    ("6", """And lay me down in thy cold bed and leave my shining lot."""),
    ("7", """Number ten, fresh nelly is waiting on you, good night husband."""),
    ("8", """Yea, his honourable worship is within, but he hath a godly minister or two with him, and likewise a leech."""),
    ("9", """Instead of shoes, the old man wore boots with turnover tops, and his blue coat had wide cuffs of gold braid."""),
    ("10", """The army found the people in poverty and left them in comparative wealth."""),
    ("11", """Thus did this humane and right minded father comfort his unhappy daughter, and her mother embracing her again, did all she could to soothe her feelings."""),
    ("12", """He was in deep converse with the clerk and entered the hall holding him by the arm."""),
    ("13", """Indeed, there were only one or two strangers who could be admitted among the sisters without producing the same result."""),
    ("14", """For if he's anywhere on the farm, we can send for him in a minute."""),
    ("15", """Their piety would be like their names, like their faces, like their clothes, and it was idle for him to tell himself that their humble and contrite hearts it might be paid a far-richer tribute of devotion than his had ever been. A gift tenfold more acceptable than his elaborate adoration."""),
    ("16", """The air and the earth are curiously mated and intermingled as if the one were the breath of the other."""),
    ("17", """I had always known him to be restless in his manner, but on this particular occasion he was in such a state of uncontrollable agitation that it was clear something very unusual had occurred."""),
    ("18", """His death in this conjuncture was a public misfortune."""),
    ("19", """It is this that is of interest to theory of knowledge."""),
    ("20", """For a few miles, she followed the line hitherto presumably occupied by the coast of Algeria, but no land appeared to the south."""),
]


def get_table(
    root: str = "/samples/demo_compare",
    control_width_px = 240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(table(cls="table table-sm"))
    with _div:
        with thead():
            with tr():
                th("#", scope="col")
                for idx, _ in samples:
                    th(idx, scope="col")
        with tbody():
            with tr():
                th("Text", scope="row", style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;")
                for _, text in samples:
                    td(p(text))

            for sys_name, sys_id in systems:
                with tr():
                    th(sys_name, scope="row", style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;")
                    for idx, _ in samples:
                        wav_path = Path(f"{root[1:]}/{sys_id}/{idx}.wav")
                        if wav_path.exists():
                            td(
                                audio(
                                    source(src=f"{root}/{sys_id}/{idx}.wav", type="audio/wav"),
                                    controls="",
                                    style=f"width: {control_width_px:d}px",
                                    preload="none"
                                )
                            )
                        else:
                            td("—",cls="center-text")
    return _div
