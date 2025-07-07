def display_recommendations(suggestions):
    print("\n🔍 COST OPTIMIZATION RECOMMENDATIONS:")
    if not suggestions:
        print("✅ No major issues detected. You're doing great!")
    for suggestion in suggestions:
        print("-", suggestion)

def write_to_file(suggestions, filename="report.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Cloud Cost Optimization Report\n")
        f.write("===============================\n")
        if not suggestions:
            f.write("No cost issues found.\n")
        else:
            for suggestion in suggestions:
                f.write(f"- {suggestion}\n")
