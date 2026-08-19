actual = [2, 4, 6]
predicted = [3, 5, 7]

squared_errors = []

for a, p in zip(actual, predicted):
    error = (a - p) ** 2
    squared_errors.append(error)

mse = sum(squared_errors) / len(squared_errors)

print("Squared Errors:", squared_errors)
print("Mean Squared Error:", mse)