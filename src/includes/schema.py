import settings

from includes.db import Db

class Schema:

    def CreateDatabase():

        query = f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci"

        return Db.ExecuteQuery(query, None, True, True)

    def CreateTables():

        #####################################################################################################
        query = """
			CREATE TABLE IF NOT EXISTS template (
                email_id VARCHAR(255) PRIMARY KEY NOT NULL,
                sender LONGTEXT NOT NULL,
                bcc_recipients JSON NULL,
                purpose VARCHAR(255) NOT NULL,
                subject LONGTEXT DEFAULT NULL,
                message LONGTEXT DEFAULT NULL,
                reply_to JSON DEFAULT NULL,
                cc_recipients JSON NULL,
                delivered BOOLEAN DEFAULT 0,
                date DATETIME NOT NULL
            ) ENGINE=INNODB;
		"""

        if not Db.ExecuteQuery(query, None, True):
            return False

        Db.ExecuteQuery("ALTER TABLE template ADD INDEX email_id (email_id);", None, True)
        Db.ExecuteQuery("ALTER TABLE template ADD INDEX sender (sender);", None, True)
        Db.ExecuteQuery("ALTER TABLE template ADD INDEX purpose (purpose);", None, True)
        Db.ExecuteQuery("ALTER TABLE template ADD INDEX subject (subject);", None, True)
        Db.ExecuteQuery("ALTER TABLE template ADD INDEX delivered (delivered);", None, True)
        Db.ExecuteQuery("ALTER TABLE template ADD INDEX date (date);", None, True)
        #####################################################################################################

        return True