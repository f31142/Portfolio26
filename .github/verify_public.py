"""Check the main portfolio pages and their local files before deployment."""

import json
import os
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
REQUIRED_LINKS = {
    "": {"about/", "projects/", "images/jeon-portrait.jpg"},
    "about/": set(),
    "projects/": {
        "projects/mylab/",
        "projects/adviser/",
        "projects/who-study-guideline/",
    },
    "projects/mylab/": {"media/mylab-demo.mp4"},
    "projects/adviser/": {
        "images/adviser/login.png",
        "images/adviser/service-selection.png",
        "images/adviser/service-workflow.png",
    },
    "projects/who-study-guideline/": {
        "images/who-study-guideline/overview.png",
        "images/who-study-guideline/weekly-gallery.png",
        "images/who-study-guideline/extra-resources.png",
    },
}
URL_ATTRIBUTES = {
    "a": ("href",),
    "img": ("src",),
    "link": ("href",),
    "script": ("src",),
    "source": ("src",),
    "video": ("src", "poster"),
}


class PageLinks(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = set()
        self.anchors = set()
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.anchors.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.anchors.add(attrs["name"])
        for name in URL_ATTRIBUTES.get(tag, ()):
            if attrs.get(name):
                self.links.add(attrs[name])


def verify(base_url):
    base = urlsplit(base_url)
    base_path = unquote(base.path)
    errors = []
    pages = {}

    def parse_page(file):
        if file not in pages:
            pages[file] = PageLinks(file.read_text(encoding="utf-8"))
        return pages[file]

    for route, required_links in REQUIRED_LINKS.items():
        page = PUBLIC / route / "index.html"
        if not page.is_file():
            errors.append(f"{route or '/'}: missing page {page.relative_to(ROOT)}")
            continue

        page_url = urljoin(base_url, route)
        found = set()
        for link in sorted(parse_page(page).links):
            target = urlsplit(urljoin(page_url, link))
            if (target.scheme, target.netloc) != (base.scheme, base.netloc):
                continue

            target_path = unquote(target.path)
            if not target_path.startswith(base_path):
                errors.append(f"{route or '/'}: {link} is outside {base_path}")
                continue

            relative = target_path.removeprefix(base_path)
            file = PUBLIC / relative
            if target_path.endswith("/") or file.is_dir():
                file /= "index.html"
            if not file.resolve().is_relative_to(PUBLIC.resolve()) or not file.is_file():
                errors.append(f"{route or '/'}: missing local target {link}")
                continue
            found.add(relative)
            fragment = unquote(target.fragment).split(":~:", 1)[0]
            if file.suffix == ".html" and fragment and fragment.lower() != "top":
                if fragment not in parse_page(file).anchors:
                    errors.append(f"{route or '/'}: missing anchor {link}")

        for link in sorted(required_links - found):
            errors.append(f"{route or '/'}: missing required reference {link}")

    return errors


def main():
    config = json.loads((ROOT / ".github-pages.json").read_text(encoding="utf-8"))
    base_url = (os.environ.get("SITE_BASE_URL") or config["baseURL"]).rstrip("/") + "/"
    errors = verify(base_url)
    if errors:
        print("Portfolio verification failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Verified {len(REQUIRED_LINKS)} portfolio pages, local links, files, and anchors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
