# Rice Field Digital Twin

This project is an interactive 3D digital twin of a rice field using Dash + Python.
It integrates:
- Real-time weather API
- IoT sensor data (CSV or MQTT)
- Rice crop growth stage prediction (ML model)
- Satellite terrain data (DEM via rasterio)

## Setup
1. Copy `.env.example` to `.env` and add your OpenWeatherMap API key.
2. Run `pip install -r requirements.txt`
3. Run `python app.py` or deploy with Docker.
