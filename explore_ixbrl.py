from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def explore_ixbrl(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")

    count = 0
    print("📊 Showing financial (numeric) tags only...\n")
    for tag in soup.find_all("ix:nonfraction"):  # this targets numeric values only
        tag_name = tag.get("name")
        tag_value = tag.text.strip()
        print(f"{tag.name:15} | {tag_name:40} | {tag_value}")
        count += 1
        if count >= 30:
            break

if __name__ == "__main__":
    # Update this path to match your latest download
    path = "sec-edgar-filings/AMZN/10-K/0001018724-25-000004/primary-document.html"
    explore_ixbrl(path)
