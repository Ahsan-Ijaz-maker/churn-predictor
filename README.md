1 . Customer Churn Predictor

A Machine Learning project that predicts whether a telecom customer is likely to churn (leave the service) based on their billing and usage behavior.

2 .  Problem Statement

Customer churn is a major challenge for subscription-based businesses such as telecom companies. Identifying customers who are likely to leave allows companies to take proactive retention measures, reducing revenue loss.

3.  Technologies Used
- Python
- Pandas
- Scikit-learn (Logistic Regression)

4. Dataset Features
- Monthly Bill: The customer's monthly billing amount
- Tenure (Months): How long the customer has been with the service
- Support Calls: Number of customer support calls made
- Will Leave: Target variable (1 = Churn, 0 = Stay)

5.  How It Works
1. The model is trained on historical customer data to identify patterns associated with churn
2. Key indicators such as high support call frequency and short tenure are strongly associated with churn
3. The model takes a new customer's data as input and predicts whether they are likely to churn

6.  Model Evaluation
The dataset was split into training and testing sets (80/20) to evaluate model performance using accuracy scoring.

7.  Features
- Logistic Regression for binary classification
- Train/Test split for unbiased model evaluation
- Real-time prediction system for new customer data

8.  Future Improvements
- Incorporate additional features such as contract type, payment method, and service usage patterns
- Use a larger, real-world dataset for improved generalization
- Compare performance against other classification algorithms (Decision Tree, Random Forest)
- Deploy the model as a web application for business use
