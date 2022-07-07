# Auto delete tagged resources in Azure using Azure DevOps pipeline

### Prerequisites:

- A docker image with the needed tools. https://github.com/savaklin/pipeline_docker_image/blob/main/Dockerfile
- A service connection with owner or contributor over your devtest management group

The script assumes you have a devtest management group with all your devtest subscriptions in it. It will loop over each sub and query for the ‘usage’ tag with either ‘on_demand’ or ‘weekdays’ values. The ‘on_demand’ tagged resource groups will be deleted every day when the pipeline runs while the resource groups tagged with ‘weekdays’ will only be deleted on Fridays. On line 20, after the ‘-n’  you’ll need to change it to the name or id of your management group.

It's up to you how you set these tags, but management group policy on resource group creation seems to work quite well.
