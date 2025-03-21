import requests
from bs4 import BeautifulSoup


def get_latest_patch_notes_url(
    base_url="https://www.leagueoflegends.com/pt-BR/news/tags/patch-notes/"
) -> str:
    """
    Obtém a URL das notas do patch mais recente do League of Legends.
    Args:
        base_url: URL base para buscar as notas de patch

    Returns:
        URL das notas do patch mais recente

    Raises:
        ValueError: Se não for possível encontrar a URL das notas do patch
    """
    response = requests.get(base_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    article_links = soup.find_all("a")
    for link in article_links:
        href = link.get("href")
        if href and "patch" in href and "game-updates" in href:
            if href.startswith("/"):
                href = "https://www.leagueoflegends.com" + href
            return href

    raise ValueError("Não foi possível encontrar as notas do patch mais recente")


def fetch_latest_patch_notes_text() -> str:
    """
    Obtém o texto completo das notas do patch mais recente.

    Returns:
        Texto completo das notas do patch mais recente
    """
    url = get_latest_patch_notes_url()
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator="\n")
