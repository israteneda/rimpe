# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import pathlib
import pandas as pd


class ScraperPipeline:
    def __init__(self):
        # Create/Connect to database
        self.con = sqlite3.connect("rimpe.db")

        # Create cursor, used to execute commands
        self.cur = self.con.cursor()

        # Create quotes table if none exists
        self.cur.execute(
            """
                CREATE TABLE IF NOT EXISTS negocios(
                    ruc TEXT PRIMARY KEY,
                    razon_social TEXT NOL NULL,
                    zonal TEXT NOT NULL,
                    regimen TEXT NOT NULL,
                    negocio_popular TEXT NOT NULL
                )
            """
        )

    def process_item(self, item, _):
        print("Item: ", item)
        file_path = item["files"][0]["path"]
        absolute_path = f"{pathlib.Path().absolute().parent}/data/{file_path}"
        print("abs: ", absolute_path)
        negocios = pd.read_excel(
            absolute_path,
            header=None,
            names=["ruc", "razon_social", "zonal", "regimen", "negocio_popular"],
            skiprows=2,
        )
        negocios.to_sql("negocios", self.con, if_exists="append", index=False)

        return item
