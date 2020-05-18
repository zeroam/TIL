from pathlib import Path
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

from utils import timeit


def download_one(url):
    """
    Downloads the specified URL and saves it to disk
    """
    req = urllib.request.urlopen(url)
    fullpath = Path(url)
    fname = fullpath.name
    ext = fullpath.suffix

    if not ext:
        raise RuntimeError("URL does not contain an extension")

    with open(fname, "wb") as handle:
        while True:
            chunk = req.read(1024)
            if not chunk:
                break
            handle.write(chunk)

    msg = f"Finished downloading {fname}"
    return msg


@timeit
def download_all(urls):
    return [download_one(url) for url in urls]


@timeit
def download_all_multithread(urls):
    """
    Create a thread pool and download specified urls
    """

    with ThreadPoolExecutor(max_workers=6) as executor:
        return executor.map(download_one, urls, timeout=60)


if __name__ == "__main__":
    urls = (
        "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf",
    )

    # 1 thread
    results = download_all(urls)
    for result in results:
        print(result)

    # 6 threads
    results = download_all_multithread(urls)
    for result in results:
        print(result)

    # remove files
    pdf_files = Path().rglob("*.pdf")
    [pdf_file.unlink() for pdf_file in pdf_files]
