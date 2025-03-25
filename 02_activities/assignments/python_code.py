import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
df = pd.read_excel("khp_2019_moh_export_open_data_updated.xlsx")

# Cleaning column names
df.columns = df.columns.str.strip()

# Using 'MailingAddress1' as a proxy for service location
location_counts = df["MailingAddress1"].value_counts().head(15)

# Plotting the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=location_counts.values, y=location_counts.index, palette="viridis")
plt.xlabel("Number of Services")
plt.ylabel("Location")
plt.title("Top 15 Ontario Locations by Number of Child & Youth Mental Health Services")
plt.tight_layout()

# Saving the chart as a PNG image
plt.savefig("mental_health_services_by_location.png")
plt.show()
