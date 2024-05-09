from flask import Flask, render_template, request
import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
import etcd3
import random
import string

app = Flask(__name__)

# Define the address of your etcd cluster
etcd_host = 'localhost'
etcd_port = 2379
etcd = etcd3.client(host=etcd_host, port=etcd_port)

# Function to generate a random key
def generate_random_key(length=10):
    return '/'.join(''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(3))

# Function to generate a random value
def generate_random_value(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to list all keys with their metadata
def list_keys():
    try:
        keys_with_metadata = etcd.get_all()
        return keys_with_metadata if keys_with_metadata else None
    except Exception as e:
        print(f"Error occurred while listing keys: {e}")
        return None

# Function to get the value associated with a specific key
def get_value(key):
    value, _ = etcd.get(key)
    return value.decode() if value else None

# Function to put a new key-value pair into etcd
def put_key_value(key, value):
    if get_value(key) is None:
        etcd.put(key, value)
        return True  # Successfully added
    else:
        return False  # Key already exists

# Function to delete a key-value pair from etcd
def delete_key(key):
    val = get_value(key)
    if val is not None:
        etcd.delete(key)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        if request.form['submit_button'] == 'Put':
            key = request.form['key']
            value = request.form['value']
            if put_key_value(key, value):
                message = f"Key '{key}' with value '{value}' successfully added."
            else:
                message = f"Key '{key}' already exists."
        elif request.form['submit_button'] == 'Get':
            key = request.form['key']
            value = get_value(key)
            if value is not None:
                message = f"Value for key '{key}': {value}"
            else:
                message = "No such key found. The specified key does not exist."
        elif request.form['submit_button'] == 'Delete':
            key = request.form['key']
            value = get_value(key)
            if value is not None:
                delete_key(key)
                message = f"Key '{key}' successfully deleted."
            else:
                message = "No such key found. The specified key does not exist."
        elif request.form['submit_button'] == 'List':
            keys_with_metadata = list_keys()
            if keys_with_metadata:
                message = "\n"
                for key, metadata in keys_with_metadata:
                    key_str = metadata.key.decode('utf-8')
                    value_str = key.decode('utf-8')
                    message += f"\n{key_str}:{value_str},"
            else:
                message = "There are no key-value pairs."
            
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
