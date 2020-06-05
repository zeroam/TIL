import zipfile

new_zip = zipfile.ZipFile("new.zip", "w")
new_zip.write("spam.txt", compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
