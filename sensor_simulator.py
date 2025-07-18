
import csv
import random
import time

field_sensors = ["temp", "humidity", "soil_moisture", "ph"]

def generate_sensor_row():
    return {
        "temp": round(random.uniform(25, 38), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "soil_moisture": round(random.uniform(20, 60), 2),
        "ph": round(random.uniform(5.5, 7.5), 2)
    }

with open("sensor_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=field_sensors)
    writer.writeheader()
    while True:
        row = generate_sensor_row()
        writer.writerow(row)
        print("Wrote:", row)
        time.sleep(5)
