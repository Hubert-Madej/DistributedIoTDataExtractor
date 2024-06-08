from enum import StrEnum, auto
from typing import Dict
import boto3

class ConfigItems(StrEnum):
  MQTT_DEVICE_HOST = auto()
  MQTT_DEVICE_PORT = auto()
  MQTT_DEVICE_TOPIC = auto()

_SSM_PARAMETERS_NAMES: dict[str, str] = {
  ConfigItems.MQTT_DEVICE_HOST: "MQTT/IoT/Device/Host",
  ConfigItems.MQTT_DEVICE_PORT: "MQTT/IoT/Device/Port",
  ConfigItems.MQTT_DEVICE_TOPIC: "MQTT/IoT/Device/Topic"
}

def load_config():
  ssm = boto3.client("ssm")
  
  try:
    ssm_response = ssm.get_parameters(Names=list(_SSM_PARAMETERS_NAMES.values()))
    ssm_param_dict = {_p["Name"]: _p["Value"] for _p in ssm_response["Parameters"]}
  except Exception as e:
    raise RuntimeError("Failed to fetch SSM Parameters: " +str(e))

  config = {}
  for (_item, _ssm_param_name) in _SSM_PARAMETERS_NAMES.items():
    try:
      config[_item] = _convert_parameter(_item, ssm_param_dict[_ssm_param_name])
    except KeyError as e:
      raise RuntimeError(f"Faile to load parameter {_item} from SSM.")

def _convert_parameter():
  print(_convert_parameter)