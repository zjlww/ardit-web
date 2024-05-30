from html import escape as html_escape
from dominate.tags import *
from dominate.util import raw


systems = [
    ("Ground Truth", "ground_truth"),
    ("ARDiT (DMD, B=4)", "ardit_dmd_b4"),
    ("ARDiT (DMD, B=1)", "ardit_dmd_b1"),
    ("ARDiT (B=1)", "ardit_b1"),
    ("ARDiT (B=4)", "ardit_b4"),
    ("UniCATS", "unicats"),
    ("VoiceCraft (16kHz)", "voicecraft"),
]


samples = [
    ("237", "237_134500_000008_000001", 'In a few moments he heard the cherries dropping smartly into the pail, and he began to swing his scythe with that long, even stroke that few American boys ever learn.', 'the cherries dropping smartly into the pail'),
    ("260", "260_123288_000041_000003", 'The instruments, the tools, our guns, are clashing and clanking violently in their collisions with each other; the nails of my boots cling tenaciously to a plate of iron let into the timbers, and I cannot draw my foot away from the spot.', 'instruments, the tools, our guns, are clashing'),
    ("908", "908_157963_000004_000000", 'Does the Eagle know what is in the pit? Or wilt thou go ask the Mole: Can Wisdom be put in a silver rod? Or Love in a golden bowl?', 'the Mole: Can Wisdom be'),
    ("1089", "1089_134691_000049_000002", 'To live, to err, to fall, to triumph, to recreate life out of life!', 'to triumph, to recreate life'),
    ("1188", "1188_133604_000024_000001", 'You have the white of foaming water, of buildings and clouds, brought out brilliantly from a white ground; and though part of the subject is in deep shadow, the eye at once catches the one black point admitted in front.', 'subject is in deep shadow, the eye'),
    ("1320", "1320_122612_000043_000001", "Recovering his recollection on the instant, instead of sounding an alarm, which might prove fatal to himself, he remained stationary, an attentive observer of the other's motions.", 'instant, instead of sounding an alarm, which'),
    ("1580", "1580_141084_000029_000002", 'My friend did not appear to be depressed by his failure, but shrugged his shoulders in half humorous resignation.', 'depressed by his failure, but shrugged his shoulders in half humorous'),
    ("1995", "1995_1826_000016_000010", 'Miss Taylor was soon starving for human companionship, for the lighter touches of life and some of its warmth and laughter.', 'touches of life and some of its warmth'),
    ("2961", "2961_961_000022_000000", "When all of them, both those who show themselves in the sky, and those who retire from view, had come into being, the Creator addressed them thus:--'Gods, sons of gods, my works, if I will, are indissoluble.", 'and those who retire from view, had'),
    ("3570", "3570_5695_000007_000003", "In the modern community there is also a more frequent attendance at large gatherings of people to whom one's everyday life is unknown; in such places as churches, theaters, ballrooms, hotels, parks, shops, and the like.", 'there is also a more frequent attendance at large'),
    ("3575", "3575_170457_000012_000003", 'He spoke French perfectly, I have been told, when need was; but delighted usually in talking the broadest Yorkshire.', 'perfectly, I have been told, when need'),
    ("4970", "4970_29095_000056_000000", 'Ruth was glad to hear that Philip had made a push into the world, and she was sure that his talent and courage would make a way for him. She should pray for his success at any rate, and especially that the Indians, in Saint Louis, would not take his scalp.', 'glad to hear that Philip had made a push into'),
    ("4992", "4992_23283_000048_000000", 'He was going to leave the room--she followed him, and cried, "But, my Lord, how shall I see again the unhappy object of my treachery?', 'him, and cried, "But, my Lord, how shall I'),
    ("5683", "5683_32879_000008_000001", 'She was up and dressed, and this moment coming down, and would be very happy to see Miss Brandon, if she would step into the drawing-room.', 'dressed, and this moment coming down'),
    ("6829", "6829_68769_000009_000000", '"If the prosecution were withdrawn and the case settled with the victim of the forged check, then the young man would be allowed his freedom. But under the circumstances I doubt if such an arrangement could be made."', 'settled with the victim of the forged check'),
    ("6930", "6930_81414_000019_000003", 'Gradually I knew I was mastering him--then all was blank.', 'mastering him--then all was'),
    ("7176", "7176_92135_000006_000007", '"My dear Sir," I should reply (or Madam), "you have come to the right shop.', 'or Madam), "you have come to the right shop'),
    ("8455", "8455_210777_000003_000000", 'I remained there alone for many hours, but I must acknowledge that before I left the chambers I had gradually brought myself to look at the matter in another light.', 'hours, but I must acknowledge that before I left'),
    ("8463", "8463_294828_000014_000001", 'I wanted nothing more than to see my country again, my friends, my modest quarters by the Botanical Gardens, my dearly beloved collections!', 'by the Botanical Gardens, my dearly'),
    ("8555", "8555_292519_000004_000000", "Guided by you, how we might stroll towards death, Our only music one another's breath, Through gardens intimate with hollyhocks, Where silent poppies burn between the rocks, By pools where birches bend to confidants Above green waters scummed with lily-plants.", 'gardens intimate with hollyhocks, Where'),
]


def emphasize(s: str, t: str) -> str:
    b = html_escape(s).replace(html_escape(t), '<u><em><strong>' + html_escape(t) + '</strong></em></u>')
    return b

def get_table(
    root: str = "/samples/inpaint",
    control_width_px = 240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(table(cls="table table-striped table-sm"))
    with _div:
        with thead():
            with tr():
                th("#", scope="col")
                for spk, _, _, _ in samples:
                    th(spk, scope="col")
        with tbody():
            with tr():
                th("Text", scope="row", style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;")
                for _, _, text_s, text_t in samples:
                    td(raw(emphasize(text_s, text_t)))

            for sys_name, sys_id in systems:
                with tr():
                    th(sys_name, scope="row", style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;")
                    for _, key, _, _ in samples:
                        td(
                            audio(
                                source(src=f"{root}/{sys_id}/{key}.wav", type="audio/wav"),
                                controls="",
                                style=f"width: {control_width_px:d}px",
                                preload="none"
                            )
                        )
    return _div
