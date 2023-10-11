from airflow.plugins_manager import AirflowPlugin
from airflow.models.baseoperator import BaseOperator, BaseOperatorLink
from airflow.models.taskinstancekey import TaskInstanceKey

from operators.googleOperator import MyFirstOperator


class GoogleLink(BaseOperatorLink):
    name = "Google"

    operators=[MyFirstOperator]
    def get_link(self, operator: BaseOperator, *, ti_key: TaskInstanceKey):
        return "https://www.google.com"

class AirflowExtraLinkPlugin(AirflowPlugin):
    name = "extra_link_plugin"
    operator_extra_links = [
        GoogleLink(), 
    ]