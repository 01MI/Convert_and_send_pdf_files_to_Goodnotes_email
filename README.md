# Python script to automatically convert and send PDFs to goodnotes email.

## Context

Goodnotes is a note-taking app with a functionnality that allows users to send PDFs files(only) to their goodnotes app using a private goodnotes email.
This script allows you to convert and send images/documents from your gmail address to your goodnotes email address.

This script uses img2pdf and pandoc for the conversion part, you will find a list of supported input formats below.\
For zips, it only supports zips and cannot extract nested zips.

## Prerequisites
1. You will need to install the dependencies specified in requirements.txt
2. You will need to create a .env file with the following informations.\
   I recommand creating a new gmail account for this usage.
   ```
   EMAIL_SENDER = your gmail
   EMAIL_PASSWORD = your gmail password
   EMAIL_RECEIVER = your goodnotes email
   ```

## Usage

You will need to move this script and .env in the same directory where are located the files you want to convert and send.\
There are 2 commands:

1. The following command will convert any files in the current directory and subdirectories.\
   It will extract zips in a folder and convert their files(directory and subdirectories).
   
   Example:
   <table>
      <tr>
         <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/51beda88-68d2-4f78-abc0-c872b6133915" width="900"></td>
      </tr>
   </table>
   <table>
      <tr>
        <td align="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/194dd68c-afa3-428f-9d38-cc21b896e5b3"></td>
        <td align="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/4da23303-d4e2-4759-9508-2519744437c8"></td>
      </tr>
   </table>


3. You can decide to only send already converted PDFs files using the argument "-send-only".
   This following command will look for any PDFs files in the current directory and subdirectories.\
   It will extract files from zips to look for PDFs files.
   ```bash
   python3 main.py
   ```
   Exemple:
   <table>
      <tr>
         <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/6071df21-c0c8-4b2e-aa3a-3fc8304aff32"></td>
         <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/9c8a7bc9-0d5c-47bf-9d21-84a5fe52bbac"></td>
      </tr>
   </table>

## Note: 
- This script extracts a zip in a folder of the same name, if a folder already exists the programm stops.
- If you convert a file and a PDF of the same name already exists, your PDF will be overwritten with the new converted PDF file.
<table>
   <tr>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/a22a93cb-40cc-46d4-a7ed-a8dd95f00a78"></td>
   </tr>
</table>

## Conversion formats

Here are the following inputs files supported by this script:\
For Img2pdf:\
Table of inputs format from https://pypi.org/project/img2pdf/ : 
<table>
   <tr>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/f4ec4b68-a10d-450f-b7b2-532dcc7aeb69"></td>
   </tr>
</table>

For Pandoc:\
Table of inputs format from Pandoc User's Guide https://pandoc.org/MANUAL.html :
<table>
   <tr>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/cd66ed21-a0fe-418e-ae96-409860ff0fdf"></td>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/093407d0-345f-4388-a4f2-295b422fac5c"></td>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/160c9900-d4cc-4352-b33d-6e22b05d032a"></td>
   </tr>
</table>

## To do

1. Support for other email providers.
2. Support for other types of archives, currently it only supports zips.
3. Support for nested zips.








