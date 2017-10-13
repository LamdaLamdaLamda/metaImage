from PIL import Image
from PIL import ExifTags
import sys
import os
import urllib2
import socket
from optparse import OptionParser


class MetaImage(object):

    def __init__(self):
        self.downloadURL = None
        self.options = None
        self.args = None
        self.image = None
        # Adding Optionparser options
        self.parser = OptionParser()
        self.parser.add_option('-s', '--source', dest='source', help='URL to the image [REQUIRED]', metavar='SOURCE')
        self.parser.add_option('-o', '--output', dest='output', help='file output [REQUIRED IF -s SET]', metavar='FILE')
        self.parser.add_option('-p', dest='printer', help='Simply prints metadata [OPTIONAL]')
        (self.options, self.args) = self.parser.parse_args()

    def verfyOptionSource(self):
        # checking all option and excute the selection
        if not self.options.printer and self.options.source:
            self.downloadImage()
            self.readMetaData()
        if self.options.printer and not self.options.source:
            self.options.output = self.options.printer
            self.readMetaData()

    def readMetaData(self):
        # checking for image jpg/jpeg format
        if (".jpg" or ".jpeg") not in self.options.output:
            print("Wrong output file format")
            exit(1)
        else:
            # opening the image -> Raise exception if it fails
            print("[*] Opening Image...")
            try:
                image = Image.open(self.options.output)
            except IOError:
                print("[-] Cant Open Image")
            # getting the exif tags and printing these tags
            # with the corresponding values
            try:
                for i,k in image._getexif().items():
                    if i in ExifTags.TAGS:
                        print(ExifTags.TAGS[i] + ": " + str(k))
            except AttributeError:
                print("[-] No Metadata found!")
                print("[-] Exiting...")
                sys.exit(1)

    def downloadImage(self):
        # set socket connection timeout
        socket.setdefaulttimeout(25)

        # preparing url request. To make sure that the request is recognized
        # as regular request, we need to ad a head (User-Agent etc.).
        req = urllib2.Request(self.options.source)
        req.add_header('User-Agent', 'Fake but made')

        # catching the case that the user gives a invalid link
        try:
            resp = urllib2.urlopen(req)
        except IOError:
            print("[-] Unable to Open Link!")
            sys.exit(1)

        imgdata = resp.read()
        # writing data to local image file
        with open(self.options.output, 'wb') as outfile:
            outfile.write(imgdata)


if __name__ == "__main__":
    os.system('clear')
    mettWurst = MetaImage()
    mettWurst.verfyOptionSource()
