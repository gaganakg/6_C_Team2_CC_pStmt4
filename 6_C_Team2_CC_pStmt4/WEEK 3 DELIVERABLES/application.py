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
        """
        Generates a random key of specified length.

        Args:
            length (int): Length of the key to be generated. Default is 10.

        Returns:
            str: Randomly generated key.
        """
        return '/'.join(''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(3))

    # Function to generate a random value
    def generate_random_value(length=10):
        """
        Generates a random value of specified length.

        Args:
            length (int): Length of the value to be generated. Default is 10.

        Returns:
            str: Randomly generated value.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    # Function to list all keys
    def list_keys():
        """
        Lists all keys present in the etcd cluster.

        Returns:
            list: List of keys present in the etcd cluster.
        """
        keys = list(etcd.get_all())
        return keys

    # Function to get the value associated with a specific key
    def get_value(key):
        """
        Retrieves the value associated with the specified key from the etcd cluster.

        Args:
            key (str): The key for which the value is to be retrieved.

        Returns:
            str: Value associated with the specified key, or None if the key does not exist.
        """
        value, _ = etcd.get(key)
        return value

    # Function to put a new key-value pair into etcd
    def put_key_value(key, value):
        """
        Adds a new key-value pair to the etcd cluster.

        Args:
            key (str): The key to be added.
            value (str): The value associated with the key.

        Returns:
            None
        """
        etcd.put(key, value)
        print(f"\nAdded new key-value pair to etcd: {key} -> {value}")

    # Function to delete a key-value pair from etcd
    def delete_key(key):
        """
        Deletes a key-value pair from the etcd cluster.

        Args:
            key (str): The key to be deleted.

        Returns:
            None
        """
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
                key = input("Enter key: ")
                value = input("Enter value: ")
                put_key_value(key, value)
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
                print("\nAll keys in etcd:")
                for key in list_keys():
                    print(key)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

except etcd3.exceptions.ConnectionFailedError:
    print("Connection error: Unable to connect to etcd cluster.")
except Exception as e:
    print(f"An error occurred: {e}")
