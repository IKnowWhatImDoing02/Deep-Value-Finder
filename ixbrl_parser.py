from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
from tag_candidates import TAG_CANDIDATES


def extract_latest_value(soup, tag_name):
    annual_values = []
    all_values = []

    for tag in soup.find_all("ix:nonfraction", attrs={"name": tag_name}):
        val = tag.text.strip().replace(",", "").replace("(", "-").replace(")", "")
        context_ref = tag.get("contextref", "").lower()
        try:
            value = float(val)
            all_values.append(value)
            if any(term in context_ref for term in ["fy", "annual", "ytd", "12m"]):
                annual_values.append(value)
        except:
            continue

    if annual_values:
        return max(annual_values)  # Prefer highest annual value
    if all_values:
        return max(all_values)     # Fallback to highest of any value
    return None


def safe_float(val):
    try:
        return float(str(val).replace(",", "").strip())
    except (ValueError, TypeError):
        return None

def parse_ixbrl(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")

    data = {}
    for label, tags in TAG_CANDIDATES.items():
        found = None
        for tag in tags:
            value = extract_latest_value(soup, tag)
            if value is not None:
                found = value
                break
        data[label] = found

    return data
