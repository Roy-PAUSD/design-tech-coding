import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Function to evaluate user input
def evaluate_function(func_str):
    # Handle the special case: convert "/func{1}{x}" to "1/x"
    if "/func{1}{x}" in func_str:
        func_str = "1/x"
    
    x = sp.symbols('x')
    func = sp.sympify(func_str)  # Parse the user input
    return sp.lambdify(x, func, "numpy")  # Return the function as a numpy-compatible function

# Get user input for the function
def graph():
    user_input = input("Enter a mathematical function (e.g., x**2 / 2), 'exit' to exit: ")
    if user_input.lower() == "exit":
        return  # Exit the function if the user types 'exit'
    
    # Convert user input into a callable function
    func = evaluate_function(user_input)

    # Create an array of x values
    x_vals = np.linspace(-10, 10, 400)

    # Calculate y values
    y_vals = func(x_vals)

    # Plot the graph
    plt.plot(x_vals, y_vals, label=f"y = {user_input}")
    plt.title(f"Graph of y = {user_input}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Recursive call to graph() for the next user input
    graph()

# Main function to start the graphing
def main():
    graph()

# Run the main function if the script is executed
if __name__ == '__main__':
    main()
