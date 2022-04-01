import matplotlib.pyplot as plt


def plot_inventory(data):
    if len(data) == 0:
        return
    date = data[0]["buy_date"][0:10]
    products = []
    price = []
    for index, row in enumerate(data):
        products.append(f"{index + 1}." + row["product_name"])
        price.append(float(row["buy_price"]))
    plt.bar(products, price, bottom=0)
    plt.xlabel("Products")
    plt.ylabel("Price in US-Dollar $")
    plt.title(f"Products we bought on {date}")
    plt.show()
