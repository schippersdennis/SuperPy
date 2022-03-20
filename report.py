import os
import csv
from rich import print
from helpers import getTime, generateCsvReport
from asyncio.windows_events import NULL
from get_tables import buildingTables
from datetime import date, datetime, timedelta
import datetime
from get_chart import plot_inventory


def reports_builder(args):
    sellExist = os.path.isfile("sell.csv")
    boughtExist = os.path.isfile("bought.csv")

    setDate = getTime(args)
    day = setDate["name"]
    newDate = setDate["date"]

    collection = {
        "items": [],
        "bought_total": 0,
        "sell_total": 0,
        "revenue_month": 0,
    }

    # BOUGHT
    if boughtExist:
        with open("bought.csv", encoding="utf8") as bought:
            bought = csv.DictReader(bought)
            for b in bought:
                date_b = datetime.datetime.strptime(
                    b.get("buy_date"), "%Y-%m-%d %H:%M:%S.%f"
                ).date()
                if date_b == newDate:
                    collection["items"].append(b)
                    collection["bought_total"] += float(b.get("buy_price"))
    else:
        print("[bold red]You need to buy products first[/bold red]")

    # SELL
    if sellExist:
        with open("sell.csv", encoding="utf8") as sold:
            sold = csv.DictReader(sold)
            for s in sold:
                date_s = datetime.datetime.strptime(
                    s.get("sell_date"), "%Y-%m-%d %H:%M:%S.%f"
                ).date()

                # Get Revenue(month of year) if --date
                if (
                    args.parser_report == "revenue"
                    and args.date
                    and (date_s.month == newDate.month and date_s.year == newDate.year)
                ):
                    collection["revenue_month"] += float(s.get("sell_price"))

                if date_s == setDate["date"]:
                    collection["sell_total"] += float(s.get("sell_price"))
    elif not args.parser_report == "inventory":
        print("[bold red]You need to sell products first[/bold red]")

    # inventory
    if args.parser_report == "inventory" and boughtExist:
        # 1. generate CLI schema
        buildingTables(collection["items"])
        # 2. Export inventory to CSV
        generateCsvReport(collection["items"])
        # 3. Render a Mathplot visual.
        plot_inventory(collection["items"])

    if boughtExist and sellExist:
        # Revenue
        if args.parser_report == "revenue":
            price = (
                collection["revenue_month"] if args.date else collection["sell_total"]
            )
            return print(f"[bold blue]{day} Revenue: ${price}[/bold blue]")
        # Profit
        if args.parser_report == "profit":
            sum = collection["sell_total"] - collection["bought_total"]
            return print(f"[bold blue]{day} Profit: ${sum}[/bold blue]")
