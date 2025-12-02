# import requests

# def lookup_ip(ip_address):
#     url = f"https://ipapi.co/{ip_address}/json/"
    
#     try:
#         response = requests.get(url, timeout=5)
#         data = response.json()

#         if "error" in data:
#             return {"error": "Invalid IP address or lookup failed"}

#         return {
#             "ip": data.get("ip"),
#             "city": data.get("city"),
#             "region": data.get("region"),
#             "country": data.get("country_name"),
#             "latitude": data.get("latitude"),
#             "longitude": data.get("longitude"),
#             "timezone": data.get("timezone"),
#             "org": data.get("org"),
#         }

#     except Exception as e:
#         return {"error": str(e)}


# -------------------------------------------------
# Your second block starts here (separated properly)
# -------------------------------------------------

import requests

def lookup_ip(ip_address):
    """
    Lookup IP address information using free IP geolocation APIs with fallbacks
    """
    
    # Try ipapi.co first (more reliable, 1000 requests/day free)
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/', timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if there's an error in the response
            if 'error' not in data:
                return {
                    'ip': ip_address,
                    'country': data.get('country_name', 'Unknown'),
                    'region': data.get('region', 'Unknown'),
                    'city': data.get('city', 'Unknown'),
                    'isp': data.get('org', 'Unknown'),
                    'timezone': data.get('timezone', 'Unknown'),
                    'lat': data.get('latitude', 'Unknown'),
                    'lon': data.get('longitude', 'Unknown')
                }
    except Exception as e:
        print(f"ipapi.co failed: {e}")
    
    # Fallback to ip-api.com
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}', timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('status') == 'success':
                return {
                    'ip': ip_address,
                    'country': data.get('country', 'Unknown'),
                    'region': data.get('regionName', 'Unknown'),
                    'city': data.get('city', 'Unknown'),
                    'isp': data.get('isp', 'Unknown'),
                    'timezone': data.get('timezone', 'Unknown'),
                    'lat': data.get('lat', 'Unknown'),
                    'lon': data.get('lon', 'Unknown')
                }
    except Exception as e:
        print(f"ip-api.com failed: {e}")
    
    # Fallback to ipinfo.io
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json', timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            # Split location into lat/lon
            loc = data.get('loc', ',').split(',')
            lat = loc[0] if len(loc) > 0 else 'Unknown'
            lon = loc[1] if len(loc) > 1 else 'Unknown'
            
            return {
                'ip': ip_address,
                'country': data.get('country', 'Unknown'),
                'region': data.get('region', 'Unknown'),
                'city': data.get('city', 'Unknown'),
                'isp': data.get('org', 'Unknown'),
                'timezone': data.get('timezone', 'Unknown'),
                'lat': lat,
                'lon': lon
            }
    except Exception as e:
        print(f"ipinfo.io failed: {e}")
    
    # If all APIs fail
    print("All IP lookup APIs failed")
    return None
