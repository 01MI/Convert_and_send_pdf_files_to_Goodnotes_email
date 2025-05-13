# Python script to automatically convert and send PDFs to goodnotes email.

## Context

Goodnotes is a note-taking app that includes a feature allowing users to send PDF files to the app via a private Goodnotes email address. Only PDF files are accepted through this feature.\
This script lets you convert and send multiple images or documents in a single email from your Gmail account to your Goodnotes email address..

It uses img2pdf and pandoc for file conversion. You’ll find a list of supported input formats below.\
For archive files, only .zip is supported, and the script cannot extract nested archives.

## Prerequisites
1. You will need to install the dependencies listed in requirements.txt
   ```
   pip3 install -r requirements.txt
   ```
3. You will need to create a .env file with the following information.\
   I recommand creating a separate Gmail account for this purpose.
   ```
   EMAIL_SENDER = your Gmail address
   EMAIL_PASSWORD = your Gmail password
   EMAIL_RECEIVER = your goodnotes email
   ```

## Usage

You will need to place this script and the .env file in the same directory as the files you want to convert and send.\
There are 2 commands:

1. The following command will convert all supported files in the current directory and its subdirectories.\
   It will also extract any .zip files into a folder and convert their contents(including files in subdirectories).
    ```bash
   python3 main.py
   ```
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


3. You can choose to only send already converted PDF files by using the ```-send-only``` argument.\
   This command will search for all PDF files in the current directory and its subdirectories.\
   It will also extract .zip files to look for PDFs inside them.
   ```bash
   python3 main.py -send-only
   ```
   Exemple:
   <table>
      <tr>
         <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/6071df21-c0c8-4b2e-aa3a-3fc8304aff32"></td>
         <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/9c8a7bc9-0d5c-47bf-9d21-84a5fe52bbac"></td>
      </tr>
   </table>

## Note: 
- This script extracts .zip files into folders with the same name. If a folder with that name already exists, the program will stop.
- If a file is converted and a PDF with the same name already exists, the existing PDF will be overwritten by the newly converted file.
<table>
   <tr>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/a22a93cb-40cc-46d4-a7ed-a8dd95f00a78"></td>
   </tr>
</table>

## Conversion formats

Here are the input formats supported by this script:\
For Img2pdf:\
Table of supported input formats from https://pypi.org/project/img2pdf/ : 
<table>
   <tr>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/f4ec4b68-a10d-450f-b7b2-532dcc7aeb69"></td>
   </tr>
</table>

For Pandoc:\
Table of supported input formats from Pandoc User's Guide https://pandoc.org/MANUAL.html :
<table>
   <tr>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/cd66ed21-a0fe-418e-ae96-409860ff0fdf"></td>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/093407d0-345f-4388-a4f2-295b422fac5c"></td>
      <td valign="middle"><img src="https://github.com/01MI/convert-and-send-pdf-files-to-goodnotes-email/assets/151965188/160c9900-d4cc-4352-b33d-6e22b05d032a"></td>
   </tr>
</table>

## To do

1. Add support for other email providers.
2. Implement support for more archive formats, only .zip files are currently supported.
3. Add support for nested archives.








