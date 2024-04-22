import etcd3

# Define the address of your etcd cluster
etcd_host = 'localhost'
etcd_port = 2379

try:
    # Connect to the etcd cluster
    etcd = etcd3.client(host=etcd_host, port=etcd_port)

    print("Successfully connected to the etcd cluster.")

except Exception as e:
    print("An error occurred while connecting to etcd:", e)
