# Credit Scoring Model
### Overview
This project implements a Credit Scoring Model for Bati Bank, in collaboration with an eCommerce partner, for a Buy-Now-Pay-Later (BNPL) service. The model classifies users into high-risk or low-risk groups based on their likelihood of default, leveraging customer transaction patterns and other behavioral features.

### The primary objectives of the model are:
To predict the probability of loan defaults.
To recommend optimal loan amounts and durations based on user risk.
To support the bank in making informed credit decisions and mitigating risk.
### Business Problem
With the growing adoption of BNPL services, it's essential for financial institutions to identify potential defaulters early. A robust credit scoring system enables better risk management and sustainable business growth.

### Key Objectives:
Classify users into high-risk or low-risk categories.
Predict the likelihood of default based on historical transaction patterns.
Recommend the appropriate loan amount and duration for each customer.
### Data
The dataset contains over 95,000 transactions and features related to customer transactions, including:

Numerical Features: Amount, Value, PricingStrategy, FraudResult.
Categorical Features: Transaction and customer-specific identifiers like TransactionId, CustomerId, ProductId, etc.
### Key statistics:
Amount: Avg ~6,700 (high variability, with significant negative outliers).
Value: Avg ~9,900 (relatively stable).
Fraud Result: Fraud rate is low at 0.2%.
### Model Development
### Preprocessing & Feature Engineering
## Missing Data Handling: 
Imputation and removal for incomplete rows.
### Feature Engineering: 
Aggregated customer transaction data (e.g., total transaction amount, average transaction value).
### Normalization & Standardization: 
Scaling numerical features for consistency.
### RFMS Analysis: 
Used Recency, Frequency, Monetary, and Seasonality indicators for better user segmentation and default risk proxy estimation.
### Weight of Evidence (WoE) Binning: 
Applied to recode features for better interpretability in predictive modeling.
### Models Implemented
### Logistic Regression: Simple, interpretable model.
### Random Forest Classifier: 
Ensemble method, offering higher accuracy and recall.
### Hyperparameter Tuning
Performed Random Search for optimal parameters in the Random Forest model.

### Usage
#### Requirements
Python 3.8+
#### Libraries:
pandas<br>
numpy<br>
scikit-learn<br>
matplotlib<br>

You can install the required libraries by running<br>
Copy code<br>
   pip install -r requirements.txt

### Insights & Recommendations
Random Forest outperformed Logistic Regression in recall and ROC-AUC, making it the preferred model for this task.<br>
The RFMS analysis combined with WoE binning provided useful customer segmentation for understanding default behavior.<br>
Recommendation: Deploy the Random Forest model to classify potential default users. Continuously update the model with new data for better accuracy.
### Conclusion
This Credit Scoring Model provides a reliable method to predict default risk for Bati Bank's BNPL services, enabling informed credit decisions and enhancing customer segmentation. By leveraging transaction patterns and behavioral insights, Bati Bank can now offer more personalized loan recommendations while minimizing financial risks.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
