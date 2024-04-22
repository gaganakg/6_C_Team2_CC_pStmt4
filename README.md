# 6_C_Team2_CC_pStmt4
#Cloud Computing ( UE21CS351 ) Project 2024 _Problem statement 2: Building a Distributed Key-Value Store with etcd

Etcd Key-Value Store
This project implements a simple key-value store using etcd, a distributed key-value store that provides a reliable way to store data across a cluster of machines. This implementation allows users to perform basic operations such as putting new key-value pairs, retrieving values by key, deleting key-value pairs, and listing all keys present in the etcd cluster.

Project Setup
Installation
Ensure you have Python installed on your system. You can install the required packages using pip:

Copy code
pip install python-etcd3
Etcd Installation
Before running the program, make sure you have etcd installed and running. You can install etcd by following the instructions provided here.

Functionalities
Put: Allows users to add new key-value pairs to the etcd cluster.
Get: Retrieves the value associated with a specified key from the etcd cluster.
Delete: Deletes a key-value pair from the etcd cluster.
List: Lists all keys present in the etcd cluster.
Exit: Exits the program.
Instructions to Run
Clone the repository or download the etcd_key_value_store.py file.
Modify the etcd_host and etcd_port variables if necessary.
Run the script using the following command:
Copy code
python etcd_key_value_store.py
Follow the on-screen instructions to perform desired operations.
Example Usage
mathematica
Copy code
Options:
1. Put
2. Get
3. Delete
4. List
5. Exit

Enter your choice: 1
Enter key: example_key
Enter value: example_value

Added new key-value pair to etcd: example_key -> example_value

Options:
1. Put
2. Get
3. Delete
4. List
5. Exit

Enter your choice: 2
Enter key: example_key
Value for key 'example_key': example_value

Options:
1. Put
2. Get
3. Delete
4. List
5. Exit

Enter your choice: 3
Enter key to delete: example_key

Deleted key-value pair from etcd with key: example_key

Options:
1. Put
2. Get
3. Delete
4. List
5. Exit

Enter your choice: 4
All keys in etcd:
...

Options:
1. Put
2. Get
3. Delete
4. List
5. Exit

Enter your choice: 5
Exiting...

Notes
Ensure that your etcd cluster is running and accessible from the specified host and port.
Handle errors gracefully if the connection to the etcd cluster fails.
