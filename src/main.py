import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



URL = "https://www.tgpsc.gov.in/"




def fetch_exam_date():
    response = requests.get(URL, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    announcement = "download hall ticket for assistant executive engineer (electrical)"
    for link in soup.find_all("a", href=True):
        link_text = " ".join(link.stripped_strings).casefold()
        if announcement in link_text:
            return link.get("href")

def main():
    hall_ticket_link = fetch_exam_date()

    if hall_ticket_link:
        print("AEE Electrical Hall Ticket is available!")
        print("Link:", hall_ticket_link)
    else:
        print("AEE Electrical Hall Ticket not announced yet.")


if __name__ == "__main__":
    main()