import os


def find_files_with_extensions(folder, extensions):
    files_with_extensions = []

    for file in os.listdir(folder):
        if file.endswith(tuple(extensions)):
            files_with_extensions.append(file)

    return files_with_extensions


if __name__ == "__main__":
    folder = os.getcwd()  # Current working directory
    extensions = (".pdf.scr", ".pdf.exe")

    files_with_extensions = find_files_with_extensions(folder, extensions)

    if files_with_extensions:
        print("Files found with extensions (.pdf.scr, .pdf.exe):")
        for file in files_with_extensions:
            print(f"- {file}")
    else:
        print("No files found with extensions (.pdf.scr, .pdf.exe)")
