from azure.storage.blob import BlockBlobService, PublicAccess


block_blob_service = BlockBlobService(account_name="ideahacksstorage", account_key="LHpyE+1NtOE9vSXqpFz6V1oWqYdEUCqsTkgngIEIoDbvR+Myf8XuWvy7dJQTEb5uKeSBEzG+aIfEw/R6zdP7ag==")
block_blob_service.create_blob_from_path("test", "test.jpeg", "/Users/johndang/git/SmartLock/testpics/test.jpeg")

print("\nList blobs in the container")
generator = block_blob_service.list_blobs("test")
for blob in generator:
    print("\t Blob name: " + blob.name)


print(block_blob_service.make_blob_url('test', 'test.jpeg'))