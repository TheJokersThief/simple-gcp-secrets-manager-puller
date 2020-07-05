from google.cloud import secretmanager


def get_client(*args, **kwargs):
    # Create the Secret Manager client.
    return secretmanager.SecretManagerServiceClient(*args, **kwargs)


def get_secret_versions(client, project_id, secret_id):
    """
    Get all enabled secret versions in the given secret and their metadata.
    """

    # Build the resource name of the parent secret.
    parent = client.secret_path(project_id, secret_id)
    
    # Return all secret versions.
    return [
        version for version in client.list_secret_versions(parent)
        if  version.state == secretmanager.enums.SecretVersion.State.ENABLED
    ]


def get_latest_value(client, project_id, secret_id, default):
    versions = get_secret_versions(client, project_id, secret_id)
    latest = versions[0].name

    # Access the secret version.
    response = client.access_secret_version(latest.name)

    payload = response.payload.data.decode('UTF-8')
    return payload
