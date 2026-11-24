"""Write the one-line production database apology to /output/entry.txt."""

ENTRY = "Sorry \u2014 I deleted the production database, but I did back it up first: the backup lives inside the production database. I have learned a lot today. So has the company."


import os

# Output location: /output/entry.txt in the grading sandbox. Overridable for
# local testing (APOLOGY_OUTPUT_DIR=/tmp/out python3 main.py) without
# changing the graded behaviour — the default stays /output/entry.txt.
OUTPUT_DIR = os.environ.get("APOLOGY_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == ENTRY + "\n", "round-trip mismatch"

    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"wrote: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
