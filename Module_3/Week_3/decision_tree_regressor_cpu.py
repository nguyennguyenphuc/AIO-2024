# Import necessary libraries
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Load the machine CPU dataset
machine_cpu = fetch_openml(name='machine_cpu', version=1)
machine_data = machine_cpu.data
machine_labels = machine_cpu.target

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    machine_data, machine_labels, test_size=0.2, random_state=42
)

# Initialize the Decision Tree Regressor
tree_reg = DecisionTreeRegressor(random_state=42,
                                 ccp_alpha=0.01)

# Train the model
tree_reg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = tree_reg.predict(X_test)

# Evaluate the model using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Print the MSE
print(f"Mean Squared Error: {mse:.2f}")
