import os, smtplib, ssl, pypandoc, imghdr, zipfile, glob, img2pdf, sys, logging
from dotenv import load_dotenv
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(files):
    if len(files) >= 1:
        BASEDIR = os.path.dirname(__file__)
        load_dotenv(os.path.join(BASEDIR, '.env'))

        email_sender = os.getenv("EMAIL_SENDER")
        email_service = os.getenv("EMAIL_SERVICE")
        email_password = os.getenv("EMAIL_PASSWORD")
        email_receiver = os.getenv("EMAIL_RECEIVER")

        smtp_server = "smtp.gmail.com"
        port = 587

        message = MIMEMultipart('alternative')
        message['Subject'] = "PDF files to Goodnotes email"
        message['From'] = email_sender
        message['To'] = email_receiver

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls(context=context)
                server.login(email_sender, email_password)
                #print(message.as_string()) Debug
                for file in files:
                    print("• Attaching " + os.path.basename(file) + " to the email.")
                    with open(file, "rb") as f:
                        pdf = MIMEApplication(f.read(),_subtype="pdf")
                    pdf.add_header('Content-Disposition','attachment',filename=os.path.basename(file))
                    message.attach(pdf)
                server.sendmail(email_sender, email_receiver, message.as_string())
                server.quit()
            print("email sent!")
        except smtplib.SMTPException as e:
            print(f"An error occured while sending the email: {e}")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
    else:
        logging.error("There are no pdf files to send")
        exit()

def convert_pandoc(files):
    all_converted_files = []
    for file in files:
        try:
            filename_converted = os.path.splitext(os.path.basename(file))[0] + ".pdf"
            outputfile = os.path.join(os.path.dirname(file), filename_converted)
            if imghdr.what(file) != None:
                print("| Converting " + file)
                with open(file, "rb") as image_file:
                    image_data = image_file.read()
                with open(outputfile, "wb") as pdf_file:
                    pdf_file.write(img2pdf.convert(image_data))
                all_converted_files.append(outputfile)
            else:
                outputfile = os.path.join(os.path.dirname(file), filename_converted)
                print("| Converting " + file)
                pypandoc.convert_file(file, 'pdf', outputfile=outputfile)
                all_converted_files.append(outputfile)
        except RuntimeError as e:
            print("-> The file '" + file + "' has not been converted because its format is not supported by this script")
    return all_converted_files

def sort_filenames(current_directory):
    regular_files = []
    zip_files = []
    pdf_files = []
    for file in glob.glob(os.path.join(current_directory, '**'), recursive=True):
        if os.path.isfile(file):
            if file.endswith(".zip"):
                zip_files.append(file)
            elif not file.endswith('.py') and not file.startswith('.'):
                if file.endswith('.pdf'):
                    pdf_files.append(file)
                regular_files.append(file)
    return regular_files, zip_files, pdf_files

def extract_files(current_directory, zip_files):
    if len(zip_files) != 0:
        for zip_file in zip_files:
            print("(Extracting " + zip_file + ")")
            try:
                extract_archive(zip_file, current_directory)
            except FileExistsError as e:
                print("Error: The folder " + os.path.splitext(os.path.basename(zip_file))[0] + " already exists, cannot extract archive.")
                exit()
        filtered_files, zip_files, pdf_files = sort_filenames(current_directory)
    return filtered_files, pdf_files

def extract_archive(archive, current_directory):
    folder_name = os.path.splitext(os.path.basename(archive))[0]
    extract_folder = os.path.join(current_directory, folder_name)
    os.makedirs(extract_folder)
    with zipfile.ZipFile(archive, 'r') as archive_file:
        archive_file.extractall(extract_folder)

if __name__ == "__main__":
    current_directory = os.getcwd()
    regular_files, zip_files, pdf_files = sort_filenames(current_directory)
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "-send-only":
            filtered_files, pdf_files = extract_files(current_directory, zip_files)
            send_email(pdf_files)
    else:
        filtered_files, pdf_files = extract_files(current_directory, zip_files)
        converted_files = convert_pandoc(filtered_files)
        send_email(converted_files)