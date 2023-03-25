from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://" + db_id + ":" + db_passwd + "@"
                                        + db_ip + ":" + db_port + "/" + db_name, encoding='utf-8')



