#Task
'''
Scrape a website for images and meta data, say Myntra. And build a classifier of images for 
1. Gender - male/female
2. ⁠Full sleeve/half sleeve
Scraping needs to be automated (less images with limited data would be acceptable). 
'''

# Future Scope:
'''
With starting of this code we can scrape the images from the website and then we can use the images to train 
the model and then we can use the model to predict the classification  as per the task of the assigment. 

2. We can use AI agents to automate the scraping process by justing only telling it name of the website and the attach function to it. Furthermore, 
we can use the AI agents to train the model and then use the model to predict the classification as per the task of the assigment.By Only
setting few parameters and then the AI agents will do the rest of the work.

1.along with that we can run it on the server and then we can use the model to predict the classification as per
the task of the assigment such as AWS S3 bucket.
sample code:


import boto3

def upload_file_to_s3(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

    You need to set them up in the AWS credentials file (~/.aws/credentials), 
    or you can set the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_SESSION_TOKEN environment variables.


'''
