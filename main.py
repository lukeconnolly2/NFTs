import requests as r
import json
import pandas as pd

def pingapi(address):
    url = 'https://graphql.icy.tools/graphql'
    header = {'x-api-key': '91a9fda75c224efaa7c44d6a9fff610c',
              'content-type': 'application/json'
              }

    query = """
      query CollectionStats($address: String!) {
    contract(address: $address) {
      ... on ERC721Contract {
        stats {
          floor
          volume
        }
        name
        attributes {
          name
          value
        }
      }
    }
  }
  
       """

    address = {"address": address}
    return json.loads(r.post(url, headers=header, json={'query': query, 'variables': address}).text)["data"]["contract"]


def main():

    address = input("Enter address: ")

    res_obj = pingapi(address)

    print(f"Name: {res_obj['name']}")
    print(f'Floor: {res_obj["stats"]["floor"]}')
    print(f'Volume: {res_obj["stats"]["volume"]}')
    main()
    return

if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

