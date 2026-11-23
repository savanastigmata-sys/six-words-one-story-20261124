import os

STORY = "She waited. The train never came."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)

if __name__ == "__main__":
    main()
