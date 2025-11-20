import unittest
import joblib
import pandas as pd
import os

class TestSmartMush(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Load model once for all tests
        if os.path.exists('mushroom_ai_model.pkl'):
            cls.model = joblib.load('mushroom_ai_model.pkl')
        else:
            raise FileNotFoundError("Model file missing. Run train_model.py first.")

    def test_model_loading(self):
        """Test if model loads correctly"""
        self.assertIsNotNone(self.model)

    def test_optimal_condition(self):
        """Test a known optimal condition (20°C, 90% Humidity, 500 CO2)"""
        input_data = pd.DataFrame([[20, 90, 500]], columns=['Temperature', 'Humidity', 'CO2_Level'])
        prediction = self.model.predict(input_data)[0]
        self.assertEqual(prediction, 1, "Should predict Optimal (1)")

    def test_suboptimal_condition_hot(self):
        """Test a known bad condition (High Temp)"""
        input_data = pd.DataFrame([[35, 90, 500]], columns=['Temperature', 'Humidity', 'CO2_Level'])
        prediction = self.model.predict(input_data)[0]
        self.assertEqual(prediction, 0, "Should predict Suboptimal (0)")

    def test_suboptimal_condition_dry(self):
        """Test a known bad condition (Low Humidity)"""
        input_data = pd.DataFrame([[20, 40, 500]], columns=['Temperature', 'Humidity', 'CO2_Level'])
        prediction = self.model.predict(input_data)[0]
        self.assertEqual(prediction, 0, "Should predict Suboptimal (0)")

if __name__ == '__main__':
    unittest.main()