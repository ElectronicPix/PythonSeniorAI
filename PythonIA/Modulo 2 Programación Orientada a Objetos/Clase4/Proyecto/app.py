from controllers.controlador import iniciar_app


def main():
    try:
        
        print("Iniciando Sistema de Parqueadero")
        
        iniciar_app()
    except KeyboardInterrupt:
        print("Gracias por usar el Parqueadero")
        print("Adios")
        
if __name__ == "__main__":
    main()
    
    
# Verificar todo el proyecto desde cero