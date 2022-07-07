from az.cli import az
from termcolor import colored
import datetime

def delete(resource_id):
    print(f"\nDeleting {resource_id.split('/')[-1]}")
    result = az(f"resource delete --id {resource_id}")
    print(colored("Deleted successfully", "green") if result[0] == 0 else f"{colored('Deletion unsuccessful', 'red')} log: {result[2]}")

def get_resource(tag):
    return az(f"group list --tag usage={tag} --query [].{{resourceId:id,name:name}}")[1]

def add_to_list(items):
    for each_item in items:
        if each_item['name'][:3] == "MC_":
            continue
        resources_to_be_deleted.append(each_item)


devtest_subscription_list = [{"name":sub['displayName'], "id":sub['name']} for sub in az("account management-group subscription show-sub-under-mg -n DevTest-MG" )[1]]
resources_to_be_deleted = []

for each_sub in devtest_subscription_list:
    az(f"account set --subscription {each_sub['id']}")

    add_to_list(get_resource("on_demand"))

    if datetime.datetime.now().isoweekday() == 5:
        add_to_list(get_resource("weekdays"))

for each_item in resources_to_be_deleted:
    delete(each_item['resourceId'])