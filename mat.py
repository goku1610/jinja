import matplotlib.pyplot as plt

# Data from the table (replace with actual data)
data = {
    'Company': ['P I Industries', 'UPL', 'Sumitomo Chemi.', 'Dhanuka Agritech',
                 'Rallis India', 'Bharat Rasayan', 'Sharda Cropchem',
                 'Meghmani Organi.', 'Median: 19 Co.'],
    'Market Cap (Rs.Cr.)': [57501.19, 42818.42, 24632.84, 7730.60, 6574.99,
                            4842.06, 4366.17, 2089.73, 2603.84]
}

# Sorting the data by Market Cap for visualization
sorted_data = sorted(data['Market Cap (Rs.Cr.)'], reverse=True)
companies = [data['Company'][i] for i in range(len(data['Market Cap (Rs.Cr.)']))
              if data['Market Cap (Rs.Cr.)'][i] in sorted_data]

# Creating the line graph
plt.figure(figsize=(10, 6))
plt.plot(companies, sorted_data, marker='o', linestyle='-', color='skyblue')
plt.xlabel('Companies')
plt.ylabel('Market Cap (Rs.Cr.)')
plt.title('Market Capitalization of Meghmani Organics Ltd. and its Peers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(True)  # Add a grid for better readability

# Save the graph as an image
plt.savefig('image.png', dpi=500)
plt.show()