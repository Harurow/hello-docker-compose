# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------------------------------

import time
import requests
import os

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
node_neworder_dapr_url = "http://localhost:{}/v1.0/invoke/nodeapp/method/neworder".format(dapr_port)
deno_neworder_dapr_url = "http://localhost:{}/v1.0/invoke/denoapp/method/neworder".format(dapr_port)
node_order_dapr_url = "http://localhost:{}/v1.0/invoke/nodeapp/method/order".format(dapr_port)
deno_order_dapr_url = "http://localhost:{}/v1.0/invoke/denoapp/method/order".format(dapr_port)

print("start")

n = 0
while True:
    n += 1
    message = {"data": {"orderId": n}}

    try:
        response = requests.post(node_neworder_dapr_url, json=message)
    except Exception as e:
        print(e)

    try:
        response = requests.post(deno_neworder_dapr_url, json=message)
    except Exception as e:
        print(e)

    if (n % 10) == 0:
        print(n)
        try:
            response = requests.get(node_order_dapr_url, json=message)
            print(response)
        except Exception as e:
            print(e)
        try:
            response = requests.get(deno_order_dapr_url, json=message)
            print(response)
        except Exception as e:
            print(e)

    time.sleep(1)
