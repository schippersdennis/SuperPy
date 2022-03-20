import argparse
from datetime import datetime
import os
from helpers import advance_time
from buy_items import buy_items
from sell_items import sell_items
from report import reports_builder


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass


# Parsers
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# Advance time argument:
parser.add_argument("--advance-time", type=int, help="advance time by amount of days")

# Buy
buy_parser = subparsers.add_parser("buy", help="Registering product purchases")
buy_parser.add_argument(
    "--product-name",
    type=str,
    help="Enter the name of the product you would like to add here",
)
buy_parser.add_argument(
    "--price", type=float, help="Enter the price for which you want to buy the product"
)
buy_parser.add_argument(
    "--expiration-date",
    type=lambda s: datetime.strptime(s, "%Y-%m-%d"),
    default="yyyy-mm-dd",
    required=True,
    help="Enter expiration date of the product. (default format: %(default)s)",
)

# Sell Parser:
sell_parser = subparsers.add_parser("sell", help="register sold product")
sell_parser.add_argument(
    "--product-name", help="Enter the product name of the product you want to sell."
)
sell_parser.add_argument(
    "--price", type=float, help="Enter the price for which you are selling the product"
)

# Report Parsers:
report = subparsers.add_parser("report", help="Generate reports about transactions.")
report_subparsers = report.add_subparsers(dest="parser_report")

# -Sub_Parsers
inventory = report_subparsers.add_parser(
    "inventory", help="Reports involving involvement to inventory"
)
revenue = report_subparsers.add_parser(
    "revenue", help="Reports involving involvement to revenue"
)
profit = report_subparsers.add_parser(
    "profit", help="Reports involving involvement to profit"
)

# --Inventory
inventory.add_argument(
    "--now", action="store_true", help="View today's inventory report"
)
inventory.add_argument(
    "--yesterday", action="store_true", help="View yesterday's inventory report"
)

# --Revenue
revenue.add_argument(
    "--yesterday", action="store_true", help="View today's revenue report"
)
revenue.add_argument(
    "--today", action="store_true", help="View yesterday's revenue report"
)
revenue.add_argument(
    "--date", help="show revenue report from given date: insert date as: YYYY-MM"
)

# --Profit
profit.add_argument("--today", action="store_true", help="View today's profit report")
args = parser.parse_args()


if not os.path.isfile("advanced_time.txt"):
    advance_time(0)
if args.advance_time or args.advance_time == 0:
    advance_time(args.advance_time)
if args.command == "buy":
    buy_items(args)
if args.command == "sell":
    sell_items(args)
if args.command == "report":
    reports_builder(args)


if __name__ == "__main__":
    main()
