import psycopg2

class UsersDAO:

    def __init__(self):
        connection_url = "dbname=photo_app_db user=postgres password=qwerty"
        self.conn = psycopg2._connect(connection_url)

#--------------- Phase 2 ---------------#

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, phone, email from Users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUserContactsById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name from Users, (select cid from ContactList where uid = %s) as C where uid = cid;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMembersByGroupId(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name from Users natural inner join isMember where gid = %s"
        cursor.execute(query, (gid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOwnerByGroupId(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name from Users natural inner join ChatGroup Where gid = %s"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()
        return result

    def getLikersByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, date from Users natural inner join Likes where mid = %s"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDislikersByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, date from Users natural inner join Dislikes where mid = %s"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

#----------------- END -----------------#

'''
    def login(self):
        result= "Welcome"
        return result

    def getUserByFirstName(self, firstName):
        result=[]
        if firstName=="Manuel":
            result=[1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
        elif firstName=="Fulano":
            result = [0, "Fulano", "Apellido", 787, "hotmail", "password123"]
        return result

    def getUserByLastName(self, lastName):
        result = []
        if lastName == "Rodriguez":
            result = [1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
        elif lastName == "Apellido":
            result = [0, "Fulano", "Apellido", 787, "hotmail", "password123"]
        return result

    def getUserByPhone(self, phone):
        result = []
        if phone == 939:
            result = [1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
        elif phone == 787:
            result = [0, "Fulano", "Apellido", 787, "hotmail", "password123"]
        return result

    def getUserByEmail(self, email):
        result = []
        if email == "gmail":
            result = [1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
        elif email == "hotmail":
            result = [0, "Fulano", "Apellido", 787, "hotmail", "password123"]
        return result

    def getUserGroupsById(self, uid):
        result = []
        return result
'''

'''
    def deleteUser(self, uid):
        result="USER DESTROYED"
        return result

    def updateUser(self, uid):
        result= "User %d information has been updated" %(uid)
        return result
    def createUser(self):
        result="User created,please check yur email to verify"
        return result
'''
