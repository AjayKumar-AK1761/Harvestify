# AgriBot 🌱

A comprehensive agricultural assistance system that helps farmers and gardeners make informed decisions about crop management, disease detection, and fertilizer recommendations.

## Features 🚀

- **Crop Recommendation**: Get personalized crop recommendations based on soil and environmental parameters
- **Disease Detection**: Identify plant diseases through image recognition
- **Fertilizer Recommendation**: Receive custom fertilizer suggestions based on soil type and nutrient content
- **Weather Integration**: Real-time weather data integration for accurate recommendations
- **User Authentication**: Secure user accounts and personalized experience
- **Interactive UI**: User-friendly interface for easy navigation and data input

## Technology Stack 💻

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy
- **Machine Learning**: 
  - PyTorch (Plant Disease Detection)
  - Scikit-learn (Crop Recommendation)
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Flask-Login
- **API Integration**: OpenWeatherMap API

## Project Structure 📁

```
AgriBot/
├── app.py              # Main application file
├── m_service.py        # Microservice utilities
├── config.py           # Configuration settings
├── requirements.txt    # Project dependencies
├── models/            # ML model files
├── templates/         # HTML templates
├── static/           # Static assets (CSS, JS, images)
├── utils/            # Utility functions and helpers
├── chatbot_server/   # Chatbot implementation
└── Data/             # Dataset and data files
```

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AgriBot.git
cd AgriBot
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
- Create a `config.py` file with your OpenWeatherMap API key:
```python
weather_api_key = "your_api_key_here"
```

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the application:
```bash
python app.py
```

## Usage 📝

1. Register for a new account or login if you already have one
2. Navigate to different services:
   - Crop Recommendation: Input soil and environmental parameters
   - Disease Detection: Upload plant images for disease identification
   - Fertilizer Recommendation: Get customized fertilizer suggestions

## Machine Learning Models 🤖

The project uses multiple ML models:
- ResNet9 architecture for plant disease detection
- Random Forest for crop recommendation
- Custom model for chatbot crop recommendations

## API Integration 🌐

- OpenWeatherMap API for real-time weather data
- Custom endpoints for model predictions and recommendations

## Contributing 🤝

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 👏

- Plant disease dataset from PlantVillage
- Weather data from OpenWeatherMap
- Contributors and maintainers

## Contact 📧

For questions and support, please open an issue in the GitHub repository.

---
Made with ❤️ by AgriBot Team 