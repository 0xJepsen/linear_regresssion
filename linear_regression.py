#!/usr/bin/env python
# coding: utf-8

# # Project: Linear Regression
# 
# Reggie is a mad scientist who has been hired by the local fast food joint to build their newest ball pit in the play area. As such, he is working on researching the bounciness of different balls so as to optimize the pit. He is running an experiment to bounce different sizes of bouncy balls, and then fitting lines to the data points he records. He has heard of linear regression, but needs your help to implement a version of linear regression in Python.
# 
# We will use loops, lists, and arithmetic to create a function that will find a line of best fit when given a set of data.

# Calculating Error

# 
# The line we will end up with will have a formula that looks like:
# ```
# y = m*x + b
# ```
# `m` is the slope of the line and `b` is the intercept, where the line crosses the y-axis.


def get_y(m, b, x):
  return m*x+b

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)


# 
# Reggie wants to try a bunch of different `m` values and `b` values and see which line produces the least error. To calculate error between a point and a line, he wants a function called `calculate_error()`, which will take in `m`, `b`, and an [x, y] point called `point` and return the distance between the line and the point.
# 
# The distance represents the error between the line `y = m*x + b` and the `point` given.
# 


def calculate_error(m,b,point):
    x_point = point[0]
    y_point = point[1]
    y_predict = get_y(m,b,x_point)
    return abs(y_point-y_predict)


# Let's test this function!

#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))


# Great! Reggie's datasets will be sets of points. For example, he ran an experiment comparing the width of bouncy balls to how high they bounce:
# 

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]


# The first datapoint, `(1, 2)`, means that his 1cm bouncy ball bounced 2 meters. The 4cm bouncy ball bounced 4 meters.
# 
# As we try to fit a line to this data, we will need a function called `calculate_all_error`, which takes `m` and `b` that describe a line, and `points`, a set of data like the example above.

def calculate_all_error(m,b,points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m,b,point)
    return total_error


#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))


#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))


# Great! It looks like we now have a function that can take in a line and Reggie's data and return how much error that line produces when we try to fit it to the data.
# 
# The way Reggie wants to find a line of best fit is by trial and error. He wants to try a bunch of different slopes (`m` values) and a bunch of different intercepts (`b` values) and see which one produces the smallest error value for his dataset.
# 

possible_ms = [m * 0.1 for m in range(-100, 101)]

# Now, let's make a list of `possible_bs` to check that would be the values from -20 to 20 inclusive, in steps of 0.1:

possible_bs = [b * 0.1 for b in range(-200, 201)]


# We are going to find the smallest error. First, we will make every possible `y = m*x + b` line by pairing all of the possible `m`s with all of the possible `b`s. Then, we will see which `y = m*x + b` line produces the smallest total error with the set of data stored in `datapoint`.

# We want to:
# * Iterate through each element `m` in `possible_ms`
# * For every `m` value, take every `b` value in `possible_bs`
# * If the value returned from `calculate_all_error` on this `m` value, this `b` value, and `datapoints` is less than our current `smallest_error`,
# * Set `best_m` and `best_b` to be these values, and set `smallest_error` to this error.
# 
# By the end of these nested loops, the `smallest_error` should hold the smallest error we have found, and `best_m` and `best_b` should be the values that produced that smallest error value.

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = (float("inf"))
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = calculate_all_error(m,b,datapoints)
print(best_m,best_b,smallest_error)


# What does our model predict?
# 
# Now we have seen that for this set of observations on the bouncy balls, the line that fits the data best has an `m` of 0.3 and a `b` of 1.7:
# 
# ```
# y = 0.3x + 1.7
# ```
# 
# This line produced a total error of 5.
# 


get_y(0.3,1.7,6)


# Our model predicts that the 6cm ball will bounce 3.5m.
# 
# Now, Reggie can use this model to predict the bounce of all kinds of sizes of balls he may choose to include in the ball pit!



