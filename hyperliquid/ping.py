import requests

def ping():
	try:
		response = requests.post(
			"https://api.hyperliquid.xyz/info",
			json={"type": "ping"}
		)
		print("Status Code:", response.status_code)
		print("Response:", response.json())
	except Exception as e:
		print("Error:", e)

if __name__ == "__main__":
	ping()
