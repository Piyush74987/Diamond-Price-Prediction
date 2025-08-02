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
    <p> 
<img width="1920" height="955" alt="Screenshot (49)" src="https://github.com/user-attachments/assets/a0a41ca3-37b2-4e60-9fb2-fa6204b7c692" />

<img width="1920" height="955" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/02cf1586-18e1-4d6a-b082-5788d6fe2007" />

<img width="1920" height="948" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/f51bd6c0-1a44-415a-b517-14f49daa7d8e" />
    </p>
    <h2>🤝 Contributing</h2>
    <p>Feel free to fork the repo and create pull requests for improvements!</p
    <h2>📄 License</h2>
    <p>This project is licensed under the MIT License.</p>


