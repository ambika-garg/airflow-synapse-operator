from airflow.models.baseoperator import BaseOperator


class MyFirstOperator(BaseOperator):

    operator_extra_links = ("https://www.google.com")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context):
        self.log.info("Hello World!")
