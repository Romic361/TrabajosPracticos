class EMPRESA_PRIVADA:
    nombre=""


class CURSOS:
    fechacomienzo= ""
    titulo=""
    descripcion=""
    objetivos=""
    programa=""
    costo=""
    duracionMeses=""   
    foto=0
    estado=""

    def __init__(self, FechaComienzo, Titulo, Descripcion, Objetivos, Programa, Costo, DuracionMeses, Foto, Estado):
        self.fechacomienzo=FechaComienzo
        self.titulo=Titulo
        self.descripcion=Descripcion
        self.objetivos=Objetivos
        self.programa=Programa
        self.costo=Costo
        self.duracionMeses=DuracionMeses
        self.foto=Foto
        self.estado=Estado

        def getFechaComienzo(self):
            return self.FechaComienzo
        def getTitulo(self):
            return self.Titulo
        def getDescripcion(self):
            return self.Descripcion
        def getObjetivos(self):
            return self.Objetivos
        def getPrograma(self):
            return self.Programa
        def getCostos(self):
            return self.Costos                    
        def getDuracionMeses(self):
            return self.DuracionMeses
        def getFoto(self):
            return self.Foto
        def getEstado(self):
            return self.Estado
        

        def setFechaComienzo(self, FechaComienzo):
            self.FechaComienzo = FechaComienzo
        def setTitulo(self, Titulo):
            self.Titulo = Titulo
        def setDescripcion(self, Descripcion):
            self.Descripcion =Descripcion
        def setObjetivos(self, Objetivos):
            self.Objetivos =Objetivos
        def setPrograma(self, Programa):
            self.Programa=Programa
        def setCostos(self, Costos):
            self.Costos= Costos                  
        def setDuracionMeses(self, DuracionMeses):
            self.DuracionMeses=DuracionMeses
        def setFoto(self, Foto):
            self.Foto=Foto
        def setEstado(self, Estado):
            self.Estado=Estado

class CATEGORIAS:
    inicial=""
    intermedio=""
    avanzado=""
    
    def __init__(self, Inicial, Intermedio, Avanzado):
        self.inicial = Inicial
        self.intermedio = Intermedio
        self.avanzado =  Avanzado

        def getInicial (self):
            return self.Inicial
        def getIntermedio (self):
            return self.Intermedio
        def getAvanzado (self):
            return self.Avanzado
        
        def setInicial (self, Inicial):
            self.Inicial = Inicial
        def setIntermedio (self, Intermedio):
            self.Intermedio = Intermedio
        def setAvanzado (self, Avanzado):
            self.Avanzado = Avanzado
        
class CONJ_CLASES:
    fecha=""
    titulo=""
    contenido=""
    URLDrive=""

    def __init__(self, Fecha, Titulo, Contenido, URLdrive):
        self.fecha = Fecha
        self.titulo = Titulo
        self.contenido = Contenido 
        self.URLDrive = URLdrive

        def getFecha (self):
            return self.Fecha
        def getTitulo (self):
            return self.Titulo
        def getContenido (self):
            return self.Contenido
        def getURLdrive (self):
            return self.URLDrive
        
        def setFecha (self, Fecha):
            self.fecha = Fecha
        def setTitulo (self, Titulo):
            self.titulo = Titulo
        def setContenido (self, Contenido):
            self.contenido = Contenido
        def setURLdrive (self, URLdrive):
            self.urldrive = URLdrive

class DOCENTES:
    apellido=""
    nombre=""
    DNI=0
    fechaNacimiento=""
    diereccion=""
    localidad=""
    codigoPostal=""
    provincia=""
    telefonoCelular=""
    email=""

    def __init__(self, Apellido, Nombre, NDNI, FechaNacimiento, Direccion, Localidad, CodigoPostal, Provincia,TelefonoCelular, Email):
        self.apellido = Apellido
        self.nombre = Nombre
        self.DNI = NDNI
        self.fechaNacimiento = FechaNacimiento 
        self.diereccion=  Direccion
        self.localidad = Localidad
        self.codigoPostal = CodigoPostal
        self.provincia = Provincia
        self.telefonoCelular = TelefonoCelular
        self.email = Email

        def getApellido(self):
            return self.Apellido
        def getNombre(self):
            return self.Nombre
        def getNDNI(self):
            return self.NDNI
        def getFechaNacimiento(self):
            return self.FechaNacimiento
        def getDireccion(self):
            return self.Direccion
        def getLocalidad(self):
            return self.Localidad
        def getCodigoPostal (self):
            return self.CodigoPostal
        def getProvicia (self):
            return self.Provicia
        def getTelefonoCelular (self):
            return self.TelefonoCelular
        def getEmail (self):
            return self.Email
        
        def setApellido(self, Apellido):
            self.apellido = Apellido
        def setNombre(self, Nombre):
            self.nombre = Nombre
        def setNDNI(self, NDNI):
            self.DNI = NDNI
        def setFechaNacimiento(self, FechaNacimiento):
            self.fechaNacimiento = FechaNacimiento
        def setDireccion(self,Direccion):
            self.direccion = Direccion
        def setLocalidad(self, Localidad):
            self.localidad = Localidad
        def setCodigoPostal(self, CodigoPostal):
            self.codigoPostal = CodigoPostal
        def setProvincia(self, Provincia):
            self.provincia = Provincia
        def setTelefonoCelular(self, TelefonoCelular):
            self.telefonoCelular = TelefonoCelular
        def setEmail(self, Email):
            self.email = Email


class CUENTA_USUARIO: 
    nombre=""
    apellido=""
    DNI=0
    fechaNacimiento=""
    direccion=""
    localidad=""
    codigoPostal=""
    provincia=""
    telefonoCelular=""
    email=""
    clave=""
    reconfirmarClave=""


    def __init__(self, Nombre, Apellido, NDNI, FechaNacimiento, Direccion, Localidad, CodigoPostal, Provincia,TelefonoCelular, Email, Clave, ReconfirmarClave):

        self.nombre = Nombre
        self.apellido = Apellido
        self.DNI = NDNI
        self.fechaNacimiento = FechaNacimiento 
        self.diereccion=  Direccion
        self.localidad = Localidad
        self.codigoPostal = CodigoPostal
        self.provincia = Provincia
        self.telefonoCelular = TelefonoCelular
        self.email = Email
        self.clave = Clave
        self.reconfirmarClave = ReconfirmarClave
 # FALTA VALIDAR EL EMAIL#
        
        def getNombre(self):
            return self.Nombre
        def getApellido(self):
            return self.Apellido
        def getNDNI(self):
            return self.NDNI
        def getFechaNacimiento(self):
            return self.FechaNacimiento
        def getDireccion(self):
            return self.Direccion
        def getLocalidad(self):
            return self.Localidad
        def getCodigoPostal (self):
            return self.CodigoPostal
        def getProvicia (self):
            return self.Provicia
        def getTelefonoCelular (self):
            return self.TelefonoCelular
        def getEmail (self):
            return self.Email
        def getClave (self):
            return self.Clave
        def getReconfirmarClave(self):
            return self.ReconfirmarClave
        
        
        def setNombre(self, Nombre):
            self.nombre = Nombre
        def setApellido(self, Apellido):
            self.apellido = Apellido
        def setNDNI(self, NDNI):
            self.DNI = NDNI
        def setFechaNacimiento(self, FechaNacimiento):
            self.fechaNacimiento = FechaNacimiento
        def setDireccion(self,Direccion):
            self.direccion = Direccion
        def setLocalidad(self, Localidad):
            self.localidad = Localidad
        def setCodigoPostal(self, CodigoPostal):
            self.codigoPostal = CodigoPostal
        def setProvincia(self, Provincia):
            self.provincia = Provincia
        def setTelefonoCelular(self, TelefonoCelular):
            self.telefonoCelular = TelefonoCelular
        def setEmail(self, Email):
            self.email = Email
        def Clave(self, Clave):
            self.clave = Clave
        def ReconfirmarClave(self, ReconfirmarClave):
            self.reconfirmarClave = ReconfirmarClave


class CARRITO_COMPRAS:
    foto=""
    titulo_del_curso=""
    duracion=""
    costo=""

    def __init__(self,Foto,Titulo_del_Curso, Duracion, Costo):
        self.foto = Foto
        self.titulo_del_curso =Titulo_del_Curso
        self.duracion =Duracion
        self.costo =Costo

        def getFoto(self):
            return self.Foto
        def getTitulo_del_Curso(self):
            return self.Titulo_del_Curso
        def getDuracion(self):
            return self.Duracion
        def getCosto(self):
            return self.Costo
        

        def setFoto(self, Foto):
            self.foto = Foto
        def setTitulo_del_Curso(self, Titulo_del_Curso):
            self.titulo_del_curso = Titulo_del_Curso
        def setDuracion(self,Duracion):
            self.duracion =Duracion
        def setCosto(self,Costo):
            self.costo =Costo


class MEDIOS_PAGO:
    tarjeta_debito=""
    tarjeta_credito=""
    transferencia_bancaria=""


    def __init__(self, Tarjeta_Debito, Tarjeta_Credito, Transferencia_Bancaria):
        self.tarjeta_debito =Tarjeta_Debito
        self.tarjeta_credito =Tarjeta_Credito
        self.transferencia_bancaria =Transferencia_Bancaria


        def getTarjeta_Debito(self):
            return self.Tarjeta_Debito
        def getTarjeta_Credito(self):
            return self.Tarjeta_Credito
        def getTransferencia_Bancaria(self):
            return self.Transferencia_Bancaria
        
        def setTrajeta_Debito(self):
            self.tarjeta_debito = self.Tarjeta_Debito
        def setTarjeta_Credito(self):
            self.tarjeta_credito = self.Tarjeta_Credito
        def setTransferencia_Bancaria(self):
            self.transferencia_bancaria = self.Transferencia_Bancaria

    
class DATOS_BASICOS:
    nombre_titular=""
    numero_tarjeta=""
    fecha_vencimiento=""
    DNI=""


    def __init__(self, Nombre_Titular, Numero_Tarjeta, Fecha_Vencimiento, NDNI):
        self.nombre_titular = Nombre_Titular
        self.numero_tarjeta = Numero_Tarjeta
        self.fecha_vencimientos = Fecha_Vencimiento
        self.DNI = NDNI


        def getNombre_Titular(self):
            return self.Nombre_Titular
        def getNumero_Tarjeta(self):
            return self.Numero_Tarjeta
        def getFecha_Vencimiento(self):
            return self.Fecha_Vencimiento
        def getNDNI(self):
            return self.NDNI
        
        def setNombre_Titular(self, Nombre_Titular):
            self.nombre_titular = Nombre_Titular
        def setNumero_Tarjeta(self, Numero_Tarjeta):
            self.numero_tarjeta = Numero_Tarjeta
        def setFecha_Vencimiento(self, Fecha_Vencimiento):
            self.fecha_vencimiento = Fecha_Vencimiento
        def setNDNI(self, NDNI):
            self.DNI = NDNI


#FALTA CONFIRMAR COMPRA #
#REGISTRAR FECHA DE COMPRA
#USUARIO QUE LA REALIZA
#MONTO TOTAL