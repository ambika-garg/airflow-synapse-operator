from airflow.models import BaseOperator
import requests
from functools import cached_property
from hooks.azureSynapseHook import AzureSynapseHook

class SynapseRunPipelineOperator(BaseOperator):
    """
    Executes a Synapse Pipeline.
        :param workspace_name: The name of the Azure Synapse workspace.
        :param pipeline_name: The name of the pipeline to execute.
        :param azure_synapse_conn_id: The Airflow connection ID for Azure Synapse.
        :param spark_pool: The name of the Spark pool (optional).

    """

    def __init__(
        self,
        pipeline_name: str,
        azure_synapse_conn_id: str,
        *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.azure_synapse_conn_id = azure_synapse_conn_id
        self.pipeline_name = pipeline_name

    @cached_property
    def hook(self):
        """Create and return an AzureSynapseHook (cached)."""
        return AzureSynapseHook(azure_synapse_conn_id=self.azure_synapse_conn_id)

    def execute(self, context) -> None:
        self.log.info("Executing the %s pipeline.", self.pipeline_name)
        response = self.hook.run_pipeline(self.pipeline_name)
        self.log.info("response %s", response)
        # self.pipeline_run_url = response["pipeline_run_url"]

        # Push the ``pipeline_run_url`` value to XCom regardless of what happens during execution. This allows for
        # retrieval the executed pipeline's ``url`` for downstream tasks especially if performing an
        # asynchronous wait.
        # context["ti"].xcom_push(key="pipeline_run_url", value=self.pipeline_run_url)

