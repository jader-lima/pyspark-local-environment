import pandas as pd
import random
import time
import argparse

def generate_products(number, output_path):
    """Gera arquivos CSV de produtos com informações de venda."""
    products = [
        {"id": "0", "name": "nintendo", "price": 50.0},
        {"id": "1", "name": "super-nintendo", "price": 200.0},
        {"id": "2", "name": "ps1", "price": 150.0},
        {"id": "3", "name": "ps2", "price": 230.0},
        {"id": "4", "name": "xbox", "price": 230.0},
        {"id": "5", "name": "ps3", "price": 270.0},
        {"id": "6", "name": "xbox-360", "price": 270.0},
        {"id": "7", "name": "xbox-one", "price": 500.0},
        {"id": "8", "name": "ps4", "price": 500.0},
        {"id": "9", "name": "xbox-series", "price": 600.0},
        {"id": "10", "name": "pc-gamer", "price": 1200.0}
    ]
    
    for i in range(number):
        n = random.randint(0, len(products) - 1)
        amount = random.randint(1, 10)
        discount = random.randint(0, 9)
        
        data = pd.DataFrame({
            "id": [products[n].get('id')],
            "product": [products[n].get('name')],
            "price": [products[n].get('price')],
            "amount": [amount],
            "total_price": [(products[n].get('price') * amount) - (products[n].get('price') * float("0.%s" % (discount)))],
            "discount": [products[n].get('price') * float("0.%s" % (discount))]
        })
        
        data.to_csv(f"{output_path}/sells{i}.csv", index=False)
        time.sleep(5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Geração de dados de produtos.")
    parser.add_argument("--output_path", type=str, required=True, help="Diretório de saída para os arquivos CSV")
    parser.add_argument("--number", type=int, default=50, help="Número de arquivos a serem gerados")

    args = parser.parse_args()
    generate_products(args.number, args.output_path)
