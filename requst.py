import requests

# URL file CSV
url = "https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv"

# Nama file yang akan disimpan
filename = "customers.csv"

# Mendownload file
response = requests.get(url)

# Menyimpan file CSV
with open(filename, 'wb') as file:
    file.write(response.content)

print(f"File {filename} telah berhasil diunduh.")
