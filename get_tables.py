from rich.console import Console
from rich.table import Table
from rich import print

console = Console()


def buildingTables(data):
    table = Table(show_header=True, header_style="bold magenta")
    if len(data) > 0:
        for header in data[0].keys():
            table.add_column(header)

        for row in data:
            table.add_row(
                row.get("id"),
                row.get("product_name"),
                row.get("buy_date"),
                row.get("buy_price"),
                row.get("expiration_date"),
            )

        return console.print(table)
    else:
        print("[bold red]No items found on this date[/bold red]")
