import os
from helpers import get_last_id, timestamp_today
import csv
from rich import print


def sell_items(args):
    file_exists = os.path.isfile("sell.csv")
    boughtExist = os.path.isfile("bought.csv")
    writeData = {
        "id": get_last_id(file_exists, "sell"),
        "product": args.product_name,
        "bought_id": 0,
        "sell_date": timestamp_today(),
        "sell_price": args.price,
    }
    if boughtExist:
        with open("bought.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row.get("product_name") == args.product_name:
                    writeData["bought_id"] = row.get("id")
                    with open("sell.csv", "a", newline="") as csv_file:
                        fieldnames = [
                            "id",
                            "product",
                            "bought_id",
                            "sell_date",
                            "sell_price",
                        ]
                        csv_writer = csv.DictWriter(
                            csv_file, fieldnames=fieldnames, delimiter=","
                        )
                        if not file_exists:
                            csv_writer.writeheader()
                        csv_writer.writerow(writeData)
                        print(
                            f"[bold green]Succes!! Your {args.product_name} sold for ${args.price}[/bold green]"
                        )

                else:
                    print("[bold red]ERROR: Product not in stock[/bold red]")

    else:
        print("[bold red]You need to buy products first[/bold red]")
