from sklearn.neural_network import MLPClassifier

# Create a multilayer perceptron with 2 hidden layers, each with 10 neurons
mlp = MLPClassifier(hidden_layer_sizes=(10, 10))

# Train the multilayer perceptron on the training data
mlp.fit(X_train, y_train)

# Predict the class labels for the test data
y_pred = mlp.predict(X_test)