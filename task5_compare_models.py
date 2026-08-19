model_errors = {
    "Model A": 12.5,
    "Model B": 9.8,
    "Model C": 15.2
}

best_model = min(model_errors, key=model_errors.get)
best_mae = model_errors[best_model]

print("Best Model:", best_model)
print("Reason: It has the lowest MAE value of", best_mae)