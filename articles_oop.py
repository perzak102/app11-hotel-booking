import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv")


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()
        self.name = df.loc[df["id"] == self.id, "name"].squeeze()
        self.in_stock = df.loc[df["id"] == self.id, "in stock"].squeeze()

    @property
    def available(self):
        return self.in_stock

    def update_stock(self):
        df.loc[df["id"] == self.id, "in stock"] = self.in_stock - 1
        df.to_csv("articles.csv", index=False)


class Receipt:
    def __init__(self, article):
        self.article = article

    def print_receipt(self) -> object:
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)

id_to_buy = int(input("Choose an article to buy: "))
article = Article(id_to_buy)
if article.available:
    receipt = Receipt(article)
    receipt.print_receipt()
    article.update_stock()
else:
    print("No article in stock")

