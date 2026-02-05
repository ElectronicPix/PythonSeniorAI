"""
================================================================================
TUTORÍA: FUNDAMENTOS DE AUTENTICACIÓN Y GENERACIÓN DE JWT
Duración: 1 hora
================================================================================

OBJETIVOS DE APRENDIZAJE:
1. Comprender qué es JWT y por qué se usa en autenticación
2. Implementar autenticación con contraseñas hasheadas
3. Generar y validar tokens JWT
4. Proteger rutas con autenticación basada en tokens
5. Entender el flujo completo de autenticación

CONCEPTOS CLAVE:
- JWT (JSON Web Token): Token estándar para autenticación stateless
- Hash de contraseñas: Almacenamiento seguro usando bcrypt
- OAuth2: Estándar de autorización usado por FastAPI
- Token Bearer: Método de autenticación HTTP

ESTRUCTURA DEL CÓDIGO:
1. Configuración y dependencias
2. Modelos de datos (Pydantic)
3. Funciones de utilidad (hash, verificación, creación de tokens)
4. Endpoints de autenticación
5. Rutas protegidas

================================================================================
"""

# ============================================================================
# IMPORTS Y DEPENDENCIAS
# ============================================================================

# ----------------------------------------------------------------------------
# FastAPI - Framework web moderno y rápido para construir APIs
# ----------------------------------------------------------------------------
# ¿Por qué FastAPI?
# - Framework web moderno basado en estándares (OpenAPI, JSON Schema)
# - Alto rendimiento (comparable a NodeJS y Go)
# - Validación automática de datos con Pydantic
# - Documentación interactiva automática (Swagger UI)
# - Soporte nativo para async/await
# - Type hints integrados para mejor desarrollo
from fastapi import FastAPI, Depends, HTTPException, status
# FastAPI.security: Módulo de seguridad que implementa OAuth2
# - OAuth2PasswordBearer: Maneja la extracción de tokens del header Authorization
# - OAuth2PasswordRequestForm: Formulario estándar para login (username/password)
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# ----------------------------------------------------------------------------
# python-jose - Librería para trabajar con JWT (JSON Web Tokens)
# ----------------------------------------------------------------------------
# ¿Por qué python-jose?
# - Implementación completa del estándar JWT (RFC 7519)
# - Soporte para múltiples algoritmos de firma (HS256, RS256, etc.)
# - Codificación y decodificación segura de tokens
# - Validación automática de expiración y firma
# - Manejo de errores específicos de JWT
# Alternativa: PyJWT (más ligera pero menos funcionalidades)
from jose import JWTError, jwt
# JWTError: Excepción específica para errores en tokens JWT
# jwt: Funciones principales para encode/decode de tokens

# ----------------------------------------------------------------------------
# passlib - Librería para hash y verificación de contraseñas
# ----------------------------------------------------------------------------
# ¿Por qué passlib?
# - Implementación segura de algoritmos de hash (bcrypt, argon2, pbkdf2)
# - Protección contra timing attacks
# - Fácil migración entre algoritmos
# - Soporte para múltiples esquemas de hash
# - Contexto configurable para diferentes niveles de seguridad
from passlib.context import CryptContext
# CryptContext: Contexto configurable para manejar múltiples esquemas de hash
# En este caso usamos bcrypt, que es resistente a ataques de fuerza bruta

# ----------------------------------------------------------------------------
# datetime - Módulo estándar de Python para manejo de fechas y tiempos
# ----------------------------------------------------------------------------
# ¿Por qué datetime?
# - Manejo de timestamps para expiración de tokens
# - Cálculo de tiempos relativos (timedelta)
# - Formato estándar UTC para tokens JWT
# - No requiere instalación adicional (parte de la biblioteca estándar)
from datetime import datetime, timedelta
# datetime: Para obtener la fecha/hora actual
# timedelta: Para calcular tiempos de expiración (ej: 30 minutos desde ahora)

# ----------------------------------------------------------------------------
# typing - Módulo estándar de Python para type hints
# ----------------------------------------------------------------------------
# ¿Por qué typing?
# - Type hints mejoran la legibilidad y mantenibilidad del código
# - Permite validación estática con herramientas como mypy
# - Documenta explícitamente qué tipos espera cada función
# - Optional indica que un parámetro puede ser None o del tipo especificado
# - No requiere instalación adicional (parte de la biblioteca estándar)
from typing import Optional
# Optional[T]: Equivale a Union[T, None] - indica que puede ser T o None

# ----------------------------------------------------------------------------
# pydantic - Librería de validación de datos usando type hints de Python
# ----------------------------------------------------------------------------
# ¿Por qué pydantic?
# - Validación automática de datos basada en type hints
# - Serialización/deserialización JSON automática
# - Integración nativa con FastAPI
# - Genera documentación automática de esquemas
# - Previene errores de tipo en tiempo de ejecución
# - BaseModel permite definir modelos de datos con validación incorporada
from pydantic import BaseModel
# BaseModel: Clase base para crear modelos de datos con validación automática

# ============================================================================
# RESUMEN DE DEPENDENCIAS Y SUS PROPÓSITOS
# ============================================================================
"""
DEPENDENCIAS PRINCIPALES Y POR QUÉ SE NECESITAN:

1. FASTAPI (fastapi)
└─ Framework web para crear la API REST
└─ Proporciona: routing, validación, documentación automática
└─ Sin esto: No tendríamos servidor web ni endpoints

2. UVICORN (uvicorn) - Requerido para ejecutar FastAPI
└─ Servidor ASGI de alto rendimiento
└─ Proporciona: servidor HTTP para ejecutar la aplicación
└─ Sin esto: No podríamos ejecutar el servidor

3. PYTHON-JOSE (python-jose[cryptography])
└─ Librería para trabajar con JWT
└─ Proporciona: encode/decode de tokens, validación de firma
└─ Sin esto: No podríamos generar ni validar tokens JWT

4. PASSLIB (passlib[bcrypt])
└─ Librería para hash de contraseñas
└─ Proporciona: hash seguro de contraseñas, verificación
└─ Sin esto: Las contraseñas estarían en texto plano (INSEGURO)

5. PYDANTIC (pydantic)
└─ Validación de datos con type hints
└─ Proporciona: modelos de datos, validación automática
└─ Sin esto: Tendríamos que validar manualmente todos los datos

6. PYTHON-MULTIPART (python-multipart)
└─ Soporte para formularios multipart (requerido por OAuth2PasswordRequestForm)
└─ Proporciona: parsing de formularios HTML
└─ Sin esto: El endpoint /token no funcionaría correctamente

DEPENDENCIAS ESTÁNDAR (incluidas en Python):
- datetime: Manejo de fechas y tiempos
- typing: Type hints para mejor desarrollo

FLUJO DE DEPENDENCIAS:
┌─────────────┐
│   Cliente   │
└──────┬──────┘
    │ HTTP Request
    ▼
┌─────────────────────────────────────────────────────────┐
│                    UVICORN                              │
│              (Servidor HTTP/ASGI)                       │
└────────────────────┬────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────┐
│                    FASTAPI                              │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Routing + Validación (Pydantic)                 │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  OAuth2PasswordBearer (Extrae token del header)  │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  python-jose (Decodifica y valida JWT)           │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  passlib (Verifica hash de contraseña)           │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                    │
                    ▼
┌─────────────┐
│  Respuesta  │
└─────────────┘
"""

# ============================================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ============================================================================

app = FastAPI(
    title="Tutoría: Autenticación JWT",
    description="Ejemplo completo de autenticación con JWT en FastAPI",
    version="1.0.0"
)

# ============================================================================
# CONFIGURACIÓN DE SEGURIDAD
# ============================================================================

# SECRET_KEY: Clave secreta para firmar los tokens JWT
# ⚠️ IMPORTANTE: En producción, usar una clave segura y almacenarla en variables de entorno
# Ejemplo: SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_KEY = "tu-clave-secreta-super-segura-cambiar-en-produccion"
ALGORITHM = "HS256"  # Algoritmo de firma (HMAC con SHA-256)
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Tiempo de expiración del token

# Contexto para hashing de contraseñas usando bcrypt
# rounds=12: Número de rondas de hashing (mayor = más seguro pero más lento)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2PasswordBearer: Maneja la extracción del token del header Authorization
# tokenUrl: Ruta donde el cliente puede obtener el token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ============================================================================
# MODELOS DE DATOS (Pydantic)
# ============================================================================

class User(BaseModel):
    """Modelo para representar un usuario"""
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

class UserInDB(User):
    """Modelo para usuario en base de datos (incluye contraseña hasheada)"""
    hashed_password: str

class Token(BaseModel):
    """Modelo para respuesta de token"""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Modelo para datos del token decodificado"""
    username: Optional[str] = None

# ============================================================================
# BASE DE DATOS SIMULADA
# ============================================================================

# En producción, esto sería una base de datos real (PostgreSQL, MongoDB, etc.)
# Las contraseñas están hasheadas usando bcrypt
dummy_users_db = {
    "usuarioprueba": {
        "username": "usuarioprueba",
        "email": "usuario@ejemplo.com",
        "full_name": "Usuario de Prueba",
        "hashed_password": pwd_context.hash("123456"),  # Contraseña: 123456
        "disabled": False
    },
    "admin": {
        "username": "admin",
        "email": "admin@ejemplo.com",
        "full_name": "Administrador",
        "hashed_password": pwd_context.hash("admin123"),  # Contraseña: admin123
        "disabled": False
    }
}

# ============================================================================
# FUNCIONES DE UTILIDAD
# ============================================================================

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con su hash.
    
    Args:
        plain_password: Contraseña en texto plano
        hashed_password: Contraseña hasheada almacenada
    
    Returns:
        True si las contraseñas coinciden, False en caso contrario
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Genera un hash de una contraseña usando bcrypt.
    
    Args:
        password: Contraseña en texto plano
    
    Returns:
        Hash de la contraseña
    """
    return pwd_context.hash(password)

def get_user(username: str) -> Optional[UserInDB]:
    """
    Obtiene un usuario de la base de datos simulada.
    
    Args:
        username: Nombre de usuario a buscar
    
    Returns:
        Usuario si existe, None en caso contrario
    """
    if username in dummy_users_db:
        user_dict = dummy_users_db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    """
    Autentica un usuario verificando sus credenciales.
    
    Args:
        username: Nombre de usuario
        password: Contraseña en texto plano
    
    Returns:
        Usuario autenticado si las credenciales son válidas, None en caso contrario
    """
    user = get_user(username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Crea un token JWT con los datos proporcionados.
    
    Estructura de un JWT:
    - Header: Tipo de token y algoritmo de firma
    - Payload: Datos del usuario (claims)
    - Signature: Firma usando SECRET_KEY
    
    Claims estándar:
    - sub (subject): Identificador del usuario
    - exp (expiration): Tiempo de expiración
    
    Args:
        data: Diccionario con los datos a incluir en el token (ej: {"sub": username})
        expires_delta: Tiempo de expiración personalizado
    
    Returns:
        Token JWT codificado como string
    """
    to_encode = data.copy()
    
    # Calcular tiempo de expiración
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Agregar claim de expiración
    to_encode.update({"exp": expire})
    
    # Codificar el token usando la clave secreta
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Dependencia de FastAPI que extrae y valida el token JWT del request.
    
    Esta función se ejecuta automáticamente cuando se usa como dependencia
    en rutas protegidas. Extrae el token del header Authorization y lo valida.
    
    Args:
        token: Token JWT extraído del header Authorization
    
    Returns:
        Usuario autenticado
    
    Raises:
        HTTPException: Si el token es inválido o el usuario no existe
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decodificar el token JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        
        if username is None:
            raise credentials_exception
        
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """
    Verifica que el usuario actual esté activo (no deshabilitado).
    
    Args:
        current_user: Usuario obtenido de get_current_user
    
    Returns:
        Usuario activo
    
    Raises:
        HTTPException: Si el usuario está deshabilitado
    """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user

# ============================================================================
# ENDPOINTS DE LA API
# ============================================================================

@app.get("/")
async def root():
    """
    Endpoint raíz con información sobre la API.
    """
    return {
        "message": "Bienvenido a la Tutoría de Autenticación JWT",
        "endpoints": {
            "POST /token": "Obtener token de autenticación",
            "GET /protected": "Ruta protegida (requiere autenticación)",
            "GET /users/me": "Obtener información del usuario actual",
            "POST /register": "Registrar nuevo usuario"
        }
    }

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint de login que genera un token JWT.
    
    FLUJO DE AUTENTICACIÓN:
    1. Cliente envía username y password
    2. Servidor verifica las credenciales
    3. Si son válidas, genera un token JWT
    4. Cliente almacena el token y lo envía en requests posteriores
    
    Uso con curl:
    curl -X POST "http://localhost:8000/token" \\
        -H "Content-Type: application/x-www-form-urlencoded" \\
        -d "username=usuarioprueba&password=123456"
    
    Args:
        form_data: Datos del formulario OAuth2 (username, password)
    
    Returns:
        Token JWT y tipo de token
    
    Raises:
        HTTPException: Si las credenciales son inválidas
    """
    # Autenticar usuario
    user = authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Crear token con el username como subject
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
async def protected_route(current_user: User = Depends(get_current_active_user)):
    """
    Ruta protegida que requiere autenticación.
    
    Esta ruta demuestra cómo proteger endpoints usando dependencias.
    El token debe enviarse en el header Authorization:
    Authorization: Bearer <token>
    
    Uso con curl:
    curl -X GET "http://localhost:8000/protected" \\
        -H "Authorization: Bearer <tu_token_aqui>"
    
    Args:
        current_user: Usuario autenticado (obtenido automáticamente del token)
    
    Returns:
        Mensaje de bienvenida con el nombre de usuario
    """
    return {
        "message": f"¡Bienvenido {current_user.username}!",
        "info": "Has accedido exitosamente a una ruta protegida",
        "user": {
            "username": current_user.username,
            "email": current_user.email,
            "full_name": current_user.full_name
        }
    }

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """
    Obtiene la información del usuario actualmente autenticado.
    
    Este endpoint demuestra cómo acceder a los datos del usuario
    desde el token JWT decodificado.
    
    Args:
        current_user: Usuario autenticado
    
    Returns:
        Información del usuario actual
    """
    return current_user

@app.post("/register")
async def register_user(username: str, password: str, email: Optional[str] = None):
    """
    Registra un nuevo usuario en el sistema.
    
    Este endpoint demuestra cómo crear usuarios con contraseñas hasheadas.
    En producción, deberías validar la fortaleza de la contraseña y
    verificar que el usuario no exista.
    
    Args:
        username: Nombre de usuario único
        password: Contraseña en texto plano (se hasheará automáticamente)
        email: Email opcional del usuario
    
    Returns:
        Confirmación de registro
    
    Raises:
        HTTPException: Si el usuario ya existe
    """
    if username in dummy_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe"
        )
    
    # Crear nuevo usuario con contraseña hasheada
    hashed_password = get_password_hash(password)
    new_user = {
        "username": username,
        "email": email,
        "full_name": username.title(),
        "hashed_password": hashed_password,
        "disabled": False
    }
    
    dummy_users_db[username] = new_user
    
    return {
        "message": f"Usuario {username} registrado exitosamente",
        "username": username
    }

# ============================================================================
# EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*70)
    print("INICIANDO SERVIDOR DE TUTORÍA JWT")
    print("="*70)
    print("\nUsuarios de prueba:")
    print("  - Username: usuarioprueba | Password: 123456")
    print("  - Username: admin | Password: admin123")
    print("\nPara iniciar el servidor:")
    print("  uvicorn Tutoria1:app --reload")
    print("\nDocumentación interactiva disponible en:")
    print("  http://localhost:8000/docs")
    print("="*70 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    # pip install fastapi uvicorn python-jose
