import requests
import pandas as pd


def nft(token, cursor):
    query = {"size": 1000}
    if cursor != "":
        query = {"cursor": cursor, "size": 1000}
    my_headers = {"Content-Type": "application/json", "x-chain-id": "8217"}
    response = requests.get(
        "https://th-api.klaytnapi.com/v2/contract/nft/" + token + "/token",
        params=query,
        auth=('AccessKey ID', 'Secret AccessKey'),
        headers=my_headers
    )
    # print(response)
    response_json = response.json()
    # print(response_json.get("cursor"))
    return response_json


def printalltoken(token, name):
    tmp_json = nft(token, "")
    json = tmp_json.get("items")
    cursor = tmp_json.get("cursor")
    print(type(json))
    while cursor != "":
        tmp_json = nft(token, cursor)
        json += (tmp_json.get("items"))
        cursor = tmp_json.get("cursor")
    print(len(json))
    df = pd.DataFrame(json)
    writer = pd.ExcelWriter(name + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()


# print(json)
# token = "0x4007cb1fb9d1158add29cf5d88568dd44a1f516e"
# name = "treasures_club"
token = input("Enter Token:")
name = input("Enter Filename:")
printalltoken(token, name)
