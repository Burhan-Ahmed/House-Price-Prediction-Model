# Linear Regression Model
I have used a supervised learning algorithm to build this Model using Linear regression that predicts the price of the house using square footage and the number of bedrooms and bathrooms in the house.

* A task done during my internship
- Multiple Linear regression was used to achieve the results.

# General Formula
- y=mx+c
where m is the slope and c is the intercept.

## Formula for this case
- y= m0+ m1*x1 + m2*x2 .... mn*xn+b

### Points to Ponder
`x_train,x_test,y_train,y_test`
- x_test and y_test is used train the model
- x_test is used to make predicts. Whereas, y_test will be usefull for calulating error or ratio of true positive.
- Default value for test_size is 0.25(25%) if not provided.