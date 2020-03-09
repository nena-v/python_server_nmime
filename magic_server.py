import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import sys

try:
    import magic
except ImportError:
    print("magic module must be installed for this SimpleHTTPrequestHandler version")
    sys.exit(1)

class RequestHandler(SimpleHTTPRequestHandler):

    def guess_type(self, path):
        self.mime = magic.Magic(mime=True)
        return self.mime.from_file(path)

if __name__ == '__main__':
    BaseHTTPServer.test(RequestHandler, BaseHTTPServer.HTTPServer)
