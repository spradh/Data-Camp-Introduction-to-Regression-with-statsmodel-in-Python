#1
# Define a DataFrame impossible
impossible = pd.DataFrame({'n_convenience': [-1,2.5]})

#2
mdl_price_vs_conv.predict(impossible)
