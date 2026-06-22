import oracledb as orc
try:
    import oracledb

    connection = oracledb.connect(
        user="system",
        password="password",
        dsn="127.0.0.1:1522/ORCL"  # replace with correct service
    )

except orc.DatabaseError as db:
    print("Problem in oracle db:",db)


#I identified port by running lsnrctl status