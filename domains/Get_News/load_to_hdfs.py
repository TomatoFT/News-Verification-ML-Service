from hdfs import InsecureClient


# Connect to HDFS
def get_client():
    client = InsecureClient("http://hadoop:50070", user="root")
    return client


client = get_client()

# Path to the file in HDFS that you want to append to
file_path = "/user/root/my_file.txt"


def create_the_hdfs_file(file_path="/user/root/my_file.txt"):
    # Specify the content to write to the file
    file_content = "Hello, HDFS!"

    # Create the file in HDFS
    client.write(file_path, data=file_content, overwrite=True)

    return file_path


if client.status(file_path):
    print(f"File '{file_path}' created in HDFS.")
else:
    print(f"Failed to create file '{file_path}' in HDFS.")
    file_path = create_the_hdfs_file()

# Append the content to the file in HDFS
def append_data_to_hdfs_file(content, client=client, hdfs_file_path=file_path):
    with client.write(hdfs_file_path, append=True, encoding="utf-8") as file:
        file.write(content)


def read_hdfs_data_file(hdfs_file_path=file_path):
    with client.read(hdfs_file_path, encoding="utf-8") as reader:
        data = reader.read()

    print(data)
    return data


# append_data_to_hdfs_file(client, hdfs_file_path, content)

# Check if the append was successful
