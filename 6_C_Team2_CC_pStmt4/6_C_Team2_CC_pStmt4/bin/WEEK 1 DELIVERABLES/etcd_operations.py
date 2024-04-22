import etcd3
import random
import string

# Define the address of your etcd cluster
etcd_host = 'localhost'
etcd_port = 2379

try:
    # Connect to the etcd cluster
    etcd = etcd3.client(host=etcd_host, port=etcd_port)

    # Function to generate a random key
    def generate_random_key(length=10):
        return '/'.join(''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(3))

    # Function to generate a random value
    def generate_random_value(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    # Function to list all keys
    def list_keys():
        keys = list(etcd.get_all())
        return keys

    # Function to get the value associated with a specific key
    def get_value(key):
        value, _ = etcd.get(key)
        return value

    # Function to put a new key-value pair into etcd
    def put_key_value(key, value):
        etcd.put(key, value)
        print(f"\nAdded new key-value pair to etcd: {key} -> {value}")

    # Example usage
    if __name__ == "__main__":
        # Listing all keys before adding a new pair
        print("All keys in etcd before adding new pair:")
        for key in list_keys():
            print(key)

        # Generating a random key and value
        random_key = generate_random_key()
        random_value = generate_random_value()

        # Putting the random key-value pair into etcd
        put_key_value(random_key, random_value)

        # Listing all keys after adding the new pair
        print("\nAll keys in etcd after adding new pair:")
        for key in list_keys():
            print(key)

except Exception as e:
    print("An error occurred while connecting to etcd:", e)
