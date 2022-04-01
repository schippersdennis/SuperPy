from operator import le
import os
from helpers import get_last_id, timestamp_today
import csv
from rich import print


def remove_item(leftOvers):
    with open("bought.csv", "w", newline="") as write_file:
        fieldnames = [
            "id",
            "product_name",
            "buy_date",
            "buy_price",
            "expiration_date",
        ]
        csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames, delimiter=",")
        csv_writer.writeheader()
        for row in leftOvers:
            csv_writer.writerow(row)


def add_to_sell(data):
    file_exists = os.path.isfile("sell.csv")
    with open("sell.csv", "a", newline="") as csv_file:
        fieldnames = [
            "id",
            "product",
            "bought_id",
            "sell_date",
            "sell_price",
        ]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=",")
        if not file_exists:
            csv_writer.writeheader()
        csv_writer.writerow(data)
        print(
            f"[bold green]Succes!! Your {data['product']} sold for ${data['sell_price']}[/bold green]"
        )


def sell_items(args):
    file_exists = os.path.isfile("sell.csv")
    boughtExist = os.path.isfile("bought.csv")
    if boughtExist:
        with open("bought.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            leftOvers = []
            row_count = 0
            for row in csv_reader:
                row_count = row_count + 1
                if row.get("product_name") == args.product_name:
                    writeData = {
                        "id": get_last_id(file_exists, "sell"),
                        "product": args.product_name,
                        "bought_id": 0,
                        "sell_date": timestamp_today(),
                        "sell_price": args.price,
                    }
                    writeData["bought_id"] = row.get("id")
                    add_to_sell(writeData)
                else:
                    leftOvers.append(row)
            remove_item(leftOvers)

        if len(leftOvers) == row_count:
            print("[bold red]ERROR: Product not in stock.[/bold red]")

    else:
        print("[bold red]You need to buy products first[/bold red]")
