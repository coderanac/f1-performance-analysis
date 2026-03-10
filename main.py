import fastf1 as f1

f1.Cache.enable_cache('cache')

session = f1.get_session(2026, 'Australia', 'R')

session.load()

print(session.results)
print(session.laps)
print(session.drivers)