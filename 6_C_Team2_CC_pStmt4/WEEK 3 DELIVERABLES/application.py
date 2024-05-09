import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
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
        value, _= etcd.get(key)
        return value

    # Function to put a new key-value pair into etcd
    def put_key_value(key, value):
        etcd.put(key, value)
        print(f"\nAdded new key-value pair to etcd: {key} -> {value}")

    # Function to delete a key-value pair from etcd
    def delete_key(key):
        val = get_value(key)
        if val != None:
            etcd.delete(key)
            print(f"\nDeleted key-value pair from etcd with key: {key}")
        else:
            print("\nNo such key found. The specified key does not exist.")
    # Example usage
    if __name__ == "__main__":
        while True:
            print("\nOptions:")
            print("1. Put")
            print("2. Get")
            print("3. Delete")
            print("4. List")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                key1 = input("Enter key: ")
                value = input("Enter value: ")
                keys = list_keys()
                flag = 0 
                for key, metadata in keys:
                    key_str = metadata.key.decode('utf-8')
                    if key1 == key_str:
                        print("\nKey already exists")
                        flag = 1
                        break
                if flag == 0:
                    put_key_value(key1, value)
                        
            elif choice == '2':
                key = input("Enter key: ")
                value = get_value(key)
                if value != None:
                    print(f"Value for key '{key}': {value}")
                else:
                    print("\nNo such key found. The specified key does not exist.")
            elif choice == '3':
                key = input("Enter key to delete: ")
                delete_key(key)
            elif choice == '4':
                keys = list_keys()
                if keys != []:
                    print("\nAll keys in etcd:")
                    for val, metadata in keys:
                        key_str = metadata.key.decode('utf-8')  
                        value_str = val.decode('utf-8')  
                        print(f"Key: {key_str}, Value: {value_str}")
                else:
                    print("\nNo key-values pairs present")
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

except etcd3.exceptions.ConnectionFailedError:
    print("Connection error: Unable to connect to etcd cluster.")
except Exception as e:
    print(f"An error occurred: {e}")
