# Amazon S3 (Simple Storage Service) Overview

## Overview
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Organizations of all sizes can use S3 to store and protect any amount of data for a range of use cases.

## Key Points about S3
- **Scalable**: Automatically scales to handle vast amounts of data without any intervention.
- **Durable**: Designed for 99.999999999% (11 9's) of data durability.
- **Available**: Provides high availability and fault tolerance.
- **Secure**: Offers robust security features to control access and protect data.

## How S3 is Represented
Amazon S3 is represented by:
- **Buckets**: Containers for storing objects.
- **Objects**: Individual data files stored in buckets.

  Sample Bucket path :
  ```text
  s3://ti-author-data/customer-billing/
  ```

## S3 Use Cases
- **Backup and Restore**: Securely back up data and quickly restore it when needed.
- **Archive**: Store data long-term for compliance and regulatory needs.
- **Content Storage and Distribution**: Host static websites and distribute content.
- **Data Lakes and Big Data Analytics**: Store vast amounts of data for analytics and machine learning.

## S3 Buckets
- **Description**: A bucket is a logical container in S3 where you store data (objects).
- **Naming Conventions**:
  - Must be unique across all of AWS.
  - Can be between 3 and 63 characters long.
  - Can contain lowercase letters, numbers, hyphens (-), and periods (.).

## S3 Objects
- **Description**: The fundamental entities stored in S3, which consist of data and metadata.
- **Details**:
  - Each object is identified by a unique key within a bucket.
  - Can range in size from a few bytes to 5 terabytes.

## S3 Security
- **Access Control**: Managed through IAM policies, bucket policies, and access control lists (ACLs).
- **Encryption**:
  - **Server-Side Encryption (SSE)**: Encrypts data at rest.
  - **Client-Side Encryption**: Data is encrypted before sending to S3.

## Bucket Policies
- **Description**: JSON-based policies used to grant or restrict permissions for an S3 bucket and the objects within it.
- **Example**: Allowing public read access to a bucket:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": "*",
        "Action": ["s3:GetObject"],
        "Resource": ["arn:aws:s3:::example-bucket/*"]
      }
    ]
  }

## Bucket Versioning
- **Description**: Keeps multiple versions of an object in the same bucket.
- **Uses:**
  - Protects against accidental deletions and overwrites.
  - Enables easy recovery of previous versions of objects.
## Storage Classes
Amazon S3 offers different storage classes for cost-efficient storage of your data:

- S3 Standard: General-purpose storage for frequently accessed data.
- S3 Intelligent-Tiering: Optimizes costs by automatically moving data to the most cost-effective access tier.
- S3 Standard-IA (Infrequent Access): For data that is accessed less frequently but requires rapid access when needed.
- S3 One Zone-IA: Lower-cost option for infrequently accessed data that doesn't require multiple availability zone resilience.
- S3 Glacier: Low-cost storage for archival data with retrieval times ranging from minutes to hours.
- S3 Glacier Deep Archive: Lowest-cost storage for data that is rarely accessed, with retrieval times of 12 hours or more.
