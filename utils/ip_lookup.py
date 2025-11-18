import requests

def lookup_ip(ip_address):
    url = f"https://ipapi.co/{ip_address}/json/"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if "error" in data:
            return {"error": "Invalid IP address or lookup failed"}

        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country_name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "timezone": data.get("timezone"),
            "org": data.get("org"),
        }

    except Exception as e:
        return {"error": str(e)}