import os

ENTRY_TEXT = ("She called yesterday, asked about my son's first day of school, and knew his teacher's name; his adoption papers list her as his birth mother, dead since 1987.")

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass

if __name__ == "__main__":
    main()
