# WordPress.com Support Documentation Crawler
Scrapy-powered documentation scraper for WordPress.com support docs to scrape document links, titles, and excerpts from.

This Scrapy crawler is intended to scrape the public WordPress.com forums based on a tag's URL, and save the resulting post title, URL, and text of the messages into a MySQL database. You can install the needed packages using `pip install -r requirements.txt`; it's recommended to run this in a virtualenv.

1. Create a MongoDB instance/collection using `topic_title`, `topic_link`, and `topic_description` as columns.
2. Update the authentication information for MongoDB in `forum_tag/forum_tag/pipelines.py`
3. Edit the `start_urls` in `support_docs_crawler/support_docs_crawler/spiders/support_docs.py` to reflect the URL for the tag/tags that you want to scrape.
4. Run the spider by using `scrapy runspider support_docs_crawler/support_docs_crawler/spiders/support_docs.py`.

While this is written specifically for the WordPress.com support docs, it should be easily modifiable to work on any documentation site by tweaking the selectors in the `parse` function in `support_docs.py`.
