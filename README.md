# README.md

# Mood Detector Web Application

This project is a web application that integrates mood detection functionality using Python. It allows users to input sentences and receive predictions about the mood conveyed in those sentences.

## Project Structure

- `src/static/css/styles.css`: Contains the CSS styles for the web application.
- `src/static/js/main.js`: Includes JavaScript code for handling user interactions.
- `src/templates/base.html`: Base HTML template with common elements.
- `src/templates/index.html`: Main HTML page with a form for mood detection.
- `src/app.py`: Main entry point for the web application.
- `src/mood_detector.py`: Contains the mood detection logic.
- `src/train.csv`: Training data for the mood detection model.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python src/app.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

Enter a sentence in the input field and click the submit button to detect the mood. The predicted mood will be displayed on the webpage.

## License

This project is licensed under the MIT License.