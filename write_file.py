# write_file.py
def write_to_file():
    with open("output.txt", "w") as f:
        f.write("Hello, GitHub Actions!\n")
        f.write("This file was created by a GitHub Actions workflow.\n")

if __name__ == "__main__":
    write_to_file()