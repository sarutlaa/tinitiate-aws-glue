# Installing Python Libraries and python modules in AWS Glue Environment.

AWS Glue provides several parameters that allow users to customize the Python environment for their ETL jobs. These parameters enable the inclusion of additional Python libraries, custom Python files, and the use of specific installation options for Python packages.

## Method 1. Including Additional Python Modules (--additional-python-modules)
### Description:
The --additional-python-modules parameter in AWS Glue is a powerful tool for customizing the Python environment of your Glue jobs. This parameter enables you to specify additional Python libraries that are not included in the default AWS Glue environment, which can be installed via pip.
### Usage:
When setting up or editing an AWS Glue job through the AWS Management Console, AWS CLI, or SDKs, you can add this parameter to the job's configuration. Upon job execution, AWS Glue will install the specified libraries before starting the job script, ensuring all necessary dependencies are available for use in your script.
### Example of adding python module through AWS Console
To integrate the amazon.ion library into your AWS Glue job, configure the job parameters as shown below:
```
--additional-python-modules "amazon.ion==0.5.0"
```
#### Implementation Details in AWS Glue Job:
If you need to utilize external libraries such as amazon.ion in your AWS Glue script, they must be specified in the Job Details section when setting up or running the script. Since amazon.ion is not included by default in AWS Glue, it needs to be explicitly added. Here’s how you can do this:

1. Navigate to the Job Details page in the AWS Glue console.
2. Go to Advanced Details and In the job parameters section, add --additional-python-modules "amazon.ion==0.5.0".
3. Save the changes to the job configuration.
4. Execute the job. During runtime, the specified amazon.ion library will be automatically imported and ready to use.
5. Below is an example screenshot illustrating where to enter the library details:

   <img width="934" alt="External_Libraries_1" src="https://github.com/sarutlaa/tinitiate-aws-glue/assets/141533429/0f167df0-c742-4fe7-bfaa-06326db1457c">




