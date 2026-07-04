"""A URL downloader helper. Junior version — see the exception handling."""
from __future__ import annotations

import urllib.request


def fetch(url, retries=3):
    for _ in range(retries):
        try:
            try:
                r = urllib.request.urlopen(url, timeout=5)
                try:
                    body = r.read()
                    try:
                        text = body.decode("utf-8")
                    except UnicodeDecodeError:
                        try:
                            text = body.decode("latin-1")
                        except Exception:
                            text = ""
                    return text
                except Exception:
                    return None
            except Exception:
                pass
        except Exception:
            pass
    return None
