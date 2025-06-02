# Normandy COVID-19 Dashboard

## Project Description

This project is a web application designed to visualize COVID-19 data, likely focusing on the Normandy region of France. It uses Python with Flask, Dash, and Pandas to create interactive dashboards.

There appear to be two main application entry points: `app.py` and `appdash.py`.

## Technologies Used

*   Python
*   Flask
*   Dash
*   Plotly
*   Pandas

## Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    The project's dependencies are listed in `requierments.txt`.
    ```bash
    pip install -r requierments.txt
    ```
    *Note: The dependencies in `requierments.txt` have been updated from their original 2020 versions to more recent ones as of July 2024. This process involved resolving several compatibility issues.*

## How to Run the Application

The application can be started using either `app.py` or `appdash.py`.

To run `app.py`:
```bash
python app.py
```

To run `appdash.py`:
```bash
python appdash.py
```

Once started, the application should typically be accessible in a web browser at `http://127.0.0.1:8050/`.

## Data Source

*   The primary data for the dashboard is expected to be in `covid.csv`.
*   **Current Data Status**: The `covid.csv` file in the repository is outdated and contains data only up to **March 30, 2020**.
*   **Data Update Attempts**: Efforts were made to automatically update this data with more recent information (up to March/June 2023 from official French government sources). However, these attempts were hindered by technical limitations within the automated execution environment, specifically timeouts when trying to download the large (approx. 13.6MB) updated data file. Therefore, the outdated data file remains in place. Users interested in the most current data may need to manually source and integrate it.

## Known Issues and Limitations

*   **Outdated Data**: As mentioned above, the `covid.csv` is from March 2020.
*   **Incomplete Recent Testing**: During the most recent automated update session (July 2024), full testing of the web application's interface (visualizations, interactivity) after dependency updates could not be completed due to timeouts in the testing environment. While the applications (`app.py`, `appdash.py`) appeared to launch when run directly, their behavior when accessed via a web browser was not fully verified in that session.
