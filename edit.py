from dominate.tags import *
from dominate.util import raw
from templates import audio_table


system_names = ["Original", "ARDiT (DMD, B=1)", "VoiceBox", "VoiceCraft"]
systems =      ["original", "ardit_dmd_b1",     "voicebox", "voicecraft"]

texts = [
    (
        """Will find himself completely at a loss on occasions of common and constant recurrence, speculative ability is one thing and practical ability is another.""",
        """occasions of common and constant recurrence""",
        """rare and unpredictable circumstances""",
    ),
    (
        """In zero weather, in mid-winter, when the earth is frozen to a great depth below the surface, when in driving over the unpaved country roads, they give forth a hard metallic ring.""",
        """the earth is frozen to a great depth below the surface""",
        """jack frost has cast his icy spell upon the land""",
    ),
    (
        """And especially as I am not very much up in latin myself, he said, the suit was on an insurance policy that he was defending on the ground of misinterpretations.""",
        """an insurance policy""",
        """a classified treasure map""",
    ),
    (
        """Yet these petty operations incessantly continued in time surmount the greatest difficulties, mountains are elevated and oceans bounded by the slender force of human beings.""",
        """mountains are elevated and oceans bounded""",
        """vast challenges emerge and unexplored frontiers beckon""",
    ),
    (
        """And the carlsruhe professor had to devise an ingenious apparatus which enabled him to bring the preparation at the required temperature on to the very plate of the microscope.""",
        """carlsruhe""",
        """inventive""",
    ),
    (
        """This was george steers the son of a british naval captain and ship modeler who had become an american naval officer and was the first man to take charge of the washington navy yard.""",
        """the first man to take charge of the washington navy yard""",
        """entrusted with the prestigious role of overseeing the operations at the renowned naval headquarters""",
    ),
]


def prettify(a: str, b: str, c:str) -> str:
    return "<strong>Text: </strong>" + a.replace(b, f"""<span style="text-decoration-line: underline; text-decoration-style: wavy;">{b}</span> <span style="text-decoration-line: underline;">{c}</span>""")


pretty_texts = [prettify(a, b, c) for a, b, c in texts]
idxs = [3, 0, 1, 2, 4, 5]


def get_table(audio_root="/samples/edit"):
    for text, idx in zip(pretty_texts, idxs):
        p(raw(text), cls="lead")
        audio_table(
            audio_files=[f"{audio_root}/{system}/{idx}.wav" for system in systems],
            audio_names=system_names, cols=4, audio_control_width_px=250,
        )
