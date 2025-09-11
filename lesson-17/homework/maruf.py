import pandas as pd
import numpy as np

# DataFrame creation
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Rename columns using a function
df.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)
# Now "First Name" --> "first_name", "Age" --> "age", etc.

# Print first 3 rows
print("First 3 rows:")
print(df.head(3))
print()

# Find mean age
mean_age = df['age'].mean()
print(f"Mean age: {mean_age}")
print()

# Select and print only 'first_name' and 'city' columns
print("Selected columns (first_name and city):")
print(df[['first_name', 'city']])
print()

# Add new column 'salary' with random values (let's say between 40k to 100k)
np.random.seed(42)  # for reproducibility
df['salary'] = np.random.randint(40000, 100001, size=len(df))

print("DataFrame with Salary column:")
print(df)
print()

# Display summary statistics
print("Summary statistics:")
print(df.describe(include='all'))
Homework 2
python
Копировать код
# Create sales_and_expenses DataFrame
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# Max sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

print(f"Maximum sales: {max_sales}")
print(f"Maximum expenses: {max_expenses}")
print()

# Min sales and expenses
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

print(f"Minimum sales: {min_sales}")
print(f"Minimum expenses: {min_expenses}")
print()

# Average sales and expenses
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

print(f"Average sales: {avg_sales}")
print(f"Average expenses: {avg_expenses}")
Homework 3
python
Копировать код
# Create expenses DataFrame
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Set 'Category' as index
expenses.set_index('Category', inplace=True)

# Max expense for each category
max_expense = expenses.max(axis=1)
print("Maximum expense for each category:")
print(max_expense)
print()

# Min expense for each category
min_expense = expenses.min(axis=1)
print("Minimum expense for each category:")
print(min_expense)
print()

# Average expense for each category
avg_expense = expenses.mean(axis=1)
print("Average expense for each category:")
print(avg_expense)
If you want, I can help you run or explain any of these sections. Would you like that?

