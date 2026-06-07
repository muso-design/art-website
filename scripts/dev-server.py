#!/usr/bin/env python3
"""
dev-server.py — Local dev server for TESTING.

It serves the site exactly like `python -m http.server`, but ALSO handles the
newsletter signup: a POST to /subscribe appends the email address (with a
timestamp) to subscribers.txt in the project folder.

Run it via serve.bat, then open http://localhost:8080 and try the form on the
Contact page. Check subscribers.txt to see captured addresses.

LOCAL ONLY — GitHub Pages cannot run Python. When you move to your own domain,
point `newsletter_action` (settings.csv) at your real endpoint. The front-end
already POSTs a urlencoded `email` field that any server/provider can read, so
no front-end changes are needed.
"""
import http.server
import socketserver
import os
import re
import json
import datetime
import urllib.parse

PORT = 8080
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SUBSCRIBERS = os.path.join(ROOT, 'subscribers.txt')
EMAIL_RE = re.compile(r'[^@\s]+@[^@\s]+\.[^@\s]+')


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def _json(self, code, obj):
        body = json.dumps(obj).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _find_email(self, raw):
        for vals in urllib.parse.parse_qs(raw).values():
            for val in vals:
                if EMAIL_RE.fullmatch(val.strip()):
                    return val.strip()
        try:
            for val in json.loads(raw).values():
                if isinstance(val, str) and EMAIL_RE.fullmatch(val.strip()):
                    return val.strip()
        except Exception:
            pass
        return ''

    def do_POST(self):
        if self.path.split('?')[0].rstrip('/') == '/subscribe':
            length = int(self.headers.get('Content-Length', 0) or 0)
            raw = self.rfile.read(length).decode('utf-8', 'replace')
            email = self._find_email(raw)
            if not email:
                return self._json(400, {'ok': False, 'error': 'no valid email'})
            ts = datetime.datetime.now().isoformat(timespec='seconds')
            with open(SUBSCRIBERS, 'a', encoding='utf-8') as f:
                f.write(f'{ts}\t{email}\n')
            print(f'  + subscribed: {email}')
            return self._json(200, {'ok': True})
        self._json(404, {'ok': False, 'error': 'not found'})

    def log_message(self, fmt, *args):
        pass  # keep the console quiet


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == '__main__':
    os.chdir(ROOT)
    with Server(('', PORT), Handler) as httpd:
        print(f'Dev server (with newsletter) running at http://localhost:{PORT}')
        print(f'New subscribers are saved to: {SUBSCRIBERS}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nStopped.')
