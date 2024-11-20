import requests
from typing import Optional


def crawl(time_limit: int = 60, source: str = 'https://en.wikipedia.org/wiki/Main_Page', return_format: str = 'csv') -> \
Optional[str]:
    """
    Crawl data from a specified source within a given time limit and return the data in a specified format.

    :param time_limit: The maximum time (in seconds) to spend crawling. Default is 60 seconds.
    :param source: The source to crawl data from. Default is 'https://en.wikipedia.org/wiki/Main_Page'.
    :param return_format: The format in which to return the data. Default is 'csv'.
    :return: The crawled data in the specified format, or None if no data is found.
    """
    try:
        # Set a timeout for the request
        response: requests.Response = requests.get(source, timeout=time_limit)

        # Check if the request was successful
        if response.status_code == 200:
            # Process the response data
            data = response.text
            if return_format == 'text':
                # todo handle text formats CSV formatu, dictionary formatu, list formatu, objektais
                return data
            else:
                return data
        else:
            print(f"Failed to retrieve data: HTTP {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
