actual = [100, 200, 300]
predicted = [110, 190, 310]

absolute_errors = []

for a, p in zip(actual, predicted):
    error = abs(a - p)
    absolute_errors.append(error)

mae = sum(absolute_errors) / len(absolute_errors)

print("Absolute Errors:", absolute_errors)
print("Mean Absolute Error:", mae)