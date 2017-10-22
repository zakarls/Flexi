from spyrk import SparkCloud

USERNAME = 'he.ho@example.com'
PASSWORD = 'pasSs'
ACCESS_TOKEN = '12adza445452d4za524524524d5z2a4'

spark = SparkCloud(USERNAME, PASSWORD)
# Or
spark = SparkCloud(ACCESS_TOKEN)

# List devices
print spark.devices

# Access device
spark.devices['captain_hamster']
# Or, shortcut form
spark.captain_hamster

# List functions and variables of a device
print spark.captain_hamster.functions
print spark.captain_hamster.variables

# Tell if a device is connected
print spark.captain_hamster.connected

# Call a function
spark.captain_hamster.digitalwrite('D7', 'HIGH')
print spark.captain_hamster.analogread('A0')
# (or any of your own custom function)

# Get variable value
spark.captain_hamster.myvariable
