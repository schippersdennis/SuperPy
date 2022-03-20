from rich.console import Console
from rich.table import Table
from rich import print

console = Console()


def buildingTables(data):
    count_list = []
    table = Table(show_header=True, header_style="bold magenta")
    count_table = Table(show_header=True, header_style="bold magenta")

    if len(data) > 0:
        for header in data[0].keys():
            table.add_column(header)

        for row in data:
            flat_values = [value for elem in count_list for value in elem.values()]
            if row.get("product_name") in flat_values:
                for dict in count_list:
                    if dict["product_name"] == row.get("product_name"):
                        dict.update(
                            {
                                "product_name": row.get("product_name"),
                                "items_in_stock": dict["items_in_stock"] + 1,
                            }
                        )
            else:
                count_list.append(
                    {"product_name": row.get("product_name"), "items_in_stock": 1}
                )

            table.add_row(
                row.get("id"),
                row.get("product_name"),
                row.get("buy_date"),
                row.get("buy_price"),
                row.get("expiration_date"),
            )

        console.print(table)

        if len(count_list) > 0:
            for title in count_list[0].keys():
                count_table.add_column(title)
            for row in count_list:
                count_table.add_row(
                    row.get("product_name"),
                    str(row.get("items_in_stock")),
                )
        console.print(count_table)
        return
    else:
        print("[bold red]No items found on this date[/bold red]")
