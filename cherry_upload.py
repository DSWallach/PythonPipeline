import os
import os.path

import cherrypy
from cherrypy.lib import static

localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)


class FileDemo(object):

    @cherrypy.expose
    def index(self):
        return """
        <html><body>
        <h2>Upload a file</h2>
        <form action='upload' method='post' enctype='multipart/form-data'>
        filename: <input type='file' name='myFile' /> <br />
        <input type='submit' />
        </form>
        <h2>Download file</h2>
        <a href='download'>This one</a>
        </body></html>
        """

    @cherrypy.expose
    def upload(self, myFile):
        out = """<html>
        <body>
            myFile length: %s <br />
            myFile filename: %s <br />
            myFile mime-type: %s
        </body>
        <html>"""

        size = 0
        while True:
            data = myFile.file.read(8192)
            if not data:
                break
            size += len(data)

        return out % (size, myFile.filename, myFile.content_type)

    @cherrypy.expose
    def download(self):
        path = os.path.join(absDir, 'pdf_file.pdf')
        return static.serve_file(path, 'application/x-download',
                                 'attachment', os.path.basename(path))


tutconf = os.path.join(os.path.dirname(__file__), 'cherry.conf')

if __name__ == '__main__':
    cherrypy.quickstart(FileDemo(), config=tutconf)
