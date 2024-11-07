# Intelligent Intrusion Detection for CPS 
This repository provides a Jupyter notebook designed for analyzing cyber-attack detection on critical infrastructure systems, specifically water treatment plants. Using datasets with records of both normal operations and attack scenarios, this notebook applies machine learning techniques to detect and classify various cyber-attacks.

## Table of Contents
Project Overview
Data Requirements
Notebook Outline
Dependencies
Usage
Results and Model Performance
License

## Project Overview
This notebook focuses on cybersecurity for critical infrastructure, specifically monitoring and detecting cyber-attacks on water treatment facilities. The analysis uses data from SWaT (Secure Water Treatment), a real-world testbed, to classify operation states and detect abnormal activities associated with various cyber-attack types.

## Goals
- To preprocess, clean, and transform SWaT dataset records.
- To train machine learning models that can distinguish between normal and attack states.
- To evaluate model performance, selecting the most suitable classifier for real-time detection.
## Data Requirements
The notebook expects the following datasets:

- **Normal Data:** Contains records from SWaT's normal operations, indicating regular readings from sensors and actuators.
- ***Attack Data:** Contains records from SWaT under simulated attack conditions, representing six distinct types of attacks.

Each dataset should include features such as sensor readings (e.g., water levels, chemical properties) and actuator states (e.g., flow rates, pump statuses).

## Notebook Outline
1. **Data Loading and Preprocessing**
- Loads both normal and attack data into Pandas DataFrames.
- Cleans data by removing any trailing or leading whitespace from column names and string values.
- Deduplicates the datasets to ensure unique records.
2. **Data Concatenation and Encoding**
- Combines normal and attack datasets into a single DataFrame.
- Encodes categorical features into numeric formats:
-Labels are encoded to represent different classes (normal and six attack types).
- Boolean and categorical columns are mapped to numeric values or one-hot encoded where applicable.
3. **Data Splitting and Scaling**
- Splits the dataset into training and testing subsets (75% training, 25% testing).
-Standardizes numeric features to have a mean of zero and unit variance, improving model performance and convergence.
4. **Model Selection and Training**
- A set of machine learning models are available, including:
    - Random Forest Classifier
    - Support Vector Classifier (Linear Kernel)
    - Decision Tree Classifier
    - Logistic Regression
- Selects the desired model (default: Random Forest) and trains it on the training data.
5. **Model Evaluation**
- Evaluates the model’s performance on the test set.
- Outputs include:
    - Confusion matrix to visualize classification performance.
    - Accuracy scores for each model tested.
    - Dependencies
- Ensure you have the dependencies existing in req.txt installed before running the notebook, by running the following command:

```bash
pip install -r req.txt
```
## Usage
- **Load the Notebook:** Open the cyberphy.ipynb notebook in Jupyter Notebook or JupyterLab.
- **Dataset Paths:** Update file paths in the notebook if needed to point to your data files.
- **Run Cells Sequentially:** Execute each cell from top to bottom to preprocess data, train the models, and view evaluation metrics.
## Configuring Model and Parameters
To change the model or parameters:

- Modify the desired_model variable to any of the supported models ('linear_svm', 'tree', 'logistic', or 'forest').
- Adjust C (regularization parameter for SVM and Logistic Regression) if applicable.
## Results and Model Performance
The notebook includes a variety of metrics and outputs:

- **Confusion Matrix:** Visualizes the model’s predictions against actual labels.
- **Accuracy:** Indicates the model’s accuracy for each test case.
- **Detailed Model Comparisons:** Optional if additional models are incorporated.

Tree-based classifiers (such as Random Forest) are preferred for their high accuracy and performance on imbalanced datasets, making them suitable for detecting rare attack instances.
