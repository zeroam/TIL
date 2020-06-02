# backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments
import os
import zipfile


def backup_to_zip(folder):
    # Back up the entire contents of "folder" into a ZIP file

    # Figure out the filename this code should use based on what files already exist
    number = 1
    while True:
        zip_filename = f"{folder}_{number}.zip"
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the ZIP file
    print(f"Creating {zip_filename}...")
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for curfolder, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {curfolder}...')
        backup_zip.write(curfolder)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            filepath = os.path.join(curfolder, filename)
            print(f"  Adding file {filepath}...")
            backup_zip.write(filepath)

    backup_zip.close()
    print("Done")


if __name__ == "__main__":
    backup_to_zip("dates_sample")
