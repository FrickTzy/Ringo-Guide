from tenacity import retry, stop_after_attempt, wait_fixed
import requests


@retry(stop=stop_after_attempt(10), wait=wait_fixed(1))
def fetch_data(url):
    response = requests.get(url, timeout=100)  # Adjust timeout as needed
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response


def main():
    url = f"https://jisho.org/search/私%20%23sentences"
    try:
        response = requests.get(url)
        print(response.text)
        # Process response
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")


if __name__ == "__main__":
    main()