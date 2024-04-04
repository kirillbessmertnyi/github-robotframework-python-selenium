import os.path
import json
from httpx import Client as HttpxClient
from aqua_rest_api_client import AuthenticatedClient
from aqua_rest_api_client.api.test_execution import test_execution_create
from aqua_rest_api_client.models.api_test_execution_new import ApiTestExecutionNew
from aqua_rest_api_client.models.api_test_step_execution_new import ApiTestStepExecutionNew
from aqua_rest_api_client.models.api_test_step_execution_step_type import ApiTestStepExecutionStepType
from aqua_rest_api_client.models.api_test_step_execution_update_status import ApiTestStepExecutionUpdateStatus
from aqua_rest_api_client.models.api_field_value_time_span import ApiFieldValueTimeSpan
from aqua_rest_api_client.models.time_unit import TimeUnit
from aqua_rest_api_client.models.api_attachment_new import ApiAttachmentNew
import requests

class Hooks:
    ROBOT_LISTENER_API_VERSION = 2
    
    AQUA_BASE_URL="https://app.aqua-cloud.io/aquawebng"
    AQUA_USERNAME="***PUT***AQUA***USERNAME***HERE***"
    AQUA_PASSWORD="***PUT***AQUA***PASSWORD***HERE***"

    def get_access_token(
        self, aqua_base_url: str, aqua_user: str, aqua_password: str
    ) -> str:
        # Authenticate against aqua server. The token is 15min valid, refresh_token can be used to generate a new token.
        auth_client = HttpxClient(base_url=aqua_base_url)
        response = auth_client.post(
            url="api/token",
            data={
                "grant_type": "password",
                "username": aqua_user,
                "password": aqua_password,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        response = json.loads(response.content)

        return response["access_token"]

    def upload_binary_file(self, aqua_base_url: str, access_token: str, file_path: str) -> str:
        with open(file_path,"rb") as file:
            headers = {
            "Authorization": f"Bearer {access_token}"
            }
            name = os.path.basename(file_path)
            response = requests.post(f"{aqua_base_url}/api/File?fileName={name}", data=file.raw, headers=headers)
            return json.loads(response.content)["Guid"]
   

    def create_singleTCAquaExecution(self, aquaTCID, result, duration, files):

        tokenAPI = self.get_access_token(aqua_base_url=self.AQUA_BASE_URL, 
                                         aqua_user=self.AQUA_USERNAME, 
                                         aqua_password=self.AQUA_PASSWORD)
        clientApi = AuthenticatedClient(base_url=self.AQUA_BASE_URL, token=tokenAPI)

        filesGuids = []

        for val in files:
            filesGuids.append(ApiAttachmentNew(self.upload_binary_file(aqua_base_url=self.AQUA_BASE_URL, access_token=tokenAPI, file_path=val)))
        
        stepStatus = ApiTestStepExecutionUpdateStatus.PASS
        if (result == 'FAIL'):
         stepStatus = ApiTestStepExecutionUpdateStatus.FAILED
        elif (result != 'PASS'):
         raise Exception("test execution has other status")
        
        testSteps = ApiTestStepExecutionNew(index=1,
                                            name="Step 1",
                                            step_type=ApiTestStepExecutionStepType.STEP,
                                            status=stepStatus)
        testDuration = ApiFieldValueTimeSpan(field_value_type='TimeSpan', text=None, value=duration/1000, unit=TimeUnit.SECOND)
        executionInfo = ApiTestExecutionNew(guid=None, 
                                            test_case_id=aquaTCID, 
                                            test_case_name=None,
                                            finalize=False,
                                            value_set_name=None,
                                            test_scenario_info=None,
                                            steps=[testSteps],
                                            tested_version="Robot Framework 7.0",
                                            execution_duration=testDuration,
                                            attached_labels=None,
                                            custom_fields=None,
                                            attachments=filesGuids)
        executionResponse = test_execution_create.sync(client=clientApi, json_body=[executionInfo])

    def end_test(self, name, attrs):
        files = []
        parentPath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
        if (attrs['status']=='FAIL'):
            files.append(os.path.join(parentPath, "Failure_"+str(name)+".png"))

        self.create_singleTCAquaExecution(attrs['tags'][0], attrs['status'], attrs['elapsedtime'], files)
        print(attrs['message'])
