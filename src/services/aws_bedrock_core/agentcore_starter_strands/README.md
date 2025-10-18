# Sample description for agentcore_starter_strands

This directory contains starter strands for the AgentCore framework, designed to help you quickly set up and run basic
agents.
These strands provide foundational functionality and can be easily customized to fit your specific use cases.

# Prerequisites

- Python 3.11 or higher
- Installed packages:
    - strands-core==1.12.0
    - bedrock-agentcore==0.1.7
    - bedrock-agentcore-starter-toolkit>=0.1.21
    - boto3==1.40.52
- Installed `AWS CLI` version 2.0 or later
- Create `requirements.txt` file with the following content:
    ```
    strands-core==1.12.0
    bedrock-agentcore==0.1.7
    bedrock-agentcore-starter-toolkit>=0.1.21
    boto3==1.40.52
    ```
- Iam user with permissions to create and manage AWS resources:
  - permission list for starter kit https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html#runtime-permissions-starter-toolkit
- Ideally execution role with permissions to access Bedrock models and other AWS services
  - permission list for execution role https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html#runtime-permissions-execution

# Configure and deploy the agent

1. Activate your Python environment:

    ```bash
    source <your-env>/bin/activate
    ```
2. `Cd` to folder `src/services/aws_bedrock_core/agentcore_starter_strands`
3. Run command `agentcore configure -e agentcore_starter_strands.py` Which will ask you to input the following information:
    - Agent name - for example `first_agent_name`
    - Path to requirements file - for example `requirements.txt`
    - Execution role
    - ECR Repository
    - Authorization Configuration
    - Requested Header
    - Configuration of memory
4. Run command `agentcore launch`