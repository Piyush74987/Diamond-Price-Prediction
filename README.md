
# Diamond Price Prediction

This repository contains a project that predicts the price of diamonds using machine learning techniques. The project follows a complete data science workflow, including data preprocessing, exploratory data analysis (EDA), model building, and performance evaluation.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Dataset Information](#dataset-information)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)


## Introduction

The Diamond Price Prediction project aims to build a reliable model that estimates the price of a diamond based on its features. The model helps jewelers, buyers, and sellers to evaluate diamond prices more effectively.

## Project Structure

```
Diamond-Price-Prediction/
├── data/                   # Contains the dataset files
├── notebooks/              # Jupyter notebooks for EDA and model development
├── src/                    # Source code for data processing and model training
├── models/                 # Saved machine learning models
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── app.py                  # Web application for user interaction
```

## Technologies Used

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Framework**: Flask (for web application)

## Dataset Information

The dataset contains the following features:

- **carat**: Weight of the diamond
- **cut**: Quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- **color**: Diamond color, from J (worst) to D (best)
- **clarity**: A measurement of how clear the diamond is (I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF)
- **depth**: Total depth percentage (z / mean(x, y))
- **table**: Width of the top of the diamond relative to the widest point
- **price**: Price of the diamond in USD
- **x, y, z**: Dimensions of the diamond in mm

The dataset is available on [Kaggle](https://www.kaggle.com/shivam2503/diamonds).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Piyush74987/Diamond-Price-Prediction.git
   cd Diamond-Price-Prediction
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the web application:
   ```bash
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000`.
3. Enter the diamond's attributes to predict its price.

## Results

The model achieves a high level of accuracy, demonstrating reliable predictions for diamond prices. The detailed performance metrics and analysis are available in the project notebooks.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.



![Screenshot (1)](https://github.com/user-attachments/assets/4c2ce3d8-727e-4c46-b6c9-1179f831c59b)

![Screenshot (3)](https://github.com/user-attachments/assets/004bd781-2f08-4e7a-9485-346dc44e1c14)
