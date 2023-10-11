from airflow.plugins_manager import AirflowPlugin

class AirflowExtraLinkPlugin(AirflowPlugin):
    name = "extra_link_plugin"
    operator_extra_links = [
        "https://www.google.com"
    ]