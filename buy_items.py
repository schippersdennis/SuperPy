import os
import csv
from helpers import get_last_id, timestamp_today
from rich import print


def buy_items(args):
    file_exists = os.path.isfile("bought.csv")
    writeData = {
        "id": get_last_id(file_exists, "bought"),
        "product_name": args.product_name,
        "buy_date": timestamp_today(),
        "buy_price": args.price,
        "expiration_date": args.expiration_date,
    }
    with open("bought.csv", "a", newline="") as csv_file:
        fieldnames = ["id", "product_name", "buy_date", "buy_price", "expiration_date"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=",")
        if not file_exists:
            csv_writer.writeheader()
        csv_writer.writerow(writeData)
        print("[bold green]successfully added[/bold green]")
