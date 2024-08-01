from typing import List, Iterable, Optional

from math import ceil

import dominate
from dominate.tags import *


def header(title: str, sub: str):
    return h2(title, br(), small(sub), style="text-align: center")


def authors_row(names: Iterable[str], emails: Iterable[str]):
    rows = div(cls="row")
    for name, email in zip(names, emails):
        rows.add(
            div(
                [
                    strong(name, style="text-align:center"),
                    br(),
                    a(email, href=f"mailto:{email}"),
                ],
                cls="col-md-4",
                style="text-align: center;",
            )
        )
    return rows


def text_row(texts: Iterable[str], is_strong: bool = False) -> html_tag:
    """Generate a table row (tr) containing texts."""
    row = tr()
    with row:
        for title in texts:
            if title is not None:
                td(strong(title) if is_strong else title)
            else:
                td()
    return row


def audio_row(
    audio_files: Iterable[str],
    audio_type: str = "audio/wav",
    control_width_px: int = 120,
) -> html_tag:
    row = tr()
    with row:
        for audio_file in audio_files:
            if audio_file is not None:
                td(
                    audio(
                        source(src=audio_file, type=audio_type),
                        controls="",
                        style=f"width: {control_width_px:d}px",
                        preload="none",
                    )
                )
            else:
                td()
    return row


def audio_table(
    audio_files: Iterable[str],
    audio_names: Iterable[str] = None,
    desc: str = None,
    cols: int = 4,
    audio_control_width_px: int = 150,
) -> html_tag:
    """Create a table of the following form:
    =======================
    [desc]
    -----------------------
    name  0 | name  1 | ...
    audio 0 | audio 1 | ...
    name  w | ...
    audio w | ...
    =======================
    """
    # Padding Nones to ensure multiples of width:
    n_rows = ceil(len(audio_files) / cols)
    n_elems = n_rows * cols
    audio_files += [None] * (n_elems - len(audio_files))
    if audio_names is not None:
        audio_names += [None] * (n_elems - len(audio_names))

    # Construct the table:
    _div = div(cls="table-responsive")

    _table = _div.add(table(_class="table"))

    if desc is not None:
        _thead = _table.add(thead())
        with _thead:
            _t = _thead.add(tr())
            _t.add(th(desc, colspan=f"{cols}", style="text-align: left;"))

    _tbody = _table.add(tbody())
    with _tbody:
        for rid in range(n_rows):
            a = rid * cols
            b = rid * cols + cols
            if audio_names is not None:
                text_row(audio_names[a:b])
            audio_row(audio_files[a:b], control_width_px=audio_control_width_px)
        # tr(td() for _ in range(width))
    return _table


def audio_grid(audio_files: Iterable[str], control_width_px: int = 150) -> html_tag:
    # Construct the container:
    _div = div(cls="d-flex flex-row mb-3 flex-wrap justify-content-around")
    with _div:
        for audio_file in audio_files:
            with div(cls=f"p-2"):
                audio(
                    source(src=audio_file, type="audio/wav"),
                    controls="",
                    style=f"width: {control_width_px:d}px",
                    preload="none",
                )
    return _div


def dense_audio_table(
    audio_ids: Iterable[str],
    system_names: Iterable[str],
    system_roots: Iterable[str],
    audio_files: Iterable[str],
    control_width_px: int = 110,
    texts: Optional[Iterable[str]] = None,
):
    with div(cls="table-responsive").add(table(cls="table table-striped")):
        with thead():
            with tr():
                th("#", scope="col")
                for spk in audio_ids:
                    th(spk, scope="col")
        with tbody():
            if texts is not None:
                with tr():
                    th(
                        "Transcript",
                        scope="row",
                        style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for text in texts:
                        if text is not None:
                            td(p(text))
                        else:
                            td()

            for sys_name, sys_root in zip(system_names, system_roots):
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for comp_file in audio_files:
                        if comp_file is not None:
                            td(
                                audio(
                                    source(src=sys_root + comp_file, type="audio/wav"),
                                    controls="",
                                    style=f"width: {control_width_px:d}px",
                                    preload="none",
                                )
                            )
                        else:
                            td()
