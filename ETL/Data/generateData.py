from faker import Faker
import random
fake = Faker()

def obtenerGenero():
    genero= random.randint(0, 1)
    if genero == 0:
        return "M"
    else:
        return "F"

def obtenerNombre(genero:str):
    if genero == "M":
        return fake.first_name_male()
    else:
        return fake.first_name_female()


def obtenerApellido():
    return fake.last_name()

def obtenerDireccion():
    return fake.address();

def obtenerTelefono():
    telefono = fake.ean(length=8,prefixes=('09', ))
    for i  in [1,2]:
        telefono = telefono+str(random.randint(0,9))
    return telefono;

def obtenerCedula():
    cedula = fake.ean(length=8,prefixes=('01','02','03','04','05','06','07',"08","09","10",'11','12','13','14','15','16','17',"18","19","20",'21','22','23','24','30' ))
    for i  in [1,2]:
        cedula = cedula+str(random.randint(0,9))
    return cedula;

def obtenerNombreCalificacion():
    num_palabras =random.randint(3, 10)
    return fake.sentence(nb_words=num_palabras)

def obtenerCalificacion():
    ran = random.randint(0, 1)
    if ran == 0:
        return str(random.randint(0, 10))+','+str(random.randint(0, 99))
    else:
        return str(random.randint(0, 10))+'.'+str(random.randint(0, 99))

def obtenerSueldo():
    ran = random.randint(0, 1)
    if ran == 0:
        return str(random.randint(425, 5000))+','+str(random.randint(0, 99))
    else:
        return str(random.randint(425, 5000))+'.'+str(random.randint(0, 99))

# print(obtenerNombreCalificacion())
