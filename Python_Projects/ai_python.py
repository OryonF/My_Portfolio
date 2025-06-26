from bs4 import BeautifulSoup
import requests

def decode_secret(doc_url):
    response = requests.get(doc_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    x_col = "x-coordinate"
    char_col = "Character"
    y_col = "y-coordinate"

    # Grab all table cell values
    cells = [td.get_text(strip=True) for td in soup.find_all('td')]

    entries = []
    for i in range(0, len(cells), 3):
        col = cells[i:i+3]
        if col == [x_col,char_col,y_col]:
            continue
        try:
            #print(f"Parsing chunk: {col}")
            x = int(col[0])
            char = col[1]
            y = int(col[2])
            entries.append((char, x, y))
        except (IndexError, ValueError):
            print(f"Skipping invalid entry at index {i}")
            continue

    if not entries:
        print("No valid entries found.")
        return

    max_x = max(x for _, x, _ in entries)
    max_y = max(y for _, _, y in entries)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for char, x, y in entries:
        grid[max_y - y][x] = char

    for row in grid:
        print(''.join(row))

decode_secret('https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub')