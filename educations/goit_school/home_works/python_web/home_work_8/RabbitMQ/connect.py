from mongoengine import connect


try:
    connect(host=f"""mongodb+srv://vadnet:vad0606vad@vaddatabase.k8vkpun.mongodb.net/mydb1?retryWrites=true&w=majority""", ssl=True)
    print("Connect OK")
except Exception as e:
    print(f"Error connecting to {e}")