__all__ = ['product_data']

from pathlib import Path

d = Path(__file__).parent

with open(d / 'product_data.sql', 'r', encoding='utf-8') as file:
    product_data = file.read()
