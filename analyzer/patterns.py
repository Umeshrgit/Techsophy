def detect_anomalies(data):
    anomalies = []

    for item in data:
        usage = item['usage']
        cost = item['cost']
        if usage == 0 or cost / usage > 1.5:
            anomalies.append(item)

    return anomalies
