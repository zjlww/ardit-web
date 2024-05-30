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

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from inpaint import get_table
            h3("Speech Inpainting")
            p(
                """
                In this task, we evaluate on test set C. We mask fragments of the waveforms, and ask the models to generate the full waveforms. The masked sections are highlighted within the text.
                All speakers are unseen for all systems during training.
                """,
                cls="lead"
            )
            get_table()

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
