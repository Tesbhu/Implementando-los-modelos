import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Generar datos simulados
np.random.seed(0)
n_samples = 100
months_sales = np.random.randint(5000000, 15000000, n_samples)
correlated_variable1 = months_sales * np.random.uniform(0.5, 1.5, n_samples)
correlated_variable2 = np.random.randint(100000, 500000, n_samples)
correlated_variable3 = np.random.randint(1, 10, n_samples)
target_sales = months_sales * 1.5 + correlated_variable1 * 0.7 + correlated_variable2 * 0.3 + correlated_variable3 * 0.5 + np.random.normal(0, 2000000, n_samples)

# Crear un dataframe con los datos
import pandas as pd
data = pd.DataFrame({'MonthsSales': months_sales,
                     'CorrelatedVar1': correlated_variable1,
                     'CorrelatedVar2': correlated_variable2,
                     'CorrelatedVar3': correlated_variable3,
                     'TargetSales': target_sales})

# Dividir los datos en conjunto de entrenamiento y prueba
X = data.drop('TargetSales', axis=1)
y = data['TargetSales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Entrenar un modelo de árbol de decisiones
tree_model = DecisionTreeRegressor(random_state=0)
tree_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predictions = tree_model.predict(X_test)

# Calcular el error absoluto medio
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, predictions)
print(f"Error absoluto medio: {mae}")

# Visualizar el árbol de decisiones (opcional)
from sklearn.tree import plot_tree
plt.figure(figsize=(12, 6))
plot_tree(tree_model, feature_names=X.columns, filled=True, rounded=True)
plt.show()
