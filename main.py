class file_detector:
    
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_type(self):
        try:
            with open(self.file_path, 'rb') as file:
                magic = file.read(2)

                if magic == b'BM':
                    return "BMP"
                
                elif magic == b'MZ':
                    file.seek(60)
                    pe_offset = int.from_bytes(file.read(4), 'little')
                    file.seek(pe_offset)
                    pe_header = file.read(4)
                    
                    if pe_header == b'PE\0\0':
                        file.seek(pe_offset + 22)
                        characteristics = int.from_bytes(file.read(2), 'little')

                        if characteristics & 0x2000:
                            return "DLL"
                        else:
                            return "EXE"
                    else:
                        return "Other file"
                else:
                    return "Other file"
                
        except FileNotFoundError:
            return "File not found"
        
        except Exception as e:
            return f"Error: {e}"

def main():
    while True:
        file_path = input("where is your file? 'quit' to quit: ")
        if file_path == 'quit':
            print("bye...")
            break
        fb = file_detector(file_path)
        ext = fb.get_file_type()
        print(ext)

main()
