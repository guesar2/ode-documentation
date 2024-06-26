# ODE Docs

En este paquete se implementan tres algoritmos para la resolución
de ecuaciones diferenciales ordinarias (ODE) de la forma,
$$
    \frac{dx}{dt} = f(x, t)\,.
$$ 
Sujetas a la condición incial $x(0) = 0$.
Particularmente, se implementan los siguientes métodos de integración númerica:

- Euler: Partiendo de $x(0) = 0$ se calculan los valores de $x$ en el intervalo especificado utilizando la relación,
$$x(t + h) = x(t) + h f(x, t)$$

- Runge Kutta de segundo orden (RK2): En este caso se utiliza la relación,
$$x(t + h) = x(t) + k_2$$
donde,
$$ k_1 = h\,f(x,t)
$$
$$ k_2 = h\,f(x + k_1/2, t + h/2)
$$
- Runge Kutta de cuarto orden (RK4): Se utilizan las siguientes relaciones para obtener sucesivamente cada valor de $x$,
$$ k_1 = hf(x, t) $$
$$ k_2 = hf(x + \frac{k_1}{2}, t+\frac{h}2) $$
$$ k_3 = hf(x + \frac{k_2}{2}, t+\frac{h}2) $$
$$ k_4 = hf(x + k_3, t + h) $$
$$ x(t+h) = x(t) + \frac{1}{6}(k_1 + 2 k_2 + 2k_3 + k_4).$$ 

## Organización del proyecto

    ode/
        __init__.py 
        ode.py  # Módulo con la implementación.
