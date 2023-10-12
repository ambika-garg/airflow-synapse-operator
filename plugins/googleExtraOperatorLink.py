from airflow.plugins_manager import AirflowPlugin
from operators.RunSynapsePipelineOperator import AzureSynapsePipelineRunLink


from operators.googleOperator import GoogleLink

class AirflowExtraLinkPlugin(AirflowPlugin):
    name = "extra_link_plugin"
    operator_extra_links = [
        GoogleLink(), 
        AzureSynapsePipelineRunLink(),
    ]