import sqlite3
import pandas as pd

class DataHandler:
    def __init__(self,db_path = r'C:\Users\Administrator\DataGripProjects\MySQL-project\xianyu_auto.sqlite'):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def read_first_item(self):
        """
        读取数据库中的第一个商品名字。
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 厂商, SearchName_1, SearchName_2, SearchName_3 FROM 商品信息 LIMIT 1")
        row = cursor.fetchone()
        conn.close()

        if row:
            return row
        else:
            raise ValueError("商品信息数据库为空")

    def save_report(self, data):
        """
        将爬取的数据存储为 Excel 报告。
        """
        if not data:
            print("没有数据可用于生成报告")
            return

        df = pd.DataFrame(data)
        from datetime import datetime
        report_path = f"data/report/crawled_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

        try:
            df.to_excel(report_path, index=False)
            print(f"报告已生成：{report_path}")
        except Exception as e:
            print(f"保存报告时出错：{e}")


