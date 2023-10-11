from airflow.plugins_manager import AirflowPlugin
# from airflow.models.baseoperator import BaseOperator, BaseOperatorLink
# from airflow.models.taskinstancekey import TaskInstanceKey

from operators.googleOperator import GoogleLink
# , MyFirstOperator


class AirflowExtraLinkPlugin(AirflowPlugin):
    name = "extra_link_plugin"
    operator_extra_links = [
        GoogleLink(), 
    ]