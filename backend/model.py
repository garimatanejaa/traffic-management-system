import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

class TrafficPredictor:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.train()

    def train(self):
        # Load and prepare the dataset
        dataset_path = os.path.join(os.path.dirname(__file__), 'Dataset.csv')
        dataset = pd.read_csv(dataset_path)
        
        # Feature engineering
        dataset['IsHoliday'] = dataset['CodedDay'].apply(lambda x: 1 if x in [5, 6] else 0)
        dataset['Traffic'] = dataset['Traffic'].apply(lambda x: 1 if x > 300 else 0)  # 1 for Congested, 0 for Not Congested

        X = dataset[['CodedDay', 'Weather', 'IsHoliday']].values
        y = dataset['Traffic'].values

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Scale the features
        self.scaler = StandardScaler()
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)

        # Train the model
        self.model = RandomForestClassifier(n_estimators=300, random_state=42)
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")

    def predict(self, coded_day, weather, is_holiday):
        user_data = np.array([[coded_day, weather, is_holiday]])
        user_data_scaled = self.scaler.transform(user_data)
        prediction = self.model.predict(user_data_scaled)
        return "Congested" if prediction[0] == 1 else "Not Congested"