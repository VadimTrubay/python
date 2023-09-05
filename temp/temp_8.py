# import asyncio
#
#
# async def baz():
#     print("Preparation")
#     await asyncio.sleep(3)
#     return True
#
#
# async def main():
#     result = baz()
#     print(result)
#     result = await result
#     return result
#
# if __name__ == "__main__":
#     result = asyncio.run(main())
#     print(result)

# from time import sleep, time
# from faker import Faker
#
# fake = Faker()
#
#
# def get_user_sync(uid: int) -> dict:
#     sleep(1)
#     return {"id": uid, "name": fake.name(), "email": fake.email()}
#
#
# async def get_user_async(uid: int) -> dict:
#     await asyncio.sleep(1)
#     return {"id": uid, "name": fake.name(), "email": fake.email()}
#
#
# async def main():
#     r = await asyncio.gather(get_user_async(1),
#                              get_user_async(2),
#                              get_user_async(3))
#     return r
#
#
# if __name__ == "__main__":
#     start = time()
#     r = asyncio.run(main())
#     print(r)
#     print(time() - start)
#     print("_______________________")
#     start = time()
#     u4 = get_user_sync(4)
#     u5 = get_user_sync(5)
#     u6 = get_user_sync(6)
#     print(u4, u5, u6)
#     print(time() - start)
























































