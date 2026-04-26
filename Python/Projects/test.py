import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url: str):
    response = requests.get(doc_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    points = []

    # Find all table rows
    rows = soup.find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        
        if len(cols) == 3:
            try:
                x = int(cols[0].text.strip())
                char = cols[1].text.strip()
                y = int(cols[2].text.strip())
                points.append((x, char, y))
            except:
                continue

    if not points:
        print("No valid data found.")
        return

    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, _, y in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, char, y in points:
        grid[y][x] = char

    for row in grid:
        print("".join(row))


decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")