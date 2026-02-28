# import pymongo as py
# from PIL import Image
# import io

# client=py.MongoClient("mongodb://localhost:27017/")
# db=client["CandidateFace"]
# coll=db["Faces"]

# def saveImage():
#     im=Image.open(r"C:\\Users\\Deepak\\OneDrive\\Desktop\\useful images\\s1.png")
#     image_byte=io.BytesIO()
#     im.save(image_byte, format='PNG')
#     image = {
#             "data": image_byte.getvalue()
#         }

#     image_id = coll.insert_one(image).inserted_id
#     return image_id

# if __name__ == '__main__':
#     image_id=saveImage()