## Superpy
#### **Assignment:** SuperPy
Report Please include a short, 300-word report that highlights three technical elements of your implementation

#1
I started on the main page to define all the parsers. To keep an overview I have created several files.
When we run the program for the first time, a check is performed whether advanced_time.txt already exists.
If this is not the case yet, we will run the program for the first time and we want to store this current date and time in a text file.
We store this in a txt file and will always form the basis for timestamps in the project.
We can only advance this time or bring it back to today by entering 0. I consciously chose to do it this way.
```
# Advance Date
def advance_time(days):
    dateToday = datetime.now().date()
    updatedDate = dateToday + timedelta(days=days)
    with open("advanced_time.txt", mode="w") as file:
        file.write(str(updatedDate))
    print(f"[bold green]successfully changed the date to[/bold green] {updatedDate}")
```

#2
When we buy or sell items, the item is placed in a CSV file.
To provide these items with a Unique ID, I wrote functionality that the item will always have a unique ID.
```
# Create ID  or auto increment on new entery's
def get_last_id(file_exists, file):
    if file_exists:
        with open(f"{file}.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                pass
            return int(row.get("id")) + 1
    return 1
```

To display the inventory I used a library Rich.
It looks nice and clear. Maybe I will expand this project in the future and also apply a display on the sell.csv for a nice overview.

┌────┬──────────────┬────────────────────────────┬───────────┬─────────────────────┐
│ id │ product_name │ buy_date                   │ buy_price │ expiration_date     │
├────┼──────────────┼────────────────────────────┼───────────┼─────────────────────┤
│ 1  │ orange       │ 2022-03-11 20:50:00.597116 │ 0.8       │ 2020-01-01 00:00:00 │
└────┴──────────────┴────────────────────────────┴───────────┴─────────────────────┘


