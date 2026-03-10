import fastf1 as f1
import matplotlib.pyplot as plt

f1.Cache.enable_cache("cache")

session = f1.get_session(2026, "Australia", "R")
session.load()

laps = session.laps

leclerc_fastest = laps.pick_drivers("LEC").pick_fastest()
verstappen_fastest = laps.pick_drivers("VER").pick_fastest()

leclerc_telemetry = leclerc_fastest.get_telemetry()
verstappen_telemetry = verstappen_fastest.get_telemetry()

print("\n=== Telemetry Leclerc ===")
print(leclerc_telemetry[["Distance", "Speed", "Throttle", "Brake", "RPM", "nGear"]].head().to_string())

print("\n=== Telemetry Verstappen ===")
print(verstappen_telemetry[["Distance", "Speed", "Throttle", "Brake", "RPM", "nGear"]].head().to_string())

plt.figure()

plt.plot(leclerc_telemetry["Distance"], leclerc_telemetry["Speed"], label="Leclerc")
plt.plot(verstappen_telemetry["Distance"], verstappen_telemetry["Speed"], label="Verstappen")

plt.xlabel("Distance on track")
plt.ylabel("Speed (km/h)")
plt.title("Speed/distance comparison")
plt.legend()

plt.show()