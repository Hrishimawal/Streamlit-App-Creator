# streamlit-app-creator

[TOC]

This is a [Copier](https://copier.readthedocs.io/en/stable/) template that helps you create a minimal Streamlit
application with integrated Azure AD authentication.

## What is it?

This template enables you to quickly create a minimal Streamlit application with integrated Azure AD authentication and
role-based access control using Azure App Configuration.

Features:

- Streamlit app scaffold with modular structure
- Azure AD authentication (Microsoft identity platform)
- Role-based access control, managed via Azure App Configuration
- Example scripts for managing user roles
- Dockerfile and CI/CD pipeline for easy deployment to Azure Web App
- Ready-to-customize user interface and content

## Quickstart

### What you need

- [Python 3.12+](https://www.python.org/downloads/) installed on your local machine

- [Copier](https://copier.readthedocs.io/en/stable/) installed. You can install it using pip:

  ```sh
  pip install copier
  ```

- Access to an Azure subscription with sufficient permissions to create resources

- [Git](https://git-scm.com/) installed for version control

### Setup

1. Create a GitLab project that will contain the stream-app-creator project repository:
1. In this GitLab repository you created in the previous step:
   - [Use copier](https://copier.readthedocs.io/en/stable/) to set up the git repo starting from this template. For
     example:

     ```sh
     copier copy ssh://git@ssh.git.eon-cds.de:22222/repos/customersolutionssandbox/templates/copier/streamlit-app-creator/src.git .
     ```

     If you've already generated answers from another Copier template (e.g., `azure-resource-creator`), you can reuse
     those values:

     ```sh
     copier copy --data-file <other-template-directory>/.copier-answers.yml \
        ssh://git@ssh.git.eon-cds.de:22222/repos/customersolutionssandbox/templates/copier/streamlit-app-creator/src.git .
     ```

     This approach is useful when:

     - You want to maintain consistency across related templates
     - You've already defined project parameters in another template

     **Note:** The data file should contain YAML key-value pairs matching the template's expected variables (e.g.,
     `web_app_name`, `azure_subscription_id`, etc.). Any missing values will still be prompted interactively.

   - Fill in the prompted values.

   - Push the repository to GitLab. The GitLab CI/CD pipeline will automatically deploy the basic setup.

## Notes for contributors

### Development environment setup

- Create and activate a virtual Python environment with the Python version, e.g., specified in `.python-version`.
- Use pip to install and update `pip`, `wheel`, `setuptools`, and `pre-commit`.
- Use pip to install the requirements in `requirements.txt`.
- Install the git pre-commit hook.

### How to run the tests

Use `pytest` to run the tests:

```sh
python -m pytest test
```

### Infrastructure, secrets and environment variables used in the tests

To run certain operations, set the following environment variables:

- `AZURE_CLIENT_ID`: The Client ID that is used for resource update and/or deployment
- `AZURE_CLIENT_SECRET`: The Client Secret that is used for resource update and/or deployment
- `AZURE_TENANT_ID`: The Tenant ID that is used for resource update and/or deployment
