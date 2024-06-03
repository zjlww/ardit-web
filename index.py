import inspect
import os 
from pathlib import Path
import dominate
from dominate.tags import *
from dominate.util import raw

from templates import header, authors_row


# Where to save the generated file.
root_path = Path(inspect.getfile(inspect.currentframe())).parent
doc = dominate.document(title=None)

with doc.head:
    meta(charset="utf-8")
    meta(http_equiv="X-UA-Compatible", content="IE=edge")
    meta(name="viewport", content="width=device-width, initial-scale=1")
    title("ARDiT TTS Demo")
    link(href="/statics/bootstrap-5.2.3-dist/css/bootstrap.min.css", rel="stylesheet")
    link(href="/statics/my.css", rel="stylesheet")

with doc:
    # Title and Metadata:
    with div(cls="container").add(div(cls="row")):
        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            header(title="Autoregressive Diffusion Transformer for Text-to-Speech Synthesis", sub="")
            br()
            from abstract import section_abstract
            section_abstract()
            p(
                "You can download all audio files on this page by cloning this annoymous ", a("github repository", href="https://github.com/ardit-tts/ardit-tts.github.io"),
                ".", 
                cls="lead"
            )

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from prompt import get_table
            h3("Prompted Generation")
            p(
                """
                In this task, we evaluate on test set B. We pick a prompt and a target utterance from the same speaker. The models generate target waveforms with prompt waveforms and the transcript of both sentences.
                All speakers are unseen for all systems during training.
                """,
                cls="lead"
            )
            get_table()
            p("* please scroll horizontally to explore additional columns in the table.", cls="lead")

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from inpaint import get_table
            h3("Speech Editing")
            p(
                """
                We evaluated the performance of text-based speech editing on the speech inpainting task.
                The models generate complete waveforms given complete texts and partially masked waveforms. The masked sections are highlighted within the text.
                All speakers were unseen by all systems during training. The following 20 test cases are from test set C (long).
                """,
                cls="lead"
            )
            get_table()
            p("* please scroll horizontally to explore additional columns in the table.", cls="lead")
        
        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from demo_compare import get_table
            h3("Prompted Generation (Comparing with Proprietary Systems I)")
            p(
                """
                In this section, we compare our system with proprietary systems including NaturalSpeech 2/3, MegaTTS 2, UniAudio, CLaM-TTS, VoiceBox, and VALL-E. The source codes and model weights for these models are not available.
                The following samples are obtained from their online demo pages. All waveforms are downsampled to 16kHz.
                Please note that ARDiT's performance is influenced by the fact that the prompt waveforms are in 16kHz, not 24kHz, and the prompt texts are not semantically coherent with the target texts.
                """,
                cls="lead"
            )
            p(
                "1~4 are obtained from ", a("NaturalSpeech 3", href="https://speechresearch.github.io/naturalspeech3/"), " and 5~20 are obtained from ", a("CLaM-TTS", href="https://clam-tts.github.io/"), "'s demo page.",
                cls="lead"
            )
            get_table()
            p("* please scroll horizontally to explore additional columns in the table.", cls="lead")

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from demo_compare_meta import get_table
            h3("Prompted Generation (Comparing with Proprietary Systems II)")
            p(
                """
                In this section, we compare our system with proprietary Flow Matching based TTS systems including VoiceBox and SpeechFlow. The source codes and model weights for these models are not available.
                The following samples are obtained from their online demo pages. All waveforms are downsampled to 16kHz.
                Please note that ARDiT's performance is influenced by the fact that the prompt waveforms are in 16kHz, not 24kHz, and the prompt texts are not semantically coherent with the target texts.
                """,
                cls="lead"
            )
            p(
                "Audio samples are obtained from ", a("voicebox.metademolab.com", href="https://voicebox.metademolab.com/"),
                cls="lead"
            )
            get_table()
            p("* please scroll horizontally to explore additional columns in the table.", cls="lead")

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from celeb import get_table
            h3("Prompted Generation (Celebrities and Game Characters)")
            p(
                """
                ARDiT trained only on LibriTTS is capable of imitating famous figures' voice.
                """,
                cls="lead"
            )
            p(
                "Prompts and baseline results are obtained from ", a("Mega-TTS", href="https://mega-tts.github.io/demo-page/"), " and ", a("CLaM-TTS", href="https://clam-tts.github.io/"), "'s demo pages.",
                cls="lead"
            )
            get_table()
            p("* please scroll horizontally to explore additional columns in the table.", cls="lead")

with doc.footer:
    script(src="/statics/jquery/jquery-3.7.1.slim.min.js")
    script(src="/statics/bootstrap-5.2.3-dist/bootstrap.min.js")

# Script for allowing only one audio to play at the same time:
doc.children.append(script(raw("""
    $(function(){
        $("audio").on("play", function() {
            $("audio").not(this).each(function(index, audio) {
                audio.pause();
                audio.currentTime = 0;
            });
        });
    });
    """)
))

with open(root_path / "index.html", "w") as index:
    index.write(doc.render())
