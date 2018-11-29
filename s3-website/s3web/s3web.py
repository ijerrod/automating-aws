# -*- coding: utf-8 -*-

"""s3web.py used to deply websites with AWS.

S3web.py automates deploying static websites to AWS
- Configure AWS S3 list_buckets
  - Creates buckets
  - Set them up for static website hosting
  - Deploys local files to the buckets
- Configure DNS with AWS Route 53
- Configure a Content Devlivery Network and SSL with AWS Cloudfront
"""

import boto3
import click

from bucket import BucketManager

session = boto3.Session(profile_name='pythonAutomation')
bucket_manager = BucketManager(session)

@click.group()
def cli():
    """Deploys websites to AWS."""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an s3 bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 bucket."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)

    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to Bucket."""
    bucket_manager.sync(pathname, bucket)


if __name__ == '__main__':
    cli()
