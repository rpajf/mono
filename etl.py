class ETLProcessor:
    def __init__(self, articles):
        self.articles = articles

    def run(self):
        print("ETL process started. This is a placeholder for your ETL logic.")
        # Arbitrarily divide into two categories: first half and second half
        mid = len(self.articles) // 2
        category_1 = self.articles[:mid]
        category_2 = self.articles[mid:]
        # print("Category 1 articles:", category_1)
        # print("Category 2 articles:", category_2)
