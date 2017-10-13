# metaImage
## **General**
Python tool which provides the possibility to extract Metadata from Images.
The Format for the images are currently set to .jpg/jpeg
Features the following:
  * printing the metadata of an specified images.
  * downloading and printing the metadata of the image
  * [SOON] logging the meta data into .log

The extraction of the information is based onto the *EXIF-format*.

### **EXIF-Format**
The EXIF-Format was originially founded by the japanese inustry. It adds the abillity to append several information
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
  
