from asyncio.windows_events import NULL
from datetime import datetime, timedelta
from rich import print
import calendar
import csv


# Advance Date
def advance_time(days):
    dateToday = datetime.now().date()
    updatedDate = dateToday + timedelta(days=days)
    with open("advanced_time.txt", mode="w") as file:
        file.write(str(updatedDate))
    print(f"[bold green]successfully changed the date to[/bold green] {updatedDate}")


# Create ID  or auto increment on new entery's
def get_last_id(file_exists, file):
    if file_exists:
        with open(f"{file}.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                pass
            return int(row.get("id")) + 1
    return 1


# Get date from String.
def timestamp_today():
    with open("advanced_time.txt", mode="r") as date:
        for line in date.readlines():
            return datetime.combine(
                datetime.strptime(line, "%Y-%m-%d").date(),
                datetime.now().time(),
            )


def getTime(args):
    dateTimeObj = {"name": NULL, "date": NULL}
    # Set Date Today/Now
    if (args.parser_report == "inventory" and args.now) or (
        (args.parser_report == "revenue" or args.parser_report == "profit")
        and args.today
    ):
        dateTimeObj["name"] = "Today's"
        dateTimeObj["date"] = timestamp_today().date()

    # Set Date Yesterday
    elif args.yesterday:
        dateTimeObj["name"] = "Yesterdays's"
        dateTimeObj["date"] = (timestamp_today() - timedelta(days=1)).date()

    # Set Date Month/Year
    elif args.parser_report == "revenue" and args.date:
        monthName = calendar.month_name[
            datetime.strptime((args.date + "-01"), "%Y-%m-%d").date().month
        ]
        year = datetime.strptime((args.date + "-01"), "%Y-%m-%d").date().year
        print()
        dateTimeObj["name"] = f"{monthName} {year}"
        dateTimeObj["date"] = datetime.strptime((args.date + "-01"), "%Y-%m-%d").date()

    return dateTimeObj
