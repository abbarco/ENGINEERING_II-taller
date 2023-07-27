import pytest
from dining_experience import calcular_costo

# Pruebas con respuestas esperadas

def test_calculate_cost_normal():
    orden = {
        'pollo a la parrilla': 2,
        'pizza margarita': 1,
        'sopa de tomate': 1
    }
    costo_esperado = 10*2 + 8*1 + 5*1
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_discount_10():
    orden = {
        'pollo a la parrilla': 2,
        'pizza margarita': 1,
        'sopa de tomate': 3
    }
    costo_esperado = (10*2 + 8*1 + 5*3) * 0.9
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_discount_20():
    orden = {
        'salchipapa': 10,
        'pizza margarita': 1,
        'sopa de tomate': 1
    }
    costo_esperado = (3*10 + 8*1 + 5*1) * 0.8
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_special_offer_USD50():
    orden = {
        'costillas asadas': 4,
        'pollo a la parrilla': 1,
    }
    costo_esperado = (13*4 + 10*1) - 10
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_special_offer_USD100():
    orden = {
        'langosta': 4,
        'costillas asadas': 1,
    }
    costo_esperado = (25*4 + 13*1) - 25
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_special_meal_surcharge():
    orden = {
        'especial del chef 1': 1,
        'pizza margarita': 3
    }
    costo_esperado = (15*1 + 8*3) * 1.05
    assert calcular_costo(orden) == costo_esperado

# Combinaciones descuento 10% | descuento 20% | especial $50 | especial $100 | recargo

def test_calculate_cost_discount_10_AND_special_offer_USD50():
    orden = {
        'langosta': 2,
        'pizza margarita': 2,
        'sopa de tomate': 3
    }
    costo_esperado = (25*2 + 8*2 + 5*3) * 0.9 - 10
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_discount_20_AND_special_offer_USD50():
    orden = {
        'salchipapa': 10,
        'langosta': 1,
        'sopa de tomate': 2
    }
    costo_esperado = (3*10 + 25*1 + 5*2) * 0.8 - 10
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_discount_10_AND_special_offer_USD100():
    orden = {
        'langosta': 5,
        'pizza margarita': 2,
        
    }
    costo_esperado = (25*5 + 8*2) * 0.9 - 25
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_discount_20_AND_special_offer_USD100():
    orden = {
        'salchipapa': 10,
        'langosta': 5,
    }
    costo_esperado = (3*10 + 25*5) * 0.8 - 25
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_discount_10_AND_surcharge():
    orden = {
        'especial del chef 1': 1,
        'salchipapa': 2,
        'sopa de tomate': 3
    }
    costo_esperado = (15*1 + 3*2 + 5*3) * 0.9 * 1.05
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_discount_20_AND_surcharge():
    orden = {
        'salchipapa': 10,
        'especial del chef 1': 1,
    }
    costo_esperado = (3*10 + 15*1) * 0.8 * 1.05
    assert calcular_costo(orden) == costo_esperado

def test_calculate_special_offer_USD50_AND_surcharge():
    orden = {
        'langosta': 3,
        'especial del chef 1': 1,
    }
    costo_esperado = ( (25*3 + 15*1) - 10 ) * 1.05
    assert calcular_costo(orden) == costo_esperado

def test_calculate_special_offer_USD100_AND_surcharge():
    orden = {
        'langosta': 4,
        'especial del chef 1': 1,
    }
    costo_esperado = ( (25*4 + 15*1) - 25 ) * 1.05
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_discount_10_AND_special_offer_USD50_AND_surcharge():
    orden = {
        'langosta': 2,
        'especial del chef 1': 1,
        'sopa de tomate': 3
    }
    costo_esperado = ( (25*2 + 15*1 + 5*3) * 0.9 - 10 ) * 1.05
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_discount_20_AND_special_offer_USD50_AND_surcharge():
    orden = {
        'salchipapa': 10,
        'langosta': 1,
        'especial del chef 1': 1,
    }
    costo_esperado = ( (3*10 + 25*1 + 15*1) * 0.8 - 10 ) * 1.05
    assert calcular_costo(orden) == costo_esperado
# Pruebas con respuestas no esperadas

def test_calculate_cost_empty_order():
    orden = {}
    assert calcular_costo(orden) == -1
