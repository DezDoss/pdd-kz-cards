#!/bin/sh
# Раздать dist/ по локальной сети, чтобы открыть на айфоне.
# Мак должен не спать и быть в той же Wi-Fi сети.
PORT=${1:-8793}
DIR="$(cd "$(dirname "$0")/dist" && pwd)"
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo localhost)
echo "Открой на айфоне:  http://$IP:$PORT/"
echo "Остановить: Ctrl+C"
echo
python3 - "$PORT" "$DIR" <<'PY'
import http.server, socketserver, sys, os, datetime
os.chdir(sys.argv[2])

class H(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *a):
        sys.stdout.write("%s  %s  %s\n" % (datetime.datetime.now().strftime("%H:%M:%S"),
                                           self.client_address[0], fmt % a))
        sys.stdout.flush()

    def handle_one_request(self):
        # Safari открывает соединения про запас и закрывает неиспользованные —
        # это не ошибка, поэтому обрыв просто гасим.
        try:
            super().handle_one_request()
        except (ConnectionResetError, BrokenPipeError, TimeoutError):
            self.close_connection = True

class S(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True
    def handle_error(self, request, client_address):
        exc = sys.exc_info()[1]
        if not isinstance(exc, (ConnectionResetError, BrokenPipeError, TimeoutError)):
            super().handle_error(request, client_address)

with S(("0.0.0.0", int(sys.argv[1])), H) as s:
    try:
        s.serve_forever()
    except KeyboardInterrupt:
        print("\nостановлено")
PY
