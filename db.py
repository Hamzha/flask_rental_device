import psycopg2
from datetime import datetime
#connect to DB
def psotgresql():
    try:
        con = psycopg2.connect(
            host = '127.0.0.1',
            database = 'Flask',
            user= 'postgres',
            password = 'postgres'
        )
    except:
        print("Not connecting to postgres")
        return
    
    cur = con.cursor()

    try:
        cur.execute('CREATE TABLE IF NOT EXISTS "devices_meta" ("device_id" VARCHAR NOT NULL,"device_name" VARCHAR NOT NULL, "vendor" VARCHAR, "created_at" TIMESTAMP, "is_device_in_hub" BOOLEAN, "created_at_hub" TIMESTAMP, CONSTRAINT "devices_meta_pk" PRIMARY KEY ("device_id"));')
    except:
        print('devices_meta devices already exists!!!')
    
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS "users_meta" ("user_id" VARCHAR NOT NULL,"user_name" VARCHAR NOT NULL,"address" VARCHAR,"dob" DATE NOT NULL,"created_at" TIMESTAMP,CONSTRAINT "users_meta_pk" PRIMARY KEY ("user_id"));')
    except:
        print('userss_meta devices already exists!!!')
    
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS "device_rentals" ("device_id" VARCHAR NOT NULL,"rented_at" TIMESTAMP NOT NULL,"rented_to_uid" VARCHAR NOT NULL,"rented_to_name" VARCHAR NOT NULL,"transaction_id" SERIAL NOT NULL,"is_returned" BOOLEAN,"returned_at" TIMESTAMP,FOREIGN KEY (device_id) REFERENCES devices_meta (device_id),FOREIGN KEY (rented_to_uid) REFERENCES users_meta (user_id),CONSTRAINT "device_rentals_pk" PRIMARY KEY ("transaction_id"));')
    except:
        print('devices_rentals devices already exists!!!')
    
    cur.close()
    con.commit()
    con.close()

# psotgresql()

def connect_postgre():
    try :
        con = psycopg2.connect(
            host = '127.0.0.1',
            database = 'Flask',
            user= 'postgres',
            password = 'postgres'
        )
        return con
    except :
        return False
    
def addDevice(req):
    psotgresql()
    date_created_at = datetime.strptime(req['created_at'], "%d-%m-%Y %H:%M:%S")
    date_created_at_hub = datetime.strptime(req['created_at_hub'], "%d-%m-%Y %H:%M:%S")

    inset_query = "INSERT INTO devices_meta (device_id, device_name, vendor, created_at ,is_device_in_hub, created_at_hub) VALUES ("+ str(req["device_id"] )+",'" + req["device_name"] +"','"+ req["vendor"] +"','"+ str(date_created_at) +"',"+ str(req["is_device_in_hub"]) +",'"+ str(date_created_at_hub) +"');"
    
    con = connect_postgre()
    if con == False:
        print('Not connected')
        return 400

    else:
        try:
            cur = con.cursor()
            cur.execute(inset_query)
            con.commit()
            cur.close()
            con.close()
            return 200
        
        except:
            cur.close()
            con.close()
            return 409

def addUser(req):
    psotgresql()
    date_dob = datetime.strptime(req['dob'], "%d-%m-%Y")
    date_created_at = datetime.strptime(req['created_at'], "%d-%m-%Y %H:%M:%S")

    inset_query = "INSERT INTO users_meta (user_id, user_name, address, dob ,created_at) VALUES ("+ str(req["user_id"] )+",'" + req["user_name"] +"','"+ req["address"] +"','"+ str(date_dob) +"','"+ str(date_created_at) +"');"
    
    con = connect_postgre()
    if con == False:
        print('Not connected')
        return 400

    else:
        try:
            cur = con.cursor()
            cur.execute(inset_query)
            con.commit()
            cur.close()
            con.close()
            return 200
        except:
            cur.close()
            con.close()
            return 409

def modifyDevice(req):
    psotgresql()
    update_query = "UPDATE devices_meta SET device_name = '" + req["device_name"] +"'"
    
    if 'vendor' in req:
        update_query = update_query+", vendor = '"+ req["vendor"]+"'"
    if 'created_at' in req:
        date_created_at = datetime.strptime(req['created_at'], "%d-%m-%Y %H:%M:%S")
        update_query = update_query+", created_at = '" + str(date_created_at) +"'"
    if 'is_device_in_hub' in req:
        update_query = update_query+ ",is_device_in_hub = '"+str(req["is_device_in_hub"]) +"'"
    if 'created_at_hub' in req:
        date_created_at_hub = datetime.strptime(req['created_at_hub'], "%d-%m-%Y %H:%M:%S")
        update_query = update_query+", created_at_hub = '"+ str(date_created_at_hub) +"'"
    
    
    update_query = update_query+" WHERE device_id = '" +str(req["device_id"])+"';"
    select_query = "SELECT * FROM devices_meta WHERE device_id = '" +str(req["device_id"])+"';"
    
    con = connect_postgre()
    if con == False:
        print('Not connected')
        return 400

    else:
        cur = con.cursor()
        cur.execute(select_query)
        if cur.rowcount == 1:
            cur.execute(update_query)
            con.commit()
            cur.close()
            con.close()
            return 200
        else:
            cur.close()
            con.close()
            return 409

def modifyUser(req):
    psotgresql()
    select_query = "SELECT * FROM users_meta WHERE user_id = '" +str(req["user_id"])+"';"
    update_query = "UPDATE users_meta SET user_name = '"+ req['user_name'] +"'"
    
    if 'address' in req:
        update_query= update_query+", address = '" +req['address']+ "'"
    if 'dob' in req:
        date_dob = datetime.strptime(req['dob'], "%d-%m-%Y")
        update_query= update_query+", dob = '"+ str(date_dob) +"'"
    if 'created_at' in req:
        date_created_at = datetime.strptime(req['created_at'], "%d-%m-%Y %H:%M:%S")
        update_query= update_query+",created_at = '"+str(date_created_at)+"'"

    update_query= update_query+" WHERE user_id = '" +str(req["user_id"])+"';"
    con = connect_postgre()
    if con == False:
        print('Not connected')
        return 400

    else:
        cur = con.cursor()
        cur.execute(select_query)
        if cur.rowcount == 1:
            cur.execute(update_query)
            con.commit()
            cur.close()
            con.close()
            return 200
        else:
            cur.close()
            con.close()
            return 409

def rentDevice(req):
    psotgresql()
    date_rented_at = datetime.strptime(req['rented_at'], "%d-%m-%Y %H:%M:%S")
    date_returned_at = datetime.strptime(req['returned_at'], "%d-%m-%Y %H:%M:%S")

    select_query_user = "SELECT * FROM users_meta WHERE user_id = '" +str(req["rented_to_uid"])+"';"
    select_query_device = "SELECT * FROM devices_meta WHERE device_id = '" +str(req["device_id"])+"';"
    insert_query = "INSERT INTO device_rentals (device_id, rented_at, rented_to_uid, rented_to_name, transaction_id, is_returned, returned_at) VALUES ("+ str(req["device_id"] )+",'" + str(date_rented_at)+"','"+ str(req["rented_to_uid"]) +"','"+ str(req['rented_to_name']) +"','"+ str(req['transaction_id']) +"','"+ str(req['is_returned']) +"','"+ str(date_returned_at) +"');"

    con = connect_postgre()

    if con == False:
        print('Not connected')
        return 400
    else:
        cur = con.cursor()
        cur.execute(select_query_user)
        user_count = cur.rowcount
        cur.execute(select_query_device)
        device_count = cur.rowcount
        if user_count == 1 and device_count == 1:
            cur.execute(insert_query)
            con.commit()
            cur.close()
            con.close()
            return 200
        else:
            print(user_count, device_count)
            cur.close()
            con.close()
            return 409
        
def returnDevice(req):
    psotgresql()
    select_query_device = "SELECT * FROM device_rentals WHERE is_returned = '" +str("false")+"' AND device_id='" +str(req["device_id"]) + "';"
    con = connect_postgre()

    if con == False:
        print('Not connected')
        return 400
    else:
        cur = con.cursor()
        cur.execute(select_query_device)
        user_count = cur.rowcount
        if user_count == 0:
            cur.close()
            con.close()
            return 409
        else:
            devices = cur.fetchall()
            for value in devices:
                if(value[5] == False):
                    update_query_device = "UPDATE device_rentals SET is_returned = '" +str("true")+"' , device_id='" +str(req["device_id"]) + "' WHERE is_returned = '" +str("false")+"' AND device_id='" +str(req["device_id"]) + "';"
                    cur.execute(update_query_device)
                    con.commit()
                    cur.close()
                    con.close()
                    return 200
                else:
                    cur.close()
                    con.close()
                    return 409
                
