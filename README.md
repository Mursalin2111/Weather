# Django Weather App 🌤️

A dynamic, web-based weather application built with Python and Django. Enter the name of any city to get its current weather, temperature, and a dynamic background image matching the city!

## Features 🚀
- **Real-time Weather:** Fetches live weather conditions (temperature, description, weather icon) using the [OpenWeatherMap API](https://openweathermap.org/).
- **Dynamic Backgrounds:** Automatically fetches background images related to the searched city using an image API (LoremFlickr/Google Custom Search).
- **Graceful Error Handling:** If a city isn't found, it drops a clean error message without crashing.
- **Responsive Design:** Serves cleanly on desktop and mobile.

## Tech Stack 🛠️
- **Backend:** Python 3, Django
- **Frontend:** HTML, CSS
- **APIs Used:** OpenWeatherMap, External Image APIs (LoremFlickr)
- **Deployment Ready:** Configured for deployment on platforms like *PythonAnywhere*.

## Local Setup Instructions 💻

Follow these steps to get the project up and running on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mursalin2111/Weather.git
   cd Weather/Weather-App-
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   *The app will be available at `http://127.0.0.1:8000/`*

## Deployment 🌐
This project is configured with `requirements.txt` and static files settings (`STATIC_ROOT`) making it ready for deployment on free hosts like **PythonAnywhere**. 

1. Push your code to GitHub.
2. Clone it into your PythonAnywhere bash terminal.
3. Install `requirements.txt` in a virtual environment.
4. Run `python manage.py collectstatic`.
5. Point the PythonAnywhere WSGI configuration block to the Django settings file.

---
*Created by [Mursalin2111](https://github.com/Mursalin2111)*