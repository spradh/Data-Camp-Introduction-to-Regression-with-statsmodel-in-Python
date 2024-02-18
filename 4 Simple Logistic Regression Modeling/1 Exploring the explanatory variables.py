#1
# Create the histograms of time_since_last_purchase split by has_churned
sns.displot(x='time_since_last_purchase', col='has_churned', data = churn)

plt.show()


#2
# Create the histograms of time_since_last_purchase split by has_churned
sns.displot(x='time_since_first_purchase', col='has_churned', data = churn)

plt.show()
