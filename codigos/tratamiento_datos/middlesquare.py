#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Método 'middle square' de von Neumann para generar números pseudoaleatorios.
Von Neumann's middle-square method to generate pseudo-random numbers.

La primera versión de esta función la escribió un asistente de IA y tenía un
error: convertía el cuadrado en texto sin completarlo con ceros a la
izquierda hasta 2n cifras, así que tomaba mal las cifras centrales en cuanto
aparecía un número con un cero inicial (por ejemplo 09633548).
The first version of this function was written by an AI assistant and had a
bug: it did not pad the square with leading zeros up to 2n digits.
"""


def middle_square(seed, num_digits, num_iterations):
    """
    seed: semilla, entero de como mucho num_digits cifras / integer seed
    num_digits: número de cifras n (par) / number of digits n (even)
    num_iterations: cuántos números generar / how many numbers to generate
    Devuelve una lista de enteros / returns a list of integers
    """
    if num_digits % 2 != 0 or seed >= 10**num_digits:
        raise ValueError('num_digits debe ser par y la semilla tener '
                         'como mucho num_digits cifras')
    current_number = seed
    random_numbers = []
    for _ in range(num_iterations):
        # cuadrado con 2n cifras, rellenando con ceros a la izquierda
        squared_str = str(current_number**2).zfill(2*num_digits)
        mid_start = num_digits // 2
        current_number = int(squared_str[mid_start:mid_start + num_digits])
        random_numbers.append(current_number)
    return random_numbers


# Comprobaciones con los ejemplos del texto / tests with the text examples
assert middle_square(87289689, 8, 4) == [48980571, 9633548, 80524706,
                                         22827638]
assert middle_square(3708, 4, 8) == [7492, 1300, 6900, 6100, 2100, 4100,
                                     8100, 6100]

print(middle_square(3708, 4, 10))
