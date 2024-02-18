#1
# Update prediction data with odds_ratio
prediction_data["odds_ratio"] = prediction_data['has_churned']/(1-prediction_data['has_churned'])

# Print the head
print(prediction_data.head())

#2
# Update prediction data with odds_ratio
prediction_data["odds_ratio"] = prediction_data["has_churned"] / (1 - prediction_data["has_churned"])

fig = plt.figure()

# Create a line plot of odds_ratio vs time_since_first_purchase
sns.lineplot(x='time_since_first_purchase',
             y='odds_ratio',
             data=prediction_data)

# Add a dotted horizontal line at odds_ratio = 1
plt.axhline(y=1, linestyle="dotted")

plt.show()
