# simple-gcp-secrets-manager-puller
A _very very_ simple secret puller abstraction for GCP Secrets Manager.

Designed to be dropped into something like a python config file to pull a secret at application startup. As such, it provides a default value that is used if the client is `None` so local applications don't have to rely on the secrets manager.

## Example usage

```python
from secretpuller import get_client, get_latest_value

test_client = get_client()
secret_value = get_latest_value(test_client, "myproject-staging", "flask_secret_key", "test")
```
