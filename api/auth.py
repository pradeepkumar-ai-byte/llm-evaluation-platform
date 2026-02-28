from fastapi import Header, HTTPException


API_KEYS = {
    "admin_key_123": "admin"
}


def validate_api_key(x_api_key: str = Header(...)):

    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return API_KEYS[x_api_key]