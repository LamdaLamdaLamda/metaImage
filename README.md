# metaImage
## **General**
Python tool which provides the possibility to extract Metadata from Images.
The Format for the images are currently set to .jpg/jpeg
Features the following:
  * printing the metadata of an specified images.
  * downloading and printing the metadata of the image
  * removing metadata (EXIF-tags) of the argument.
  * [SOON] logging the meta data into .log

The extraction of the information is based onto the *EXIF-format*.

### **EXIF-Format**
The EXIF-Format was originially founded by the japanese industry. It adds the abillity to append several information
to images (.jpg/jpeg and .tiff).
Metadata basically constsis of the following informations:
 * date and time
 * ISO-value
 * information about the flashing.
 * focal length
 * several geo informations

 The possibility to download images from the web is restricted by some platforms, which means some metadata are removed by
 the website itself right before the downloading process.

 **More infos on:** [Metadata and Webservices](http://www.embeddedmetadata.org/social-media-test-results.php "Nick nack paddiwack!")

## **Package Requirements**
The following packages are necessary to excecute the **metaImage.py**.
  * PIL - Pillow -> **pip install Pillow**
  * Argument Parser - argparse -> **pip install argparse**

Depending on what python version you use you have to import a different **urllib** version.
This is why I inserted a dependent import strucutre at the beginning of the script.
In general you can install urllib2 if you use **python2.X** otherwise I recomment **urllib3** which
is acctually merged into **urllib**. As far as I know.

  * URL Libarry -> **pip install urllib**

## **Setup**
To add **metaImage.py** to your interpeter path you can execute the **setup.sh**
as follows:
  * **sudo bash setup.sh metaImage.sh**

In your case it might be not neccessary to run it with **sudo**. It depends on your
privileges.
The Script just simply copies the tool to /bin/ and marks it as executable.

After the script finished successfully you can run the tool with:
  * **metaImage [OPTIONS] [IMAGE]**
