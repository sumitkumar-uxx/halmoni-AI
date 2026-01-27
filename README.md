Halmoni AI: Your Personal Health & Lifestyle Companion

Project Overview

Halmoni AI is an intelligent health prediction system that uses machine learning to analyze your lifestyle habits and provide personalized insights about your health, longevity, hydration needs, social media addiction levels, and productivity potential.

Think of it as your digital health advisor that combines multiple predictive models into one easy-to-use application!

What It Can Do

1. Life Expectancy Predictor
- Estimates how long you might live based on your daily habits
- Considers factors like work hours, sleep, exercise, and occupation
- Gives you insights into how lifestyle choices impact longevity

2. Hydration Advisor
- Calculates your ideal daily water intake
- Takes into account your age, weight, activity level, and weather conditions
- Helps you stay optimally hydrated for better health

3. Social Media Addiction Analyzer
- Assesses your social media usage patterns
- Provides an addiction score based on your habits and demographics
- Helps you understand if your phone usage is becoming problematic

4. Productivity Optimizer
- Evaluates your morning routine effectiveness
- Suggests how to structure your mornings for maximum productivity
- Considers factors like wake-up time, meditation, and screen time

Technical Details

Models & Algorithms
- Primary Algorithm: XGBoost Regressor (Extreme Gradient Boosting)
- Preprocessing: Label Encoding for categorical variables
- Framework: Streamlit for interactive web interface
- Model Persistence: Joblib for saving and loading trained models

Data Processing Pipeline
1. Data Loading: CSV files with various health and lifestyle metrics
2. Feature Encoding: Converting categorical text data to numerical values
3. Train-Test Split: 80-20 split for model training and validation
4. Model Training: Individual XGBoost models for each prediction task
5. Model Saving: Serialized models for quick deployment

Project Structure

Halmoni_AI/
│
├── model_training.py          # Main training script
├── halmoni_app.py            # Streamlit web application
│
├── model.pkl                 # Life expectancy model
├── model_sec.pkl             # Water intake model
├── model_third.pkl           # Addiction score model
├── model_four.pkl            # Productivity model
│
├── Updated Quality of Life Data.csv
├── Daily_Water_Intake.csv
├── Students Social Media Addiction.csv
├── Morning_Routine_Productivity.csv
│
└── README.md                 # This file

How to Use

Prerequisites
pip install pandas scikit-learn xgboost joblib streamlit

Running the Application
1. First, train the models (if using new data):
python model_training.py

2. Launch the web app:
streamlit run halmoni_app.py

3. Interact with the models:
   - Navigate through different prediction sections
   - Input your personal data
   - Get instant predictions with explanations

Key Features

Interactive Interface
- Clean, sectioned layout for each prediction type
- Real-time prediction updates
- Loading animations for better user experience

Data-Driven Insights
- Each model trained on relevant datasets
- Continuous learning potential with new data
- Scientific approach to health predictions

Performance Optimized
- Pre-trained models for instant predictions
- Efficient data preprocessing
- Scalable architecture for adding new features

Who Is This For?

- Health-conscious individuals wanting data-driven lifestyle insights
- Students concerned about study-life balance and phone addiction
- Professionals looking to optimize productivity
- Researchers interested in lifestyle-health correlations
- Anyone curious about how daily habits affect long-term wellbeing

Important Notes

Disclaimer
These models provide predictive estimates based on statistical patterns, not medical advice. Always consult healthcare professionals for serious health decisions. The predictions are educational tools, not definitive diagnoses.

Data Privacy
- All calculations happen locally in your browser
- No personal data is stored or transmitted
- You maintain complete control over your information

Future Enhancements

Planned improvements include:
- More lifestyle factors integration
- Personalized recommendations based on predictions
- Historical tracking of your scores over time
- Mobile app version
- Multi-language support
- Integration with wearable device data

Contributing

Found a bug? Have a feature request? Feel free to:
1. Open an issue detailing your suggestion
2. Fork the repository and submit a pull request
3. Share your own health datasets (anonymized)

Learn More

The models are based on principles from:
- Preventive medicine research
- Behavioral psychology
- Time management studies
- Digital wellness literature

Remember: Small daily habits create big lifetime impacts. Use these insights to make informed choices, but always listen to your body and consult professionals for personalized advice.

Stay healthy, stay curious!

Project by Sumit | Halmoni AI - Making health insights accessible to everyone