import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Load the dataset
file_path = "C:/Users/undha/Downloads/updated_retail_data.xlsx"  # Replace with your actual file path
sheet_name = "Sheet1"

# Load the data from the Excel file
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Display basic information about the dataset
print("Dataset Overview:")
print(data.head())
print("\nColumns in Dataset:")
print(data.columns)

# Create a bar chart for "Total Sales After Discount"
plt.figure(figsize=(15, 7))
plt.bar(data["Product Name"], data["Total Sales After Discount"], color="skyblue")
plt.xlabel("Product Name")
plt.ylabel("Total Sales After Discount")
plt.title("Total Sales After Discount for Each Product")
plt.xticks(rotation=90)
plt.tight_layout()

# Save and display the graph
graph_file = "total_sales_after_discount_graph.png"
plt.savefig(graph_file)
plt.show()

print(f"Graph saved as {graph_file}")
