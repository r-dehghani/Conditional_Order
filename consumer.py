import pika , json , os , psycopg2
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULES" , "C_O_API_Project.settings")
# django.setup()

# from C_O_API_App.models import indexes
 
params = pika.URLParameters("amqps://qovczade:SltebwIvG3a5zJDbkYxKP7yHQQc8aPCf@fly.rmq.cloudamqp.com/qovczade")
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received ")
    data = json.loads(body)
    # indexes.symbolisin = 
    print(data)
    

    con = psycopg2.connect(host='db', port="5432" , user="postgres" ,password ="dariush", database="postgres")
    cursor = con.cursor()

    INSERT_QUERY = """
    INSERT INTO "C_O_API_App_indexes" 
        ("symbolisin", "variation", "top", "bottom" , "opening_price") VALUES (%s,%s,%s,%s,%s);"""
    
    cursor.execute(INSERT_QUERY, (f'{data["symbolisin"]}',f'{data["variation"]}',f'{data["top"]}',f'{data["bottom"]}',f'{data["opening_price"]}'))
    con.commit()
    cursor.close()
    con.close()
    

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True) 


print(' [*] start consuming. To exit press CTRL+C')
channel.start_consuming()







    # close the cursor
    # cursor.close()
    # # close the connection
    # con.close()
    
 

