# Disease Prediction through Blood Report Data

## Overview
This project utilizes **Machine Learning** to predict diseases based on blood report data. The model leverages an **ensemble learning approach** combining **Random Forest, Support Vector Machine (SVM), and Gradient Boosting** to improve accuracy and generalization.

## Features
- Predicts multiple diseases based on blood report parameters.
- Implements **ensemble learning** for improved accuracy.
- Preprocesses blood report data using **feature scaling and encoding**.
- Provides a **user-friendly interface** for inputting test data.

## Dataset
The dataset consists of blood report parameters with labeled disease categories. It includes:
- **Input Features:** Hemoglobin, WBC count, RBC count, Platelet count, etc.
- **Output Labels:** Disease classifications (e.g., Anemia, Diabetes, Liver Disease, etc.).

## Model Architecture
The model is trained using a combination of:
- **Random Forest** - for robustness and feature importance.
- **Support Vector Machine (SVM)** - for effective classification in high-dimensional space.
- **Gradient Boosting** - for reducing bias and improving model performance.

## Installation
### Prerequisites
Ensure you have the following dependencies installed:
```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

### Clone Repository
```bash
git clone https://github.com/PothanSai2004/Disease-Prediction-Blood-Report.git
cd Disease-Prediction-Blood-Report
```

## Usage
### Running the Model
1. **Prepare Dataset:** Ensure the dataset is properly formatted.
2. **Train the Model:** Run the following command:
   ```bash
   python train.py
   ```
3. **Make Predictions:** Use the trained model to predict diseases:
   ```bash
   python predict.py --input sample_report.csv
   ```

## Results & Performance
- Achieved **high classification accuracy** using ensemble learning.
- Applied **cross-validation** to ensure model reliability.
- Visualized feature importance for better interpretability.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License
This project is licensed under the **MIT License**.

## Contact
For queries, reach out via:
- **GitHub**: [PothanSai2004](https://github.com/PothanSai2004)
- **Email**: pothansaithummala@gmail.com
