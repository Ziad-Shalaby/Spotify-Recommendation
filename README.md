# Spotify Recommendation System

## Project Overview

This project implements a recommendation system for Spotify, utilizing similarity analysis to suggest songs based on user preferences. The system relies on a combination of scraped data and a pre-prepared dataset to build an efficient and scalable recommendation engine. It includes a web scraping component to gather additional data, preprocessing steps to generate the similarity file, and a deployment script to make the recommendations accessible through a user-friendly interface.

## Table of Contents

1. [Features](#features)
2. [Data Collection](#data-collection)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)

## Features

- **Song Recommendation:** Suggests songs based on user inputs and preferences.
- **Similarity Analysis:** Uses a precomputed similarity file for efficient recommendations.
- **Web Scraping:** Collects song data, including metadata and audio features, from Spotify or similar platforms.
- **Dataset Integration:** Incorporates a pre-prepared dataset to complement the scraped data.
- **Deployment Ready:** Includes deployment scripts for running the project in a local or online environment.

## Data Collection

The data used for this project comes from two main sources:

1. **Web Scraping:**
   - A Python script (`scraper.py`) is used to scrape song data from online sources.
   - The script gathers song titles, artist names, genres, and audio features (e.g., tempo, energy, danceability).

2. **Prepared Dataset:**
   - In addition to scraped data, a pre-prepared dataset is used to ensure the recommendation system has comprehensive and high-quality data.
   - This dataset provides a rich set of audio features and metadata that are preprocessed and ready for use.

3. **Data Storage:**
   - Both the scraped data and the prepared dataset are combined and stored in a structured CSV file (`songs_data.csv`) for further processing.

4. **Preprocessing:**
   - The combined data is cleaned and processed to ensure consistency.
   - A similarity matrix is computed based on audio features, and the result is saved as `similarity.pkl` for use in the recommendation system.

## Prerequisites

- **Python 3.8 or above**
- **Required Libraries:** Listed in `requirements.txt`
- **Similarity File:** Ensure the similarity file (`similarity.pkl`) is included in the project directory. This file is essential for the system to function.

## Installation

To set up this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ziad-Shalaby/Spotify-Recommendation.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Spotify-Recommendation
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment:**

   - On Windows:

     ```bash
     env\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source env/bin/activate
     ```

5. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the web scraping script (optional):**

   If you need to scrape new data:

   ```bash
   python scraper.py
   ```

   Ensure the output CSV file is saved in the project directory.

2. **Generate the similarity file (if needed):**

   If the similarity file is not present or needs to be updated:

   ```bash
   python generate_similarity.py
   ```

3. **Run the project:**

   Make sure the similarity file (`similarity.pkl`) is present in the project directory. Then, execute the deployment script:

   ```bash
   python app.py
   ```

4. **Access the application:**

   Open your web browser and navigate to `http://localhost:5000` to interact with the recommendation system.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the repository.**
2. **Create a new branch:**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make your changes and commit them:**

   ```bash
   git commit -m 'Add some feature'
   ```

4. **Push to the branch:**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a pull request.**

---

Thank you for exploring the Spotify Recommendation System! Your feedback and contributions are greatly appreciated.
