import argparse

# [START auth_cloud_implicit]
def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)
# [END auth_cloud_implicit]


# [START auth_cloud_explicit]
def explicit():
    from google.cloud import storage

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        'service_account.json')

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)
# [END auth_cloud_explicit]


# [START auth_cloud_explicit_compute_engine]
def explicit_compute_engine(project):
    from google.auth import compute_engine
    from google.cloud import storage

    # Explicitly use Compute Engine credentials. These credentials are
    # available on Compute Engine, App Engine Flexible, and Container Engine.
    credentials = compute_engine.Credentials()

    # Create the client using the credentials and specifying a project ID.
    storage_client = storage.Client(credentials=credentials, project=project)

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)
# [END auth_cloud_explicit_compute_engine]

def create_object():
    from google.cloud import storage
    from datetime import datetime

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('dev-gke-batch')
    blob = bucket.blob(current_time + '-test.txt')
    blob.upload_from_filename('input/test.txt')
    print('uploaded:' + current_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('implicit', help=implicit.__doc__)
    subparsers.add_parser('explicit', help=explicit.__doc__)
    explicit_gce_parser = subparsers.add_parser(
        'explicit_compute_engine', help=explicit_compute_engine.__doc__)
    explicit_gce_parser.add_argument('project')
    subparsers.add_parser('create_object', help=create_object.__doc__)

    args = parser.parse_args()

    if args.command == 'implicit':
        implicit()
    elif args.command == 'explicit':
        explicit()
    elif args.command == 'create_object':
        create_object()
    elif args.command == 'explicit_compute_engine':
        explicit_compute_engine(args.project)

