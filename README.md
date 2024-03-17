# Overview
![pythonapp](https://github.com/lamht/udacity-azure-devops-project02/docs/actions/workflows/pythonapp.yml/badge.svg)
The python web app project make prediction.

## Project Plan
A link to a spreadsheet that includes the original and final project plan
https://github.com/lamht/udacity-azure-devops-project02/blob/main/lamht%20Project%20Management.xlsx

## Instructions
When the commit on GitHub repos, Auzre Pipeline will trigger build, test, and deploy to Azure Web app service.
![Alt text](/images/devops-diagram.png?raw=true "DevOps Diagram")


* Project running on Azure App Service


* Project cloned into Azure Cloud Shell
![Alt text](/images/Project_cloned_into_Azure_Cloud_Shell.png?raw=true "DevOps Diagram")



* Passing tests that are displayed after running the `make all` command from the `Makefile`


* Output of a test run
![Alt text](/images/gitaction-test-pass.png?raw=true "DevOps Diagram")

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
![Alt text](/images/azure-build-deployed-pipeline.png?raw=true "DevOps Diagram")

* Running Azure App Service from Azure Pipelines automatic deployment


* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

Next we can user docker image to deployed app.

## Demo 
https://youtu.be/sO_Um1EROUQ


