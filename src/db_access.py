def db_access_func() -> str:
    return db_access_body()
def db_access_body() -> str:
    # 本当は、ここにDBアクセスのいろんなのが書いてある
    return "db_access"

def db_access_func_with_parameters(str1:str,int1:int) -> str:
    return db_access_body_with_parameters(str1, int1)
def db_access_body_with_parameters(str1:str,int1:int) -> str:
    # ここにもDBアクセスのいろんなのが書いてある
    return "db_access_with_parameters"