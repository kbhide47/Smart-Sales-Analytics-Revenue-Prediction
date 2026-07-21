import os

os.makedirs("data/documents", exist_ok=True)

text = """
Business Knowledge

Category:
Furniture
Office Supplies
Technology

Regions:
West
East
South
Central

KPIs:
Sales
Profit
Orders
Discount

Use professional business language while answering.
"""

with open(
    "data/documents/business_knowledge.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(text)

print("Knowledge Base Created")