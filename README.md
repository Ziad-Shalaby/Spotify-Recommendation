# Spotify Recommendation System

## Project Overview

This project implements a recommendation system for Spotify, utilizing similarity analysis to suggest songs based on user preferences. It includes a preprocessed similarity file that is essential for running the project and deploying the system.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)

## Features

- **Song Recommendation:** Suggests songs based on user inputs and preferences.
- **Similarity Analysis:** Uses a precomputed similarity file for efficient recommendations.
- **Deployment Ready:** Includes deployment scripts for running the project in a local or online environment.

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

1. **Run the project:**

   Make sure the similarity file (`similarity.pkl`) is present in the project directory. Then, execute the deployment script:

   ```bash
   python app.py
   ```

2. **Access the application:**

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
