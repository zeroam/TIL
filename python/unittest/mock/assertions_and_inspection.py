from unittest.mock import Mock

# Create a mock object
json = Mock()

print(json.loads('{"key": "value"}'))

# You know that you called loads() so you can
# make assertions to test that expectation
json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')

print(json.loads('{"key": "value"}'))

# If an assertion fails, the mock will raise an AssertionError
try:
    json.loads.assert_called_once()
except AssertionError as e:
    print(e)

try:
    json.loads.assert_called_once_with('{"key": "value"}')
except AssertionError as e:
    print(e)

try:
    json.loads.assert_not_called()
except AssertionError as e:
    print(e)


print('Number of times you called loads():')
print(json.loads.call_count)

print('The last loads() call:')
print(json.loads.call_args)

print('List of loads() calls:')
print(json.loads.call_args_list)

print("List of calls to json's methods (recursively)")
print(json.method_calls)
