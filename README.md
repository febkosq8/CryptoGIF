# **CryptoGIF**
A Web based GUI that enables data hiding in images(including GIF's) securely with the use of steganography and data encryption. It makes use of a [python steganography module](https://github.com/computationalcore/cryptosteganography) to store messages or files protected with AES-256 encryption inside an image.

Steganography is the art of concealing information within different types of media objects such as images or audio files, in such a way that no one, apart from the sender and intended recipient, suspects the existence of the message. By default steganography is a type of security through obscurity.

A research paper has been published on the same : [Springer](https://link.springer.com/chapter/10.1007/978-981-16-1773-7_32)

## **Proposed System**
To start with, we ask the user to input their choice of GIF (Graphics Interchange Formats). We then send the specific GIF into the processing engine which de-frames the GIF into individual images which when viewed in a defined motion acts like a GIF. We number all the breakdown images from the GIF to facilitate easy processing later into the engine. We then ask the user for the data to be encrypted and stored inside the specified GIF. We run the data through the encryption engine which encrypts the data using AES-256 bit encryption. This data is passed on down the engine to be embedded onto the images derived from the GIF in order to facilitate hiding the data in the specified GIF. After the data is hidden, we combine all the images back in the same order to form a GIF, which to the world seems like any other GIF image. After this we encrypt the GIF with the hidden data with a secure key that would be needed to decrypt the GIF and hence the data hidden inside it. This means that for the recipient of the secured data image, they should have the GIF image along with the decrypt key to successfully extract the data out of the GIF file.

![Diagram](https://user-images.githubusercontent.com/33223665/152702403-ea580a63-0384-4d87-92b0-b6fd29a7e0bc.png)

## **Instructions to host Web-GUI**
Use these instructions to run the web server locally on your system [Link](/RunInstructions.md)

## **Release**

_v1.0 - initial version which has been tested and confirmed working for storing data in jpeg, png files [Link](https://github.com/febkosq8/CryptoGIF/releases/tag/v1.0)_
