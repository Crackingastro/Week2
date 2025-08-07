## Overview

This project analyzes user reviews from Google Play for three major Ethiopian banking apps—Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank—to surface key drivers of user satisfaction and prevalent pain points .

---

## Goals

* Extract and preprocess review data from the Google Play Store
* Classify user sentiment (positive, negative, neutral)
* Identify dominant themes from reviews using NLP techniques
* Provide actionable insights to enhance user experience within these banking apps

---

## Repository Structure (Estimated)

Here’s a likely layout based on your repo's folder names:

```
Week2/
├── notebooks/            # Jupyter notebooks for analysis and visualization
├── scraper.py            # Script for scraping Google Play reviews
├── Visualization/        # Visual assets (e.g., word cloud images, charts)
├── .gitignore
└── README.md             # (You’re writing this now!)
```

---

## Getting Started

### Prerequisites

You'll need:

* Python 3.7+
* Libraries such as: `pandas`, `wordcloud`, `google_play_scraper`, `spacy`, `transformers`, `tqdm`, `NLTK`, `spaCy`, `scikit-learn`, and `matplotlib`.

### Installation

```bash
git clone https://github.com/Crackingastro/Week2.git
cd Week2
```

### Usage

1. **Scrape in-app feedback**

   ```bash
   python scraper.py
   ```
2. **Explore and analyze within notebooks**
   Open and run notebooks in `notebooks/` for sentiment classification and theme extraction.
3. **View visualizations**
   Check out figures and plots under `Visualization/`.

---

## Methodology Highlights

* **Data Collection**: Reviews were scraped from the Google Play Store for CBE, BOA, Dashen Bank apps
* **Preprocessing**: Text cleaning including tokenization, removal of stop words, and normalization
* **Sentiment Analysis**: Classification of reviews into sentiment categories using NLP tools
* **Theme Extraction**: Application of techniques like TF‑IDF and keyword analysis to uncover recurring topics, both positive (e.g., usability, convenience) and negative (e.g., crashes, performance issues)
* **Insights**: CBE and Dashen Bank apps show moderate satisfaction; BOA has comparatively more negative feedback. Recommended improvements include better app stability, performance optimization, and enhanced UX design .

---

## Key Findings

* **CBE & Dashen Bank**: Moderately positive reviews indicating decent user satisfaction
* **Bank of Abyssinia (BOA)**: Higher volume of negative comments, signaling areas that need attention
* **Suggested Enhancements**: Streamline performance, reduce crashes, and improve feature interactivity and responsiveness 

---

## How to Contribute

* **Add coverage** for Sense of Banking apps (iOS, different platforms)
* Explore alternative NLP approaches: e.g., LDA, BERT-based clustering
* Fine-tune sentiment models for Amharic or Afaan Oromo reviews
* Build an interactive dashboard to visualize user sentiment and evolving themes



