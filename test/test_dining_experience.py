import pytest
import dining_experience

# Prueba para validar la selección de una cantidad válida de un plato
def test_valid_quantity():
    assert is_valid_quantity(2) == True

# Prueba para validar la selección de una cantidad inválida de un plato (cero)
def test_invalid_quantity_zero():
    assert is_valid_quantity(0) == False

# Prueba para validar la selección de una cantidad inválida de un plato (negativa)
def test_invalid_quantity_negative():
    assert is_valid_quantity(-3) == False

# Prueba para calcular el costo total sin aplicar descuentos
def test_calculate_total_cost_without_discounts():
    menu = {'pollo a la parrilla': 2, 'pizza margarita': 3, 'sopa de tomate': 1}
    total_cost = calcular_costo(menu)
    assert total_cost == 43

# Prueba para calcular el costo total aplicando descuento del 10%
def test_calculate_total_cost_with_10_percent_discount():
    menu = {'pollo a la parrilla': 5, 'pizza margarita': 3, 'sopa de tomate': 5}
    total_cost = calcular_costo(menu)
    assert total_cost == 52.2

# Prueba para calcular el costo total aplicando descuento del 20%
def test_calculate_total_cost_with_20_percent_discount():
    menu = {'pollo a la parrilla': 7, 'pizza margarita': 6, 'sopa de tomate': 8}
    total_cost = calcular_costo(menu)
    assert total_cost == 86.4

# Prueba para calcular el costo total aplicando descuento de $10
def test_calculate_total_cost_with_10_dollar_discount():
    menu = {'pizza margarita': 2, 'pastel de chocolate': 2}
    total_cost = calcular_costo(menu)
    assert total_cost == 10

# Prueba para calcular el costo total aplicando descuento de $25
def test_calculate_total_cost_with_25_dollar_discount():
    menu = {'pizza margarita': 5, 'pastel de chocolate': 5, 'especial del chef 1': 7}
    total_cost = calcular_costo(menu)
    assert total_cost == 83

# Prueba para calcular el costo total aplicando recargo del 5% a comidas especiales
def test_calculate_total_cost_with_5_percent_surcharge():
    menu = {'pizza margarita': 2, 'especial del chef 1': 2, 'especial del chef 2': 3}
    total_cost = calcular_costo(menu)
    assert total_cost == 72.75

# Prueba para calcular el costo total con una orden inválida (cantidad superior a 100)
def test_calculate_total_cost_with_invalid_order():
    menu = {'pizza margarita': 101}
    total_cost = calcular_costo(menu)
    assert total_cost == -1

# Prueba para calcular el costo total con una orden inválida (plato no disponible)
def test_calculate_total_cost_with_unavailable_meal():
    menu = {'pizza margarita': 2, 'hamburguesa': 2}
    total_cost = calcular_costo(menu)
    assert total_cost == -1

# Prueba para obtener una respuesta válida del usuario
def test_get_valid_response():
    with pytest.raises(StopIteration):
        responses = iter(['sii', 'no', 'sí', 'n'])
        for _ in range(4):
            respuesta = obtener_respuesta_valida(responses)
            assert respuesta == 'si' if _ < 2 else 'no'
