import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_ecr_client():
    """
    Returns an ECR client using boto3.

    Returns:
    boto3.ECR: an instance of the ECR client.
    """
    return boto3.client('ecr')


def delete_images(client, registry_id, repository_name, image_ids):
    """
    Deletes untagged images from a given ECR repository.

    Args:
    client: boto3 ECR client instance.
    registry_id: ID of the registry that contains the repository.
    repository_name: Name of the repository from which to delete images.
    image_ids: A list of dictionaries with the image details.
    """
    try:
        response = client.batch_delete_image(
            registryId=registry_id,
            repositoryName=repository_name,
            imageIds=image_ids
        )

        if response["failures"]:
            logger.error(f"Failures occurred while deleting images in repository '{repository_name}': {response['failures']}")
        else:
            logger.info(f"Successfully deleted images from repository '{repository_name}'")

    except Exception as e:
        logger.error(f"Error deleting images from repository '{repository_name}': {str(e)}")


def handle_repository(client, repository):
    """
    Handles the deletion of untagged images from a single repository.

    Args:
    client: boto3 ECR client instance.
    repository: A dictionary with the repository details.
    """
    registry_id = repository["registryId"]
    repository_name = repository["repositoryName"]

    try:
        untagged_images = client.list_images(
            registryId=str(registry_id),
            repositoryName=str(repository_name),
            filter={
                'tagStatus': 'UNTAGGED'
            }
        )

        if untagged_images["imageIds"]:
            logger.info(f"Found untagged images in repository '{repository_name}'")
            delete_images(client, registry_id, repository_name, untagged_images["imageIds"])
        else:
            logger.info(f"No untagged images found in repository '{repository_name}'")

    except Exception as e:
        logger.error(f"Error handling repository '{repository_name}': {str(e)}")


def lambda_handler(event, context):
    try:
        client = get_ecr_client()
        repositories_dict = client.describe_repositories()

        for repository in repositories_dict["repositories"]:
            handle_repository(client, repository)

        logger.info("Execution succeeded.")
        return {
            'statusCode': 200,
            'body': "Execution succeeded."
        }

    except Exception as e:
        logger.error(f"Execution failed: {str(e)}")
        return {
            'statusCode': 400,
            'body': f"Execution failed: {str(e)}"
        }