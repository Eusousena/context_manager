from contextlib import contextmanager

@contextmanager
def database_transaction(file_path, mode):
    file = None
    try:
        print("File open")
        file = open(file_path, mode)
        yield file
    except Exception as e:
        print("Error", e)
    finally:
        print("Close file")
        file.close()    

class Database:
    @staticmethod
    def write_data(data):
        with database_transaction("data_context_manager", "a") as file:
            file.write(data)

    @staticmethod
    def reading_data():
        with database_transaction("data_context_manager", "r") as file:
            return file.read()

            
# Escrevendo dados no arquivo
Database.write_data("Primeira linha\n")
Database.write_data("Segunda linha\n")

# Lendo dados do arquivo
data = Database.reading_data()
print("Dados lidos do arquivo:")
print(data)