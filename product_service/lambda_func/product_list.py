import json

def handler(event, context):


    products = [
            {"id": "1", "name": "Product1", "price" 100},
            {"id": "2", "name": "Product2", "price" 200},
        ]

    return {'statusCode': 200,
            'headers' : {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "content-type": "application/json"
            },
            "body" :jsonduns: json: dumps(products)
    }