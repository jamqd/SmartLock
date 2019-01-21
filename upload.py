from azure.storage.blob import BlockBlobService, PublicAccess

def upload(fileName, absFilePath):
    """
    Uploads file with fileName as blob to Azure container

    The file should be under the the images folder. The images folder should be in
    the same directory as this file

    The absolute path variable defined below should be changed depending on where
    this repository is stored on the machine 
    """

    # set credentials for uploading blobs to Azure
    block_blob_service = BlockBlobService(account_name="", account_key="")
    
    # the path to the directory containing this file
    absolute_path = "/Users/johndang/git/SmartLock/"

    #upload blob to azure container
    block_blob_service.create_blob_from_path("pics", fileName, absFilePath)

    print("\nList blobs in the container")
    generator = block_blob_service.list_blobs("pics")
    for blob in generator:
        print("\t Blob name: " + blob.name)
    # print url of uploaded file
    upload_url = block_blob_service.make_blob_url('pics', fileName)
    print(upload_url)
    return upload_url
