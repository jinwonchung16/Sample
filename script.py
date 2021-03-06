import sys
import requests

print(sys.executable)
print(sys.version)


def greet(who_to_greet):
    greeting = f"hello, {who_to_greet}"
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
