#!/usr/bin/env python3
"""serve.py — Local development server for bisulfid.com.

Serves the site/ directory on localhost using Python's built-in http.server.
Run build.py first to generate site/ output before serving.

No external dependencies. No browser auto-open.
Default port: 8000.
"""

import http.server
import os
import sys


SITE_DIR = "site"
DEFAULT_PORT = 8000


def main():
    if not os.path.isdir(SITE_DIR):
        print(f"ERROR: '{SITE_DIR}' directory not found.")
        print("  Run: python scripts/build.py")
        return 1

    os.chdir(SITE_DIR)

    port = DEFAULT_PORT
    handler = http.server.SimpleHTTPRequestHandler

    print(f"Serving '{SITE_DIR}/' at http://localhost:{port}/")
    print("  Press Ctrl+C to stop.")

    with http.server.HTTPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
