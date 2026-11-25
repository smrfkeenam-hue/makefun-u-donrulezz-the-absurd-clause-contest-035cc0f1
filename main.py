import os

# The Absurd Clause Contest: one sentence, an absurd clause buried in a ToS.
ENTRY = "By using the Service, you grant the Company a perpetual, irrevocable licence to all crumbs you produce, including the right to resell them to pigeons at market rate."

with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)  # no trailing newline: the entry is exactly one sentence

