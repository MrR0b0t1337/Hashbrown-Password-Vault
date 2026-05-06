from database.db import init_users_db, create_user, authenticate_user

init_users_db()
print("users.db created successfuly")

result = create_user("Brady", "opensesame123")
print("create_user result:", result)

result = authenticate_user("Brady", "opensesame123")
print("Successful authentication(good sign-in):", result)

result = authenticate_user("Brady", "opensesame1234")
print("Unsuccessful authentication(bad sign-in)", result)

result = authenticate_user("brady", "opensesame123")
print("Unsuccessful authentication(bad sign-in)", result)