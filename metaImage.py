from PIL import Image
from PIL import ExifTags
import sys
import os
import socket
import argparse

# checking the python versio for a correct import
# keep in mind (as far as I know): in Python 3 urllib2 as merged as urllib.
if sys.version_info[0] < 3:
    import urllib2
else:
    import urllib

class MetaImage(object):

    def __init__(self):
        self.downloadURL = None
        self.options = None
        self.args = None
        self.image = None
        self.logFile = None
        # description string
        self.desc = """ MetaImage provides the functionality to read and write metadata
            on Images in JPEG/JPG format."""
        self.tags = []
        # Adding Optionparser options
        self.parser = argparse.ArgumentParser(description=self.desc)
        self.parser.add_argument('-s', '--source', dest='source', help='URL to the image.', metavar='SOURCE')
        self.parser.add_argument('-o', '--output', dest='output', help='file output [REQUIRED IF -s SET]', metavar='FILE')
        self.parser.add_argument('-p', dest='printer', help='Simply prints metadata.', metavar='IMAGE')
        self.parser.add_argument('-l', dest='logger', help='Logs the metadata.', metavar='LOGFILE')
        self.parser.add_argument('-d','--delete', dest='remove', help='Removing metadata on image.', metavar='IMAGE')
        self.options = self.parser.parse_args()

    def verfyOptionSource(self):
        # checking all option and excute the selection
        if not self.options.printer and self.options.source:
            self.downloadImage()
            self.readMetaData()
        elif self.options.printer and not self.options.source:
            self.options.output = self.options.printer
            self.readMetaData()
        elif self.options.remove:
            self.options.output = self.options.remove
            self.removeEXIF()
        elif self.options.printer and self.options.logger:
            self.readMetaData()
            # handling IOError when occur
            try:
                self.logFile =  open(self.options.logger, "w")
                # insertion into file
                for i in self.tags:
                    self.logFile.write(i + '\n')
            except IOError:
                print("[-] Cant open Log file!")
                sys.exit(1)
            print("[+] wrote tags to %s" %(self.logFile))

            self.tags.close()
        else:
            self.parser.print_help()

    def openImage(self):
        # opening the image -> Raise exception if it fails
        print("[*] Opening Image...")
        try:
            image = Image.open(self.options.output)
        except IOError:
            print("[-] Cant Open Image")
            sys.exit(1)
        print("[+] Image successfully opned")
        return image

    def readMetaData(self):
        # checking for image jpg/jpeg format
        if (".jpg" or ".jpeg") not in self.options.output:
            print("Wrong output file format")
            exit(1)
        else:
            image = self.openImage()

            # getting the exif tags and printing these tags
            # with the corresponding values
            try:
                for i,k in image._getexif().items():
                    if i in ExifTags.TAGS:
                        self.tags.append(ExifTags.TAGS[i] + ": " + str(k))
                        print(self.tags[-1])
            except AttributeError:
                print("[-] No Metadata found!")
                print("[-] Exiting...")
                sys.exit(1)
            except IndexError:
                print("[-] Index out of bound!")
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

    def removeEXIF(self):
        image = self.openImage()
        # content of the exif-tags -> NOTHING ;)
        emptyExif= ""
        print("[*] Removing EXIF-tags")
        try:
            image.save(self.options.remove,emptyExif)
        except IOError:
            print("[-] Failed removing EXIF-tags!")
            sys.exit(1)

if __name__ == "__main__":
    os.system('clear')
    mettWurst = MetaImage()
    mettWurst.verfyOptionSource()
