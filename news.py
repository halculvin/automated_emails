import requests as requests


class NewsFeed:
    """
    Representing multiple news titles and links as a single string
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "1b89f39252304b43926a3c1ed4321c88"

    def __init__(self, interest, from_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.language = language

    def get(self):
        """A function to construct the email body"""
        url = self._build_url()
        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        """A function to retrieve articles from the url provided"""
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        """A function to build the url"""
        url = f"{self.base_url}" \
              f"q={self.interest}&" \
              f"from={self.from_date}&" \
              "sortBy=publishedAt&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url



