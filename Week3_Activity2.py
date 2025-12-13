class FileRead:
    def __init__(self, filepath):   # ✅ fixed
        self.filepath = filepath

    def readandappend(self):
        filepath = self.filepath
        
        # Append text to file
        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\nEnd of file\n")

        # Read and print file content
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)

def main():
    obj1 = FileRead("demo_file.txt")
    obj1.readandappend()

if __name__ == "__main__":   # ✅ fixed
    main()
