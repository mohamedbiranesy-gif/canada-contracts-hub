import urllib.request, json, csv, os, sys
os.makedirs('data/incoming/jules/downloads/ca_municipal_purchase_orders_open_data', exist_ok=True)
def dl_socrata(domain, id, name):
    url = f"https://{domain}/api/views/{id}/rows.csv?accessType=DOWNLOAD"
    path = f"data/incoming/jules/downloads/ca_municipal_purchase_orders_open_data/{domain}_{id}.csv"
    print(f"Downloading {name} from {domain}...")
    try:
        urllib.request.urlretrieve(url, path)
        print("Success")
    except Exception as e:
        print(f"Failed: {e}")

# Edmonton y9rm-5xha (Purchase Orders Over $10,000)
dl_socrata("data.edmonton.ca", "y9rm-5xha", "Purchase Orders Over $10,000")
