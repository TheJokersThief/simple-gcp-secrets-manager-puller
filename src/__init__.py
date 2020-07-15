from google.cloud import secretmanager


def get_client(*args, local=False, **kwargs):
    """
    Creates a secret manager client, forwarding *args and **kwargs to the constructor.

    local   :bool:  Return a None client to short-circuit trying to connect to
                    the secrets manager.
    """
    if local:
        return None

    # Create the Secret Manager client.
    return secretmanager.SecretManagerServiceClient(*args, **kwargs)


def get_secret_versions(client, project_id, secret_id):
    """
    Get all enabled secret versions in the given secret and their metadata.

    client      :SecretManagerServiceClient:    Client for interacting with secrets manager
    project_id  :str:   Name of the GCP project (e.g. myproject-staging)
    secret_id   :str:   Key for secret to fetch
    """

    # Build the resource name of the parent secret.
    parent = client.secret_path(project_id, secret_id)
    
    # Return all secret versions.
    return [
        version for version in client.list_secret_versions(parent)
        if  version.state == secretmanager.enums.SecretVersion.State.ENABLED
    ]


def get_latest_value(client, project_id, secret_id, default):
    """
    Retrieve latest, enabled secret value

    client      :SecretManagerServiceClient:    Client for interacting with secrets manager
    project_id  :str:   Name of the GCP project (e.g. myproject-staging)
    secret_id   :str:   Key for secret to fetch
    default     :str:   If client is None, the default value to return
    """
    return_value = default
    if client:
        versions = get_secret_versions(client, project_id, secret_id)
        latest = versions[0].name

        # Access the secret version.
        response = client.access_secret_version(latest)

        return_value = response.payload.data.decode('UTF-8')
    return return_value
