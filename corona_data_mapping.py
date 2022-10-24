def map_corona_data(data):
    active = data[-1]["Cases"] - data[-14]["Cases"]
    active_seven_days_ago = data[-8]["Cases"] - data[-21]["Cases"]
    last_seven_days = data[-1]["Cases"] - data[-8]["Cases"]
    return  {
        "cases": data[-1]["Cases"],
        "active": active,
        "lockdown": last_seven_days > 10000,
        "trend": "UP" if active_seven_days_ago < active else "DOWN"
    }