import gdown

# Google Drive Shareable Link (Modify this with your actual file ID)
drive_link = "https://drive.google.com/drive/folders/1uKQhz2myuHmYzCXvKYMs2UEgaoaXDVXh?usp=drive_link"
output = "my_dataset_file.zip"  # Change to your file name

# Download the file
gdown.download(drive_link, output, quiet=False)
print("Download complete!")