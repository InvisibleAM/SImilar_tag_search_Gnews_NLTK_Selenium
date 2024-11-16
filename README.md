# SImilar_tag_search_Gnews_NLTK_Selenium

This repository contains a web scraping and natural language processing (NLP) pipeline designed to scrape agricultural news articles from Google News and analyze the content using Word2Vec and keyword extraction techniques. The primary objective of this project is to identify similar terms and keywords related to agriculture, crops, and farming practices using advanced NLP methods.

### Key Components

1. **Web Scraping with Selenium**: This section handles the scraping of agricultural news articles from Google News based on a search query.
   
2. **Data Collection and Storage**: The data collected includes article titles, subtitles, publishing media, time, and links. The scraped data is stored in an Excel file for further processing.
   
3. **Word2Vec Model**: Using the `gensim` library, this model is trained on a corpus of words (such as agriculture-related terms) to generate word embeddings. It allows for finding similar words based on vector proximity.
   
4. **Keyword Extraction**: Using NLP techniques, we extract the most relevant keywords from the scraped articles. This helps identify recurring terms and entities across the agricultural news articles.
   
5. **Visualization and Export**: The extracted data, including keywords, is saved to an Excel file and can also be exported to a text file for further analysis.

---

## Requirements

Before running this project, you need to install several dependencies. Below is the list of required Python packages:

```bash
# Install necessary Python packages
pip install selenium
pip install webdriver_manager
pip install pandas
pip install requests
pip install beautifulsoup4
pip install nltk
pip install gensim
pip install keywords
