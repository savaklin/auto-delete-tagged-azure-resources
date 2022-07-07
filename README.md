# Auto delete tagged resources in Azure using Azure DevOps pipeline

Prerequisites:

- A pipeline docker image that can be found here. https://github.com/savaklin/pipeline_docker_image/blob/main/Dockerfile
- A service connection with owner or contributor over your devtest management group

The script assumes you have a devtest management group with all your devtest subscriptions in it. It will loop over each sub and query for the ‘usage’ tag with either ‘on_demand’ or ‘weekdays’ values. The ‘on_demand’ tagged resource groups will be deleted every day when the pipeline runs while the resource groups tagged with ‘weekdays’ will only be deleted on Fridays. On line 20, after the ‘-n’  you’ll need to change it to the name of your management group.

It's up to you how you set these tags but management group policy seems to work quite well.
