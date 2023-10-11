from airflow.models.baseoperator import BaseOperator


class MyFirstOperator(BaseOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context):
        self.log.info("Hello World!")
