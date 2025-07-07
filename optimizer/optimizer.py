def suggest_optimizations(anomalies):
    suggestions = []

    for item in anomalies:
        service = item["service"]
        usage = item["usage"]
        cost = item["cost"]

        if usage == 0:
            suggestions.append(f"🛑 {service}: No usage but cost exists — consider shutting it down.")
        elif cost / usage > 1.5:
            suggestions.append(f"⚠️ {service}: Cost is too high relative to usage — optimize or downgrade.")

    return suggestions
