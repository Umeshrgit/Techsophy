import random

def fetch_mock_data():
    services = ["EC2", "RDS", "S3", "Lambda", "CloudFront"]
    data = []

    for service in services:
        usage = round(random.uniform(10, 100), 2)
        cost = round(random.uniform(usage * 0.5, usage * 2), 2)
        data.append({
            "service": service,
            "usage": usage,
            "cost": cost
        })

    return data
