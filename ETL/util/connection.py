from sqlalchemy import create_engine
from ETL.util.properties import getProperty

import pymysql
import traceback


class Db_Connection():
    """
    Class to manage database connections

    Attributes
    ----------
        connection : SQLAlchemy Engine
            database connection pool
        type : str, required
            type of database
        host : str, required
            database host
        port : str, required
            database port
        user : str, required
            database username
        password : str, required
            database password
        database : str, required
            name of the database

    Methods
    -------
    start(self):
        Creates and returns a database connection pool.
    stop(self):
        Dispose the database connection pool.    
    """

    def __init__(self, type, host, port, user, password, database):        
        """Constructor with initialization values for the class attributes

        Parameters
        ----------
        type : str, required
            value for the type attribute
        host : str, required
            value for the host attribute
        port : str, required
            value for the port attribute
        user : str, required
            value for the user attribute
        password : str, required
            value for the password attribute
        database : str, required
            value for the database attribute

        Returns
        -------
        None

        Raises
        ------
        None
        """    
        self.connection = None
        self.type = type
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def start(self):
        """Create and returns a database connection.

        Parameters
        ----------
        None      
        
        Returns
        -------
        SQLAlchemy Engine
            database connection pool

        Raises
        ------
        None
        """          
        try:
            if self.type == 'mysql':
                db_connection_str = 'mysql+pymysql://'+self.user+':'+self.password+'@'+self.host+':'+self.port+'/'+self.database
                self.connection = create_engine(db_connection_str)
                return self.connection
            else:
                return -1
        except Exception as e:
            print('Error in connection\n'+str(e))
            return -2

    def stop(self):
        """Dispose the database connection pool.

        Parameters
        ----------
        None     
        
        Returns
        -------
        None

        Raises
        ------
        None
        """  
        self.connection.dispose()
    
    

def connect(db_Name:str):
    #Variable
    type= getProperty("TYPE")
    host= getProperty("HOST")
    port= getProperty("PORT")
    user= getProperty("USER")
    pwd=  getProperty("PASSWORD")
    db=   db_Name
    
    try:
        con_db = Db_Connection(type,host,port,user,pwd,db)
        ses_db = con_db.start()
        if ses_db == -1:
            raise Exception(f"the give database type {type} is not valid")
        elif ses_db == -2:
            raise Exception(f"Error trying to conect to database {db}")
        
        return ses_db
    except:
        traceback.print_exc()
        
