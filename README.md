🏠 House Price Predictor

A clean, ML-powered web app that predicts house prices in Bengaluru based on area, location, and number of BHKs. Built with Python, Streamlit, and scikit-learn.



📌 Overview

This project showcases how a Linear Regression model can predict housing prices using basic property features. The model is trained on real-world Bengaluru housing data and deployed with a user-friendly interface using Streamlit.



💡 Features

- 📊 Predicts price of a house based on Area, BHK, and Location
- 🧠 Trained using Linear Regression from scikit-learn
- 🧹 Includes preprocessing: BHK extraction, sqft conversion, one-hot encoding
- ⚙️ Built with Streamlit for interactive UI
- 📁 Organized, modular, and GitHub-ready structure



📁 Project Structure

house-price-predictor/
├── app.py                  # Streamlit web application
├── model_train.py          # Script to train and save the model
├── house_price_model.pkl   # Trained Linear Regression model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── data/
│   └── Bengaluru_House_Data.csv # Original dataset
└── images/
    └── app_screenshot.png  # UI screenshot



🚀 How to Run Locally

🛠️ Prerequisites:
- Python 3.7+
- pip



🔧 Setup Instructions:

# Clone the repository
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py



📈 Dataset

Source: Kaggle - Bengaluru House Price Data  
URL: https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

Features Used: total_sqft, bhk, location  
Target Predicted: price (in Lakhs)



📊 Sample Output

Input:
- Area: 1200 sqft
- BHK: 3
- Location: Whitefield

Output:
💰 Predicted Price: ₹ 89.73 Lakhs

![App Screenshot](https://https://github.com/Vikasni-S-06/house-price-predictor/blob/main/images/house%20predictor%20page.png)





🌐 Live Demo

🔗 [Click here to try the live app](https://vikasni-06-house-price-predictor-push.streamlit.app/)



🧠 Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Joblib  
- Streamlit  



🙌 Acknowledgements

- Streamlit for simple ML app deployment  
- Kaggle for the housing dataset  
