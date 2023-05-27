<h1>AWS ECR Untagged Image Cleaner Lambda Function</h1>

<p>This repository contains an AWS Lambda function written in Python that deletes untagged Docker images from AWS ECR repositories.</p>

<h2>Overview</h2>

<p>Docker images that are untagged can often pile up in ECR, taking up valuable space. This AWS Lambda function helps by automatically deleting these untagged images.</p>

<h2>Requirements</h2>

<ul>
    <li>Python 3.x</li>
    <li>AWS SDK for Python (Boto3)</li>
    <li>AWS CLI</li>
    <li>AWS Account with configured access key and secret</li>
</ul>

<h2>Setup &amp; Deployment</h2>

<ol>
    <li>Clone this repository:
        <pre><code>git clone https://github.com/bgrhnshn/aws-ecr-untagged-image-cleaner.git</code></pre>
    </li>
    <li>Install the AWS CLI and configure it with your AWS account details. <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html">AWS CLI Configuration Documentation</a></li>
    <li>Deploy the function to AWS Lambda. You can use the AWS Console, AWS CLI, or any other tool like Serverless framework. <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-upload.html">AWS Lambda Deployment Documentation</a></li>
</ol>

<h2>Usage</h2>

<p>The function is triggered based on the event source defined in AWS Lambda. It can be set to run on a schedule using Amazon EventBridge or can be triggered manually.</p>