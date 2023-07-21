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

def test_calculate_cost_special_offer_1():
    orden = {
        'costillas asadas': 4,
        'pollo a la parrilla': 1,
    }
    costo_esperado = (13*4 + 10*1) - 10
    assert calcular_costo(orden) == costo_esperado

def test_calculate_cost_special_offer_2():
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

# Pruebas con respuestas no esperadas

def test_calculate_cost_empty_order():
    orden = {}
    assert calcular_costo(orden) == -1
