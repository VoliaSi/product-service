from aws_cdk import Stack
from product_service.api_gateway import ApiGateway
from product_service.get_product_by_id import ProductsById
from product_service.get_products import GetProducts
from constructs import Construct

Class MyCdkAppStack(Stack):

    def __init__(self, scope:Construct, id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        get_products_list_lbd = GetProducts(self, 'ProductsList')
        get_product_by_id_lbd = ProductsById(self, 'ProductsById')
        ApiGateway(self, 'APIGateway', get_products_list_fn = get_products_list_lbd.get_products_list, get_product_by_id_fn=get_product_by_id_lbd.get_product_by_id)
        
        self.get_products_by_id = _lambda.Function(
            self, 'GetProductsListHandler'.
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset('product_service/lambda_func/'),
            handler= 'product_by_id.handler'

        )