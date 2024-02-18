#1
# Draw a linear regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(x="time_since_first_purchase",
            y='has_churned',
            data=churn,
            ci=None,
            line_kws={"color": "red"})



plt.show()

#2
# Draw a linear regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(x="time_since_first_purchase",
            y="has_churned",
            data=churn, 
            ci=None,
            line_kws={"color": "red"})

# Draw a logistic regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(x="time_since_first_purchase",            
            y="has_churned",            
            data=churn,            
            ci=None,            
            logistic=True,
            line_kws={"color": "blue"})

plt.show()
