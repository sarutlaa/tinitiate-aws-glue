# AWS Lambda Functions

The individual functions you write and deploy within the AWS Lambda service. Each Lambda function is a piece of code that performs a specific task and is executed in response to an event. 

## Core Concepts of Lambda Functions
* Triggers: Events that invoke your function. Examples include changes in data within an S3 bucket, updates to a DynamoDB table, HTTP requests via API Gateway, and schedule events from CloudWatch.
* Function Code: The code you write to handle events. It can include libraries and dependencies.
* Runtime: The execution environment that runs your function. You select a runtime that corresponds to your choice of programming language.
* Resources: Configuration settings that you provide, such as memory and execution time.
* IAM Role: The IAM policy that grants your function permission to access AWS resources

## How Lambda Function works internally?
1. Uploading Code:
  Developers upload their function code to AWS Lambda. This code is what will be executed when the function is triggered.
  Supported runtime programming languages  : Python, Node.js, Java, .Net, Ruby, Go or custom runtime language. 

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

## Hands-On Lambda Function Creation in Python

### Step 1: Open AWS Lambda Console
- Navigate to the AWS Management Console.
- Find and select Lambda under Services.

### Step 2: Create a New Lambda Function
- Create Function: Click on the "Create function" button.
    <p align="center">
    <img src="images/Lambda_3.png" alt="Lambda Create Function" width="600"/>
  </p>
- Author from Scratch: Select "Author from scratch".
- Function Configuration:
  - Name: Enter a name for your function, such as HelloWorldPython.
  - Runtime: Select "Python 3.8" (or the latest supported Python version available).
    <p align="center">
    <img src="images/Lambda_4.png" alt="Lambda Function 1" width="600"/>
  </p>
  - Permissions: Expand the "Change default execution role" section.
  - Execution Role: Choose "Create a new role with basic Lambda permissions" or use an existing role if you already have one appropriate for a simple Lambda function.
      <p align="center">
    <img src="images/Lambda_5.png" alt="Lambda Function 2" width="600"/>
  </p>

### Step 3: Write Function Code
- After creating the function, you will be redirected to the function's configuration page.
  <p align="center">
    <img src="images/Lambda_6.png" alt="Lambda Function 3" width="600"/>
  </p>
- In the "Function code" section, find the online code editor.
- Replace the existing code with the following simple "Welcome to Tinitiate, AWS Training!" Python code:

  ```python
  def lambda_handler(event, context):
    print("Welcome to Tinitiate, AWS Training!")
    return {
        'statusCode': 200,
        'body': 'Welcome to Tinitiate, AWS Training'
    }
  ```
  <p align="center">
    <img src="images/Lambda_7.png" alt="Lambda Function 4" width="600"/>
  </p>

### Step 4: Save and Test the Function
- Save: Click the "Deploy" button to save your function code.
- Test:
  - Click on the "Test" button at the top of the page.
  - Create a new test event: In the dialog that appears, you can leave the default event template. Name your test event (e.g., testEvent) and click "Create".
    <p align="center">
    <img src="images/Lambda_8.png" alt="Lambda Function 4" width="600"/>
  </p>
  - Click the "Test" button again to execute the function with the test event you created.
               
   
### Step 5: Review Execution Result
- After testing, you will see the execution result in the console. This includes the execution log and return value from the function. The logs will display "Hello, World!" if executed correctly, and the execution result should show the return statement defined in your function.

 <p align="center">
    <img src="images/Lambda_9.png" alt="Lambda Function 5" width="600"/>
  </p>

### Step 6: Monitor and Logs
You can view detailed logs and monitor the function's execution metrics using AWS CloudWatch, which is directly integrated into the Lambda console under the "Monitor" tab.

 <p align="center">
    <img src="images/Lambda_10.png" alt="Lambda Function 6" width="600"/>
  </p>

   <p align="center">
    <img src="images/Lambda_11.png" alt="Lambda Function 7" width="600"/>
  </p>


## TASK : Similarly implement the same for jave code.


## Lambda Functions: Working with other Languages

When using AWS Lambda, only Python and Node.js have direct support for in-browser code editing. For other supported languages (like Java, Go, C#, Ruby, and PowerShell), you must package and upload your code as a ZIP file.
### 1. Prepare Your Code
* Write Your Code: Develop your Lambda function locally in your chosen language.
* Package Your Code:
    - For compiled languages (like Java or C#), compile your code and package the binaries and any dependencies into a ZIP file.
    - For interpreted languages (like Ruby), package your script files and any dependencies into a ZIP file.
### 2. Create a Lambda Function
* Open AWS Management Console, go to the Lambda section.
* Create Function: Select “Author from scratch”, input your function name, and select the runtime that matches your programming language.
* Set Permissions: Choose an existing IAM role or create a new one that has the necessary permissions for your function.
### 3. Upload Your Function Code
* Navigate to Function Code Section: Choose "Upload from" -> ".zip file".
* Upload Your ZIP File: Upload the ZIP file containing your function and its dependencies.
### 4. Configure Your Function
* Handler Name: Specify the method in your code that Lambda calls to start execution.
  * Example for Java: com.example.MyHandler::handleRequest
  * Example for Ruby: lambda_function.handler
* Environment Variables: Set any necessary environment variables.
### 5. Deploy and Test
* Deploy Your Code: Save and deploy your changes in the Lambda console.
* Test Your Function: Set up a test event and invoke your function to ensure it works correctly.
### 6. Monitoring and Logs
* Use AWS CloudWatch: Monitor the execution and performance of your function through logs and metrics available in CloudWatch.
