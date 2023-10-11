from airflow.models.baseoperator import BaseOperator
from airflow.models.taskinstancekey import TaskInstanceKey
from airflow.models.baseoperator import BaseOperatorLink

class GoogleLink(BaseOperatorLink):
    name = "Google"

    def get_link(self, operator: BaseOperator, *, ti_key: TaskInstanceKey):
        return "https://www.google.com"

class MyFirstOperator(BaseOperator):

    operator_extra_links = (GoogleLink(), )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context):
        self.log.info("Hello World!")

# class GoogleLink(BaseOperatorLink):
#     name = "Google"
#     operators = [MyFirstOperator]
#     def get_link(self, operator: BaseOperator, *, ti_key: TaskInstanceKey):
#         return "https://www.google.com"

