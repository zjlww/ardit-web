from dominate.tags import *


systems = [
    ("Prompt", "prompt"),
    ("ARDiT (DMD, B=4)", "ardit_dmd_b4"),
    ("ARDiT (DMD, B=1)", "ardit_dmd_b1"),
    ("StyleTTS 2", "styletts2"),
    ("ARDiT (B=1)", "ardit_b1"),
    ("ARDiT (B=4)", "ardit_b4"),
    ("VoiceCraft (16kHz)", "voicecraft"),
    ("HierSpeech++ (16kHz)", "hierspeechpp"),
    ("UniCATS", "unicats"),
    ("Ground Truth", "ground_truth"),
    ("Autoencoder", "reconstruct"),
]


samples = [
    ('237', "237_126133_000029_000000", '"Boys," whispered their mother, warningly, "she can\'t answer you; just look at her face."'),
    ('1089', "1089_134686_000002_000001", 'After early nightfall the yellow lamps would light up, here and there, the squalid quarter of the brothels.'),
    ('1188', "1188_133604_000024_000000", 'But in this vignette, copied from Turner, you have the two principles brought out perfectly.'),
    ('1320', "1320_122612_000020_000001", 'A circle of a few hundred feet in circumference was drawn, and each of the party took a segment for his portion.'),
    ('1995', "1995_1837_000021_000002", 'The Sun, the Swamp? Then finding all well, she closed her eyes and slept.'),
    ('2300', "2300_131720_000020_000008", 'Hence the Edison electrolytic meter is no longer used, despite its excellent qualities.'),
    ('2830', "2830_3979_000018_000000", "The Reformer had lectured on this Epistle of saint Paul's in fifteen nineteen and again in fifteen twenty three."),
    ('3570', "3570_5695_000004_000011", 'The last items of this category of consumption are not given up except under stress of the direst necessity.'),
    ('4077', "4077_13754_000017_000001", 'This statement assumes, as granted, a distinction between bigamy and the "Mormon" institution of plural marriage.'),
    ('4446', "4446_2275_000030_000000", '"Yes, I was happy, wasn\'t I?" She pressed his hand gently in gratitude. "Weren\'t you happy then, at all?"'),
    ('4970', "4970_29093_000049_000001", 'He knew his uncle would be glad to hear that he had at last turned his thoughts to a practical matter.'),
    ('5105', "5105_28241_000021_000000", '"Is it not impossible," he murmured aloud, "that any city should disappear so completely?'),
    ('5683', "5683_32866_000028_000000", "'It is very happy, for her at least, they are not,' said Rachel, and a long silence ensued."),
    ('6829', "6829_68769_000091_000001", 'Give me a check for a hundred and fifty, and I\'ll turn over to you the forged check and quash further proceedings."'),
    ('7021', "7021_85628_000005_000000", 'The first person he met was a farm labourer walking alongside a load of peat and smacking at his horse.'),
    ('7176', "7176_88083_000010_000002", 'For all its appalling speed, the sound of his flight was nothing more than a strong pulsating hiss.'),
    ('7729', "7729_102255_000016_000002", 'The firm defensive attitude of the people of Lawrence had produced its effect.'),
    ('8230', "8230_279154_000018_000000", 'Some points may be taken as fixed, and such as any theory of memory must arrive at.'),
    ('8463', "8463_294828_000014_000000", 'Even so, I had just returned from an arduous journey, exhausted and badly needing a rest.'),
    ('8555', "8555_284449_000057_000000", 'This was done, the once royal family departing from the palace with shamed and downcast looks.'),
]


def get_table(
    root: str = "/samples/prompt",
    control_width_px = 240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(table(cls="table table-sm"))
    with _div:
        with thead():
            with tr():
                th("#", scope="col")
                for spk, _, _ in samples:
                    th(spk, scope="col")
        with tbody():
            with tr():
                th("Text", scope="row", style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;")
                for _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id in systems:
                with tr():
                    th(sys_name, scope="row", style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;")
                    for _, key, _ in samples:
                        td(
                            audio(
                                source(src=f"{root}/{sys_id}/{key}.wav", type="audio/wav"),
                                controls="",
                                style=f"width: {control_width_px:d}px",
                                preload="none"
                            )
                        )
    return _div