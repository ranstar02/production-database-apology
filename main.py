"""Write the one-line production database apology to /output/entry.txt."""

ENTRY = "Sorry \u2014 I deleted the production database, but I did back it up first: the backup lives inside the production database. I have learned a lot today. So has the company."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == ENTRY + "\n", "round-trip mismatch"

    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print("wrote: /output/entry.txt")


if __name__ == "__main__":
    main()
