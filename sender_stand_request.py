import data
import requests
import config

def post_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE,
                         json=body,
                         headers=data.headers)
# Создает новый заказ

def get_poisk_zakaza(track):
    return requests.get(config.URL_SERVICE + config.CHEK + str(track))
# Создает запрос на отслеживание по номеру