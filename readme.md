
# Time Series Analysis: Log Transformation and Box-Cox

This repository contains a time series analysis project that aims to make a series stationary. The project applies log transformations and the Box-Cox technique to the time series data, performs stationarity tests, and visualizes the results.

## Project Structure

```
TIME-SERIES-LOG-TRANSFORM-AND-BOX-COX
│   .gitignore
│   requirements.txt    
│
├── myenv                   # Virtual environment directory
│
├── notebook                # Jupyter notebooks for analysis
│   └── Making_series_stationary.ipynb
│
└── scripts                 # Python scripts for time series analysis
    └── time_series_log_transform_box_cox.py
```

## Installation

First, clone this repository to your local machine. Navigate to the cloned directory, and then you can set up the project environment by following these steps:

1. **Create a Virtual Environment (optional):**

```bash
python -m venv myenv
```

2. **Activate the Virtual Environment:**

- For macOS and Linux:

```bash
source myenv/bin/activate
```

- For Windows:

```bash
myenv\Scripts\activate
```

3. **Install Required Packages:**

```bash
pip install -r requirements.txt
```

## Usage

Open the Jupyter notebook to interactively explore the data and analysis:

```bash
jupyter notebook notebook/Making_series_stationary.ipynb
```

Alternatively, you can run the Python script directly:

```bash
python scripts/time_series_log_transform_box_cox.py
```

## Analysis Workflow

- Load the training and validation datasets.
- Convert the date column to datetime and set it as the index.
- Visualize the original and processed time series data.
- Perform Augmented Dickey-Fuller (ADF) and Kwiatkowski-Phillips-Schmidt-Shin (KPSS) tests to check for stationarity.
- Apply log transformation and differencing to achieve stationarity.
- Apply Box-Cox transformation to the series and visualize the results.

## Contributing

Contributions to this project are welcome! Please feel free to fork this repository, make changes, and submit pull requests.

## License

This project is open source and available under the MIT License.
```

