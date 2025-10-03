Access Denied: AWS IAM Access Analyzer keeps those...
Select a challenge below to get started.

Solve using:

Open AWS Console
>_AWS_CLI
Restart Challenge

Your challenge is ready!
All the best, and remember to have fun!


Overview
Once upon a time, there was a company called "Cloud Kingdom" that had been using Amazon Web Services (AWS) to host their applications and services for several years. They had stringent guidelines that access to their S3 buckets should be only from the zone of trust (ie. AWS Account in which bucket was created). However, as the company grew, they started seeing malicious access to their S3 buckets, which is a huge security risk.

One day, the Cloud Kingdom security team came across AWS IAM Access Analyzer. This tool provided them with the ability to analyze their access policies and check for any potential security risks or violations. With IAM Access Analyzer, they could find and remove any policy statement(s) that allow access to their resources from outside the zone of trust (AWS Account).

They quickly set up IAM Access Analyzer and ran a scan on their entire AWS environment. The results were eye-opening; they discovered that they had several findings including access to the resources from outside the zone of trust (their own AWS Account).

Now as a Cloud consultant at "Cloud Kingdom", you are requested to quickly identify and fix the issue reported for one of their S3 bucket, which is greatly affecting their overall security posture.

Task 1: Identify finding ID of the overly permissive access
Possible Points
24
Clue Penalty
0
Points Available
24
Check my progress

Task and Clues
Submit Answer
Background
You should start looking for any overly permissive access or improperly configured policies that could potentially allow unauthorized access to the JAM challenge bucket. IAM Access Analyzer is a powerful tool for identifying and addressing security vulnerabilities in your AWS environment. By analyzing resource policies, access control lists (ACLs), and other permissions configurations, IAM Access Analyzer can help you to identify potential security risks and ensure that your resources are properly secured. Specifically for the JAM Challenge bucket, IAM Access Analyzer can assist in detecting and addressing any misconfigurations or overly permissive access policies that may be leaving the bucket open to unauthorized access.

Your Task
Your task is to look though the active findings in the IAM Access Analyzer which lists JAM challenge S3 buckets as the resource and identify the Finding ID.

Getting Started
Wait until the Analyzer creation process is complete, and then inspect the active findings for the JAM challenge bucket. Look through the active findings which lists JAM challenge S3 bucket as the resource.

Note: Ensure that you have logged into the right AWS region in which this challenge is deployed. You may find the challenge region under Output Properties -> JamRegion

Inventory
AWS IAM Access Analyzer has been already created for you. You can find the JAM challenge S3 bucket in the Output Properties section.

Services you should use
AWS IAM, IAM Access Analyzer, Amazon S3

Task Validation
The task will complete once you input the correct Finding ID (listed against the JAM challenge bucket) in the response field. eg: A sample Finding ID would look like : 9d1bbab7-cfbe-41fe-8fb3-1a4818b2f273

Note : You don't have to fix any finding in this task. You would be fixing the finding as part of next task.

Como resolver (via Console)

Vá no IAM → Access Analyzer.

Localize o analyzer já criado (provavelmente com nome tipo jam-analyzer).

Clique em Findings (Resultados).

Use o filtro Resource type = S3Bucket.

Procure pelo bucket listado nos Output Properties do desafio (JamBucket).

Na linha do resultado, vai aparecer o Finding ID (um UUID no formato xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).

Copie esse ID e insira no campo de resposta do challenge.
