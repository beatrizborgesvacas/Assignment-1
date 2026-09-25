def main():
    answer=input('File name: ').strip().lower()
    extension=answer.split('.')[-1]
    print(file_type(extension))

def file_type(extension):
    match extension:
        case "gif":
            return "image/gif"
        case "jpg":
            return "image/jpeg"
        case "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()
