# pathlib provides an object-oriented way to work with files and paths.
# It is more modern but slightly advanced compared to open().
from pathlib import Path

Path("file.txt").write_text("Hello World\n")
content = Path("file.txt").read_text()
print(content)