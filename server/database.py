import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

print("MONGO_DETAILS",config("MONGO_DETAILS"))
MONGO_DETAILS =  config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

#defining database name
database = client.fastapi

#defining collection name
student_collection = database.get_collection("students_collection")

# helpers

#just to conver the resopnse into python dict
def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }

# Retrieve all students present in the database
async def retrieve_students():
    students = []
    data = await student_collection.find()
    print(data)
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students

# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    print(student)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    #resonse will be in bson format so we have to convert it into python dict
    print(new_student)
    # to convert bson to python dict we have to use helper function
    return student_helper(new_student)

# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)
    
# Update a student with a matching ID
    # Update a student with a matching ID

    #javaScript CameCase convention python follow snake_case convention
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False
    
# Delete a student from the database
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True