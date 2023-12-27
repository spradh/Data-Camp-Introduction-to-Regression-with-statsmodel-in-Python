# Create a new figure, fig
fig = plt.figure()

sns.regplot(x="n_convenience",
            y="price_twd_msq",
            data=taiwan_real_estate,
            ci=None)
# Add a scatter plot layer to the regplot
sns.scatterplot(x='n_convenience', 
                y='price_twd_msq', 
                data=prediction_data,
                color='red',
                marker='s')

# Show the layered plot
plt.show()
