# Overview of AWS Lambda Functions

The individual functions you write and deploy within the AWS Lambda service. Each Lambda function is a piece of code that performs a specific task and is executed in response to an event. 

## Core Concepts of Lambda Functions
* Triggers: Events that invoke your function. Examples include changes in data within an S3 bucket, updates to a DynamoDB table, HTTP requests via API Gateway, and schedule events from CloudWatch.
* Function Code: The code you write to handle events. It can include libraries and dependencies.
* Runtime: The execution environment that runs your function. You select a runtime that corresponds to your choice of programming language.
* Resources: Configuration settings that you provide, such as memory and execution time.
* IAM Role: The IAM policy that grants your function permission to access AWS resources

## How Lambda Function works internally?
1. Uploading Code:
  Developers upload their function code to AWS Lambda. This code is what will be executed when the function is triggered. The code must be written in one of the programming languages supported by Lambda, such as Python or Node.js.

3. ARN Generation:
  When you upload your code, AWS Lambda automatically generates an Amazon Resource Name (ARN). This ARN is a unique identifier for your Lambda function, which you will use to reference and invoke your function.

<p align="center">
  <img src="images/Lambda_1.png" alt="Lambda Function" width="600"/>
</p>

4. Invoking the Function:
    Your Lambda function can be triggered (invoked) in various ways:
    
    - Directly through the AWS Management Console or using the AWS CLI.
    - Automatically by AWS services, such as when a new file is uploaded to S3 or a new record is added to a DynamoDB table.
  
4. Load Balancing:
  AWS Lambda uses internal load balancing mechanisms to efficiently distribute incoming function calls across its infrastructure. This ensures that each function invocation is processed quickly and efficiently.

5. Execution:
  Lambda functions are executed inside a secure, isolated environment. This environment is automatically managed by AWS and runs on a fleet of EC2 instances that are optimized for Lambda. Developers do not need to worry about the underlying EC2 instances; AWS handles the scaling and management automatically.


<p align="center">
  <img src="images/Lambda_2.png" alt="Lambda Function Internal Working" width="600"/>
</p>

### Key Points to Remember
- Isolation: Each function runs in its own isolated environment, ensuring that functions do not interfere with each other.
- Scalability: AWS Lambda automatically scales by adjusting the number of EC2 instances based on the number of incoming requests. This means your function can handle increases in workload without any manual intervention.
- Pay for Use: You only pay for the compute time you consume, making AWS Lambda a cost-effective solution for running code that responds to events.


