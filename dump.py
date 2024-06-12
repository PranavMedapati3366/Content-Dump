# import csv
# import requests
# import json
# def to_csv(data):
#     file = 'output.csv'

# def getData(id):
#     url = f"https://api.allen-live.in/api/v1/learningMaterials/filter/0"
    
#     headers = {
#         'Content-Type':'application/json',
#         'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhVVNzVzhHSTAzZHlRMEFJRlZuOTIiLCJkX3R5cGUiOiJ3ZWIiLCJkaWQiOiJmNjFhMWUzOS1mZWM1LTQwZDEtYTZmMy1hMGJkNDgwMmY0OWQiLCJlX2lkIjoiOTQxOTY3MjU4IiwiZXhwIjoxNzE4MTQyNTA0LCJpYXQiOiIyMDI0LTA2LTExVDAzOjQ4OjI0LjE2ODE1MzA4NVoiLCJpc3MiOiJhdXRoZW50aWNhdGlvbi5hbGxlbi1wcm9kIiwiaXN1IjoiIiwicHQiOiJJTlRFUk5BTF9VU0VSIiwic2lkIjoiOTZlOGM1YTktMWQyNS00MDc0LThiMjgtYWY3YjdjNDZkZTgxIiwidGlkIjoiYVVTc1c4R0kwM2R5UTBBSUZWbjkyIiwidHlwZSI6ImFjY2VzcyIsInVpZCI6Ild4NUlDR3VxM2tkQnpqTkpVdE1GQiJ9.ErhScnrVEPMhKZ0FkSa2buxOXCkEgjTj0iSR8X2InS4'
#     }

#     payload  = json.dumps({
#         "id":id,
#         "page_size":25
#     })

#     response = requests.request("POST",url,headers=headers,data=payload)
#     response  = json.loads(response.text)
#     print(response)

# getData("421cd243-fe4f-446e-91f1-a3fd5e1b463f")


import requests
import json
import csv

url = "https://api.allen-live.in/api/v1/learningMaterials/filter/{page}"

payload_request = json.dumps({
  "type": "RECORDED_CONTENT",
  "center_id":"fa_lDkulak8SgZx4UuC3KFTu",
  "page_size":25

})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhVVNzVzhHSTAzZHlRMEFJRlZuOTIiLCJkX3R5cGUiOiJ3ZWIiLCJkaWQiOiJmNjFhMWUzOS1mZWM1LTQwZDEtYTZmMy1hMGJkNDgwMmY0OWQiLCJlX2lkIjoiOTQxOTY3MjU4IiwiZXhwIjoxNzE4MjM2NzIyLCJpYXQiOiIyMDI0LTA2LTEyVDA1OjU4OjQyLjU1NjQyMzU1MloiLCJpc3MiOiJhdXRoZW50aWNhdGlvbi5hbGxlbi1wcm9kIiwiaXN1IjoiIiwicHQiOiJJTlRFUk5BTF9VU0VSIiwic2lkIjoiOTZlOGM1YTktMWQyNS00MDc0LThiMjgtYWY3YjdjNDZkZTgxIiwidGlkIjoiYVVTc1c4R0kwM2R5UTBBSUZWbjkyIiwidHlwZSI6ImFjY2VzcyIsInVpZCI6Ild4NUlDR3VxM2tkQnpqTkpVdE1GQiJ9.JlR1DEwCTX3ROhLxPKY88IuGkQEPTKX2-3t4tvhe4tk'
}

"""
id_value = payload.get("id", "")
name = payload.get("name", "")
type_value = payload.get("type", "")
sub_type = payload.get("sub_type", "")
center_id = payload.get("center_id", "")
tenant_id = payload.get("tenant_id", "")
stream = ""
subject = ""
class_value = ""
super_topic = ""
topic = ""
sub_topic = ""

# Extracting taxonomy data if available
taxonomies = payload.get("taxonomies", [])
for taxonomy in taxonomies[0]:
    node_type = taxonomy.get("node_type", "")
    name = taxonomy.get("name", "")
    
    if node_type == "STREAM":
        stream = name
    elif node_type == "SUBJECT":
        subject = name
    elif node_type == "CLASS":
        class_value = name
    elif node_type == "SUPER_TOPIC":
        super_topic = name
    elif node_type == "TOPIC":
        topic = name
    elif node_type == "SUBTOPIC":
        sub_topic = name

# Writing to CSV
csv_fields = ["id", "name", "type", "sub_type", "center_id", "tenant_id", "stream", "subject", "class", "super_topic", "topic", "sub_topic"]
csv_data = [id_value, name, type_value, sub_type, center_id, tenant_id, stream, subject, class_value, super_topic, topic, sub_topic]

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_fields)
    writer.writerow(csv_data)

print("Data written to output.csv")

"""


with open('adpl.csv', mode='w', newline='') as file:
    csv_fields = ["id", "name", "type", "sub_type", "center_id", "tenant_id", "stream", "subject", "class",
                  "super_topic", "topic", "sub_topic" , "active","state"]
    writer = csv.writer(file)
    writer.writerow(csv_fields)
    page = 0
    while True:
        response = requests.request("POST", url.format(page = page), headers=headers, data=payload_request)
        page += 1
        # print(response.text)
        print(page)
        res = json.loads(response.text)
        data = res["data"]
        materials = data.get("Materials" ,[])
        if len(materials) == 0:
            break
        for payload in materials:
            id_value = payload.get("id", "")
            name = payload.get("name", "")
            type_value = payload.get("type", "")
            sub_type = payload.get("sub_type", "")
            center_id = payload.get("center_id", "")
            tenant_id = payload.get("tenant_id", "")
            active = payload.get("active" , "")
            state = payload.get("state","")
            stream = ""
            subject = ""
            class_value = ""
            super_topic = ""
            topic = ""
            sub_topic = ""

            # Extracting taxonomy data if available
            taxonomies = payload.get("taxonomies", [])
            for taxonomy in taxonomies[0]:
                node_type = taxonomy.get("node_type", "")
                cur_val = taxonomy.get("name", "")

                if node_type == "STREAM":
                    stream = cur_val
                elif node_type == "SUBJECT":
                    subject = cur_val
                elif node_type == "CLASS":
                    class_value = cur_val
                elif node_type == "SUPER_TOPIC":
                    super_topic = cur_val
                elif node_type == "TOPIC":
                    topic = cur_val
                elif node_type == "SUBTOPIC":
                    sub_topic = cur_val

            # Writing to CSV
            csv_data = [id_value, name, type_value, sub_type, center_id, tenant_id, stream, subject, class_value,
                        super_topic, topic, sub_topic , active,state]
            writer.writerow(csv_data)