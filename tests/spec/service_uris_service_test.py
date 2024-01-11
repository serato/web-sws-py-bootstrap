from web_sws_py_bootstrap.service_uris_service import ServiceUrisService
import pytest
import os
import json
from pprint import pprint

def get_default_service_uris_data_provider():
    environments = {
        "dev",
        "staging",
        "preprod",
    }
    for environment in environments:
        yield environment

def get_default_service_uris_for_test_stack_data_provider():
    environments = {
        "test-1",
        "test-99",
    }
    for environment in environments:
        yield environment

@pytest.mark.parametrize("environment", get_default_service_uris_data_provider())
def test_get_default_service_uris(environment):
    service = ServiceUrisService(environment)
    expectedResult = get_uri_data(environment)
    actualResult = service.get_default_service_uris()

    assert expectedResult == actualResult

@pytest.mark.parametrize("environment", get_default_service_uris_for_test_stack_data_provider())
def test_get_default_service_uris_for_test_stack(environment):
    testUris = get_uri_data('test')

    expectedResult = {}
    for key, value in testUris.items():
          expectedResult[key] = value.replace(":test_env", environment)

    service = ServiceUrisService(environment)
    actualResult = service.get_default_service_uris()

    assert expectedResult == actualResult

def test_get_default_service_uris_for_invalid_stack():
    with pytest.raises(Exception) as excinfo:
        service = ServiceUrisService('invalid')
        actualResult = service.get_default_service_uris()
    assert str(excinfo.value) == 'Invalid environment'

def get_uri_data(environment):
    json_file = open(os.path.dirname(__file__) + "/../../web_sws_py_bootstrap/data/service_uris.json")
    uris = json.load(json_file)
    json_file.close()

    return uris[environment]

def test():
    return 0