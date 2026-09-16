from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    sales = pd.DataFrame(
        {
            "sale_id": range(1, 11),
            "product": [
                "Notebook",
                "Pen Set",
                "Desk Lamp",
                "Backpack",
                "Water Bottle",
                "Headphones",
                "Keyboard",
                "Mouse",
                "Monitor Stand",
                "Webcam",
            ],
            "sale_amount": [12.50, 8.75, 34.99, 45.00, 18.25, 59.99, 42.50, 24.99, 31.75, 49.95],
        }
    )

    average_sale = sales["sale_amount"].mean()
    print(f"Average sale: ${average_sale:.2f}")

    chart_path = Path(__file__).with_name("demo_sales_bar_chart.png")
    plt.figure(figsize=(10, 5))
    plt.bar(sales["product"], sales["sale_amount"], color="steelblue")
    plt.title("Demo Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sale Amount ($)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(chart_path, dpi=150)
    plt.close()
    print(f"Bar chart saved to: {chart_path}")


if __name__ == "__main__":
    main()