"""
This script scrapes a webpage 'O Rol de Procedimentos e Eventos em Saúde' for PDF links, 
downloads the files, and compresses them into a zip file.

by @luc-llb
"""

import requests
from bs4 import BeautifulSoup
import os

def get_page(url: str) -> BeautifulSoup:
    """
    Fetches the HTML content of a webpage and returns a BeautifulSoup object.

    :param url: str - The URL of the webpage to fetch.
    :return: BeautifulSoup - Parsed HTML content of the webpage.
    :raises Exception: If the page cannot be loaded.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")
    
    return BeautifulSoup(response.content, 'html.parser')

def get_pdf_links(soup: BeautifulSoup) -> list[str]:
    """
    Extracts all PDF links from the BeautifulSoup object.

    :param soup: BeautifulSoup - Parsed HTML content of the webpage.
    :return: list[str] - List of PDF links found in the webpage.
    """
    link_files = [link.get('href') for link in soup.find_all('a') 
                  if link.get('href') and (link.get('href').endswith('.pdf'))]
    return link_files

def download_file(url: str, folder_path: str) -> None:
    """
    Downloads a file from a given URL and saves it to a specified folder."

    :param url: str - The URL of the file to download.
    :param folder_path: str - The path to the folder where the file will be saved.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filename = os.path.join(folder_path, url.split('/')[-1])
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download {url}: {response.status_code}")

def compact_files(folder: str, save_in_parent: bool = False) -> None:
    """
    Compresses all files in a specified folder into a zip file.
    
    :param folder: str - The path to the folder to compress.
    :param save_in_parent: bool - If True, saves the ZIP in the parent folder.
    """
    import zipfile
    
    if not os.path.exists(folder):
        print(f"{folder} does not exist.")
        return
    if not os.path.isdir(folder):
        print(f"{folder} is not a directory.")
        return
    if not os.listdir(folder):
        print(f"{folder} is empty.")
        return

    folder = folder.rstrip('/\\')
    folder_name = os.path.basename(folder)

    zip_path = os.path.join(os.path.dirname(folder) if save_in_parent else folder, f"{folder_name}.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)

                # Avoid adding the zip file itself to the zip
                # This is important if you are zipping the folder where the zip file will be saved
                if file_path == zip_path:
                    continue

                zipf.write(file_path, os.path.relpath(file_path, folder))
    print(f"Created zip file: {zip_path}")

def main():
    url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
    folder_path = './1-scraping/files/'

    # Get the page content
    soup = get_page(url)
    link_files = get_pdf_links(soup)
    
    if not link_files:
        print("No files found.")
        return
    
    link_files = [link for link in link_files if 'Anexo' in link] # Filter for 'Anexo'

    # Download each file
    for link in link_files:
        download_file(link, folder_path)

    # Compact the downloaded files
    compact_files(folder_path)
    print("All files downloaded and zipped successfully.")

if __name__ == "__main__":
    main()