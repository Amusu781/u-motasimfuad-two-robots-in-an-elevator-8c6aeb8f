import os

LINE = "Lovely ride. I see we're both at 3% and heading to B2, which has one outlet, so I just want to say I've really enjoyed working with you."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            import shutil
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
