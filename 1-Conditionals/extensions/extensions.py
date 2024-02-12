# File text
#   .gif = image/gif
#   .jpeg = image/jpeg
#   .png = image/png
#   .pdf = application/pdf
#   .txt = text/plain
#   .zip = application/zip


def main():
    file_type = input(("Enter file name : ")).casefold()
    if (".gif") in file_type:
        print("image/gif")
    elif (".jpeg") in file_type:
        print("image/jpeg")
    elif (".png") in file_type:
        print("image/png")
    elif (".pdf") in file_type:
        print("application/pdf")
    elif (".txt") in file_type:
        print("text/plain")
    elif (".zip") in file_type:
        print("application/zip")
    else:
        print("application/octet-stream")


main()
