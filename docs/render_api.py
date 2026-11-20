"""Render the Sphinx API directives and docstrings as book chapter content."""

import json
import re
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from sphinxcontrib.serializinghtml import JSONHTMLBuilder


class QuartoAPIBuilder(JSONHTMLBuilder):
    name = "quarto-api"

    def get_target_uri(self, docname, typ=None):
        return f"{docname}.html"


def setup(app):
    app.add_builder(QuartoAPIBuilder)
    return {"parallel_read_safe": True}


def main():
    docs = Path(__file__).resolve().parent
    with TemporaryDirectory() as build_dir:
        subprocess.run(
            [sys.executable, "-m", "sphinx", "-q", "-b", "quarto-api", str(docs), build_dir],
            check=True,
        )
        for source in sorted((docs / "api").glob("*.rst")):
            page = Path(build_dir) / "api" / f"{source.stem}.fjson"
            body = json.loads(page.read_text(encoding="utf-8"))["body"]
            # Move section IDs onto headings so Quarto can build its own table of contents.
            body = re.sub(
                r'<section id="([^"]+)">(\s*(?:<span id="[^"]+"></span>\s*)*)<h([1-6])>',
                r'\2<h\3 id="\1">',
                body,
            ).replace("</section>", "")
            # Pandoc discards attributes on definition-list terms. Keep their anchors inline.
            body = re.sub(r'(<dt\b[^>]*\bid="([^"]+)"[^>]*>)', r'\1<span id="\2"></span>', body)
            markdown = subprocess.run(
                ["quarto", "pandoc", "--from=html", "--to=markdown", "--wrap=none"],
                input=body,
                encoding="utf-8",
                stdout=subprocess.PIPE,
                check=True,
            ).stdout
            source.with_suffix(".qmd").write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
