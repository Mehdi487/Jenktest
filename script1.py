#test

#test2
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def test_connect(task):
  task.run(task=netmiko_send_command, command_string="show configuration | display xml")
 
results = nr.run(task=test_connect, name="TEST SCRIPT AGAIN!")
print_result(results)


