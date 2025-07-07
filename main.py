import matplotlib.pyplot as plt

from collector.usage_data import fetch_mock_data
from analyzer.patterns import detect_anomalies
from optimizer.optimizer import suggest_optimizations
from actions.recommender import display_recommendations, write_to_file

def plot_usage_cost(data):
    services = [item['service'] for item in data]
    usage = [item['usage'] for item in data]
    cost = [item['cost'] for item in data]

    x = range(len(services))
    bar_width = 0.4

    plt.bar([i - bar_width/2 for i in x], usage, width=bar_width, label="Usage", color='skyblue')
    plt.bar([i + bar_width/2 for i in x], cost, width=bar_width, label="Cost", color='salmon')

    plt.xticks(x, services)
    plt.ylabel("Amount")
    plt.title("Cloud Service Usage vs Cost")
    plt.legend()
    plt.tight_layout()
    plt.show()

def run():
    data = fetch_mock_data()
    anomalies = detect_anomalies(data)
    suggestions = suggest_optimizations(anomalies)

    display_recommendations(suggestions)
    write_to_file(suggestions)
    plot_usage_cost(data)

if __name__ == "__main__":
    run()
