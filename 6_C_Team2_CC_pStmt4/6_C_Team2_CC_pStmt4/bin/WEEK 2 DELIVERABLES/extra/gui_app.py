from flask import Flask, render_template, request, redirect, url_for
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

# Function to delete a key-value pair from etcd
def delete_key(key):
    val = get_value(key)
    if val != None:
        etcd.delete(key)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        if request.form['submit_button'] == 'Put':
            key = request.form['key']
            value = request.form['value']
            put_key_value(key, value)
            message = f"Key '{key}' with value '{value}' successfully added."
        elif request.form['submit_button'] == 'Get':
            key = request.form['key']
            value = get_value(key)
            if value != None:
                message = f"Value for key '{key}': {value}"
            else:
                message = "No such key found. The specified key does not exist."
        elif request.form['submit_button'] == 'Delete':
            key = request.form['key']
            value = get_value(key)
            if value != None:
                delete_key(key)
                message = f"Key '{key}' successfully deleted."
            else:
                message = "No such key found. The specified key does not exist."
        elif request.form['submit_button'] == 'List':
            keys = list_keys()
            message = f"All keys: {str(keys)}"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
