<h1>💎 GemWorth: Diamond Price Prediction System</h1>
<p>This project predicts the price of diamonds using machine learning techniques. It follows a complete data science pipeline: data preprocessing, EDA, model training, and deployment using Flask.</p>
<h2>📁 Project Structure</h2>
<pre>
Diamond-Price-Prediction/
├── data/                   # Contains dataset files
├── notebooks/              # Jupyter notebooks for EDA and modeling
├── src/                    # Source code for preprocessing and modeling
├── models/                 # Saved trained ML models
├── requirements.txt        # Python package requirements
├── README.md               # Documentation
└── app.py                  # Flask web application
    </pre>
    <h2>🛠️ Technologies Used</h2>
    <ul>
        <li><strong>Programming Language:</strong> Python</li>
        <li><strong>Libraries:</strong> Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn</li>
        <li><strong>Web Framework:</strong> Flask</li>
    </ul>
    <h2>📊 Dataset Information</h2>
    <p>The dataset includes the following features:</p>
    <ul>
        <li><strong>carat:</strong> Weight of the diamond</li>
        <li><strong>cut:</strong> Quality (Fair, Good, Very Good, Premium, Ideal)</li>
        <li><strong>color:</strong> J (worst) to D (best)</li>
        <li><strong>clarity:</strong> I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF</li>
        <li><strong>depth:</strong> Total depth % = z / mean(x, y)</li>
        <li><strong>table:</strong> Width of top relative to widest point</li>
        <li><strong>price:</strong> Diamond price (USD)</li>
        <li><strong>x, y, z:</strong> Dimensions in mm</li>
    </ul>
    <h2>🚀 Installation</h2>
    <pre><code>git clone https://github.com/yourusername/GemWorth-Diamond-Price-Prediction.git
cd Diamond-Price-Prediction
pip install -r requirements.txt</code></pre>

   <h2>🖥️ Usage</h2>
    <ol>
        <li>Run the app:</li>
        <pre><code>python app.py</code></pre>
        <li>Visit <code>http://localhost:5000</code> in your browser.</li>
        <li>Fill out the form with diamond features and click <strong>Predict</strong>.</li>
    </ol>
    <h2>📈 Results</h2>
    <p>The model provides an accurate prediction of the diamond price based on user inputs. Evaluation metrics like RMSE and R<sup>2</sup> score can be found in the notebook.</p>
    <h2>🖼️ Screenshot</h2>
    <p> <img width="1920" height="1080" alt="Screenshot (49)" src="https://github.com/user-attachments/assets/59751ae1-0dab-478e-a18f-b06fdf0ee3db" />

    <img width="1920" height="1080" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/015e8fec-11d3-488a-8406-144518eec48d" />

   <img width="1920" height="1080" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/09bfbd48-a548-4d60-9c2c-5ed868220e58" />
    </p>
    <h2>🤝 Contributing</h2>
    <p>Feel free to fork the repo and create pull requests for improvements!</p
    <h2>📄 License</h2>
    <p>This project is licensed under the MIT License.</p>

</body>
</html>

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
- [Screenshot](#screenshot)
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

## screenshoot

<img width="1920" height="1080" alt="Screenshot (49)" src="https://github.com/user-attachments/assets/59751ae1-0dab-478e-a18f-b06fdf0ee3db" />

<img width="1920" height="1080" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/015e8fec-11d3-488a-8406-144518eec48d" />

<img width="1920" height="1080" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/09bfbd48-a548-4d60-9c2c-5ed868220e58" />
.
## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request

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


