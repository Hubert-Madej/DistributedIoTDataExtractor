# Set up MQTT IoT Device variables
awslocal ssm put-parameter --name "MQTT/IoT/Device/Host" --value "localhost" --type "String"
awslocal ssm put-parameter --name "MQTT/IoT/Device/Port" --value "1883" --type "String"
awslocal ssm put-parameter --name "MQTT/IoT/Device/Topic" --value "core-device" --type "String"

# Set up MQTT IoT Gateway variables
awslocal ssm put-parameter --name "MQTT/IoT/Gateway/Host" --value "localhost" --type "String"
awslocal ssm put-parameter --name "MQTT/IoT/Gateway/Port" --value "1884" --type "String"
awslocal ssm put-parameter --name "MQTT/IoT/Gateway/Topic" --value "core-gateway" --type "String"
