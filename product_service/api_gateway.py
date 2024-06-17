from aws_cdk import (
    aws_lambda as _lambda,
    Stack,
    #aws_sqs as aws_sqs
)
from constructs import Construct

Class ApiGateway(Stack):

    def __init__(self, scope:Construct, construct_id: str, get_products_list_fn: _lambda, get_product_by_id_fn: _lambda, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api= apigateway.RestApi(self, 'ProductServiceApi', rest_api_name = 'Product Service')


        products_resourse = api.root.add_resource('products')
        products_resourse.add_method('GET', apigateway.LambdaIntegration(get_products_list_fn)
        
        product_by_id_resourse = api.root.add_resource('{productid}')
        products_resourse.add_method('GET', apigateway.LambdaIntegration(get_product_by_id_fn)