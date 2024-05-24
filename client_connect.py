from ftplib import FTP

# Connect to FTP server
ftp = FTP()
ftp.connect("127.0.0.1", 21)
ftp.login(user="user", passwd="password")


# Function to upload a file
def upload_file(file_path):
    with open(file_path, 'rb') as file:
        ftp.storbinary(f"STOR {file_path}", file)


# Function to download a file
def download_file(file_name):
    with open(file_name, 'wb') as file:
        ftp.retrbinary(f"RETR {file_name}", file.write)

print("Enter the location of the files")

# Example usage
upload_file('eg.txt')
print("File uploaded successfully!")

download_file(r'C:\Users\jayva\Downloads\eg.txt')
print("File downloaded successfully!")

ftp.quit()
