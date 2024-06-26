# ode/ode.py

"""Proporciona funciones que implementan
métodos númericos para resolver ODEs de primer orden

El módulo contiene las siguientes funciones:


- `rk2(a, b, n_steps, func)` - Resulve la ODE utilizando RK2.
- `rk4(a, b, n_steps, func)` - Resulve la ODE utilizando RK4.
- `euler(a, b, n_steps, func)` - Resulve la ODE utilizando el método de Euler.
"""

import numpy as np


def rk2(a, b, n_steps, func):
    """Encuentra el valor de la solución a la ODE
    utilizando el método RK2
    
    Examples:
        >>> x, t = rk2(0, 5, 5, lambda x, t: x + t)
        >>> print(x)
        >>> print(t)

    Args:
        a (float): tiempo inicial
        b (float): tiempo final
        n_steps (_type_): número de pasos
        func (_type_): función f(x, t) tal que y'(t) = f(x, t)

    Returns:
        tuple: una tupla con dos numpy arrays:
            - x (numpy.ndarray): arreglo con los valores de la variable dependiente
            - t (numpy.ndarray): arreglo con los valores de la variable independiente
    """

    x = np.zeros(n_steps)
    t = np.linspace(a, b, n_steps)
    h = t[1] - t[0]
    for i in range(n_steps - 1):
        k1 = h * func(x[i], t[i])
        k2 = h * func(x[i] + k1 / 2, t[i] + h / 2)
        x[i + 1] = x[i] + k2

    return x, t


def rk4(a, b, n_steps, func):
    """Encuentra el valor de la solución a la ODE
    utilizando el método RK4

    Examples:
        >>> x, t = rk4(0, 5, 5, lambda x, t: x + t)
        >>> print(x)
        >>> print(t)

    Args:
        a (float): tiempo inicial
        b (float): tiempo final
        n_steps (_type_): número de pasos
        func (_type_): función f(x, t) tal que y'(t) = f(x, t)

    Returns:
        tuple: una tupla con dos numpy arrays:
            - x (numpy.ndarray): arreglo con los valores de la variable dependiente
            - t (numpy.ndarray): arreglo con los valores de la variable independiente
    """

    x = np.zeros(n_steps)
    t = np.linspace(a, b, n_steps)
    h = t[1] - t[0]
    for i in range(n_steps - 1):
        k1 = h * func(x[i], t[i])
        k2 = h * func(x[i] + k1 / 2, t[i] + h / 2)
        k3 = h * func(x[i] + k2 / 2, t[i] + h / 2)
        k4 = h * func(x[i] + k3, t[i] + h)
        x[i + 1] = x[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return x, t


def euler(a, b, n_steps, func):
    """Encuentra el valor de la solución a la ODE
    utilizando el método de Euler

    Examples:
        >>> x, t = euler(0, 5, 5, lambda x, t: x + t)
        >>> print(x)
        >>> print(t)

    Args:
        a (float): tiempo inicial
        b (float): tiempo final
        n_steps (_type_): número de pasos
        func (_type_): función f(x, t) tal que y'(t) = f(x, t)

    Returns:
        tuple: una tupla con dos numpy arrays:
            - x (numpy.ndarray): arreglo con los valores de la variable dependiente
            - t (numpy.ndarray): arreglo con los valores de la variable independiente
    """
    x = np.zeros(n_steps)
    t = np.linspace(a, b, n_steps)
    h = t[1] - t[0]
    for i in range(n_steps - 1):
        x[i + 1] = x[i] + h * func(x[i], t[i])

    return x, t
