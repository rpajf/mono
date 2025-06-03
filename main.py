from gdeltdoc import GdeltDoc, Filters, near, repeat
import pandas as pd

f = Filters(
    keyword = "climate change",
    start_date = "2020-05-10",
    end_date = "2020-05-11"
)
f2 = Filters(
    keyword = "artificial intelligence",  # <-- your subject here
    start_date = "2023-01-01",            # <-- start of interval
    end_date = "2024-01-07"               # <-- end of interval
)
gd = GdeltDoc()

# Search for articles matching the filters
articles = gd.article_search(f)

articles_ai = gd.article_search(f2)
print("Sample Article AI:")
for article in articles_ai[:3]:
    print(article)



f3 = Filters(
    start_date = "2020-05-01",
    end_date = "2020-05-02",
    num_records = 250,
    keyword = "climate change",
    # domain = ["bbc.co.uk", "nytimes.com"],
    # theme = "GENERAL_HEALTH",
    # near = near(10, "airline", "carbon"),
    # repeat = repeat(5, "planet")
)
articles_3 = gd.article_search(f3)
timeline_f3 = gd.timeline_search("timelinevol", f3)
print("Sample Article Climate Change:")

for article in timeline_f3[:3]:
    print(article)
print("\nTimeline Data:")
print(timeline_f3)

# Convert articles_3 to a DataFrame and print two articles, then store them into a CSV
articles_3_df = pd.DataFrame(articles_3)
print("\nFirst two articles from DataFrame:")
print(articles_3_df.head(2))

# Store the DataFrame into a CSV file
articles_3_df.to_csv("articles_climate_change.csv", index=False)

# Get a timeline of the number of articles matching the filters
# timeline = gd.timeline_search("timelinevol", f)
# print("\nTimeline Data:")
# print(timeline)