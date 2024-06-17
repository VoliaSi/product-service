import json

def handler(event, context):


    products = [
            {"id": "1", "title": "Product1", "description": "desc", "price" : 100},
            {"id": "2", "title": "Product2", "description": "desc", "price" : 200},
            {"id": "3", "title": "Product3", "description": "desc", "price": 300},
        ]

    return {'statusCode': 200,
            'headers' : {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "content-type": "application/json"
            },
            'body' :json.dumps(products)
    }