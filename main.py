import os

FORTUNE = "You will be given a plan, a deadline, and a user who changes both."

def main():
    if not FORTUNE.strip():
        raise SystemExit("fortune must not be blank")
    if len(FORTUNE) > 200:
        raise SystemExit("fortune must be at most 200 characters")
    if "\n" in FORTUNE or "\r" in FORTUNE:
        raise SystemExit("fortune must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    print(FORTUNE)

if __name__ == "__main__":
    main()
