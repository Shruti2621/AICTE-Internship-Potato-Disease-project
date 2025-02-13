import gdown

# Google Drive Shareable Link (Modify this with your actual file ID)
drive_link = "https://drive.google.com/file/d/1flzrcloeGIwFn3lwyO_cu0SQOx0ONlRd/view?usp=drive_link"
output = "my_large_file.zip"  # Change to your file name

# Download the file
gdown.download(drive_link, output, quiet=False)
print("Download complete!")