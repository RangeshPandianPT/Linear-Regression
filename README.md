### 📄 README.md

# 🏡 Housing Price Prediction using Linear Regression

This project demonstrates the implementation and understanding of **Simple and Multiple Linear Regression** using the `Housing.csv` dataset. We use libraries like `Scikit-learn`, `Pandas`, and `Matplotlib` to analyze and predict housing prices based on various features.

---

## 📁 Project Structure



linear\_regression\_project/
│
├── linear\_regression\_model.py              # Python script for training and evaluation
├── linear\_regression\_model.ipynb           # Jupyter notebook version
├── Housing\_modified.csv                    # Preprocessed dataset with numerical features
├── Housing\_sample.csv                      # Random sample (10 rows) from the dataset
├── regression\_plot.png                     # Scatter plot: Area vs Actual vs Predicted price
├── top\_features\_barplot.png                # Bar chart of top 10 most influential features

````

---

## 📊 Dataset Information

Original dataset contains features such as:
- `price` (Target variable)
- `area`, `bedrooms`, `bathrooms`, `stories`, `parking`
- Categorical: `mainroad`, `guestroom`, `basement`, `airconditioning`, `hotwaterheating`, `furnishingstatus`, `prefarea`

The categorical features were one-hot encoded and saved in `Housing_modified.csv`.

---

## 🚀 How to Run

### 🐍 Using Python script:
```bash
python linear_regression_model.py
````

### 📒 Or open the notebook:

```bash
jupyter notebook linear_regression_model.ipynb
```

---

## 📈 Model Evaluation

* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**
* **R² Score**

---

## 📷 Visualizations

![Image](https://github.com/user-attachments/assets/afc3f81b-711d-4f45-be4b-a7acd8cd9a3a)

![Image](https://github.com/user-attachments/assets/8b1c072b-9678-46e6-a222-1fbd4beaec5e)

---

## 🧰 Tools Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Jupyter Notebook

---

## 🙌 Author

Created by RANGESHPANDIAN PT


---

