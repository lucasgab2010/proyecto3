import sqlite3
sqlite3.register_adapter(bool, int)