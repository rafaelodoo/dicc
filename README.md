# DICC - Desarrollo e Innovación para Odoo 18

## 📋 Descripción

DICC es un proyecto de desarrollo dedicado a la creación de nuevos features, módulos personalizados y actualizaciones para Odoo 18. Este repositorio contiene las extensiones, mejoras y personalizaciones desarrolladas para optimizar y expandir las funcionalidades nativas de Odoo.

## 🚀 Características Principales

- **Módulos Personalizados**: Desarrollo de módulos específicos para necesidades empresariales
- **Mejoras de Rendimiento**: Optimizaciones en procesos existentes de Odoo
- **Integraciones Avanzadas**: Conectores con sistemas externos y APIs
- **Personalización de UI/UX**: Mejoras en la interfaz de usuario
- **Automatizaciones**: Flujos de trabajo automatizados y procesos inteligentes

## 🛠️ Tecnologías Utilizadas

- **Odoo 18**: Framework ERP base
- **Python 3.8+**: Lenguaje de programación principal
- **PostgreSQL**: Base de datos
- **XML/QWeb**: Templates y vistas
- **JavaScript/jQuery**: Frontend interactivo
- **CSS/SCSS**: Estilos personalizados

## 📦 Estructura del Proyecto

```
dicc/
├── pos_self_order_search/  # Módulo de búsqueda para Autopedido
├── custom_module_1/        # Ejemplo de módulo personalizado
├── custom_module_2/        # Ejemplo de módulo personalizado
├── docs/                   # Documentación del proyecto
│   └── tickets/            # Tickets de desarrollo
├── config/                 # Archivos de configuración (desarrollo local)
├── data/                   # Datos de prueba y migraciones
├── scripts/                # Scripts de utilidad
└── tests/                  # Pruebas automatizadas
```

> **Nota para Odoo.sh**: Los módulos se ubican directamente en la raíz del proyecto para compatibilidad con Odoo SH (Odoo.sh).

## 🔧 Instalación y Configuración

### Prerequisitos

- Python 3.8 o superior
- PostgreSQL 12 o superior
- Node.js (para desarrollo frontend)
- Git

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd dicc
   ```

2. **Crear entorno virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate     # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   ```bash
   createdb odoo_dicc
   ```

5. **Configurar Odoo**
   ```bash
   cp config/odoo.conf.example config/odoo.conf
   # Editar config/odoo.conf con tus configuraciones
   ```

6. **Ejecutar Odoo**
   ```bash
   ./odoo-bin -c config/odoo.conf
   ```

## 🌐 Despliegue en Odoo.sh

Este proyecto está optimizado para **Odoo.sh**:

- Los módulos se ubican directamente en la raíz del repositorio
- No se requiere directorio `addons/`
- Odoo.sh detecta automáticamente los módulos en la raíz
- Los archivos de configuración local (`config/`) son ignorados en producción

### Estructura para Odoo.sh
```
dicc/                       # Repositorio raíz
├── pos_self_order_search/  # Módulo 1
├── otro_modulo/            # Módulo 2
├── docs/                   # Documentación
└── README.md
```

## 🔨 Desarrollo

### Crear un Nuevo Módulo

```bash
# Generar estructura base del módulo en la raíz (para Odoo.sh)
python scripts/create_module.py nombre_del_modulo

# O manualmente:
mkdir nombre_del_modulo
cd nombre_del_modulo
touch __manifest__.py __init__.py
mkdir models views controllers data security tests
```

### Mejores Prácticas

- Seguir las convenciones de nomenclatura de Odoo
- Documentar todos los métodos y clases
- Escribir pruebas unitarias para funcionalidades críticas
- Usar control de versiones semántico
- Revisar código antes de hacer merge

### Estructura de un Módulo

```
custom_module/              # Módulo en la raíz del proyecto (Odoo.sh)
├── __manifest__.py         # Manifiesto del módulo
├── __init__.py             # Inicialización del módulo
├── models/                 # Modelos de datos
│   └── __init__.py
├── views/                  # Vistas XML
├── controllers/            # Controladores web
├── static/                 # Archivos estáticos (JS, CSS, imágenes)
├── data/                   # Datos por defecto
├── security/               # Reglas de acceso y seguridad
│   └── ir.model.access.csv
├── tests/                  # Pruebas del módulo
│   └── __init__.py
└── README.md               # Documentación del módulo
```

## 🧪 Pruebas

```bash
# Ejecutar todas las pruebas
python -m pytest tests/

# Ejecutar pruebas de un módulo específico
python -m pytest custom_module/tests/

# Ejecutar pruebas con coverage
pytest --cov=. tests/

# Ejecutar pruebas de Odoo (si tienes servidor local)
./odoo-bin -c config/odoo.conf -d test_db --test-enable --stop-after-init -i custom_module
```

## 📚 Documentación

- [Guía de Desarrollo](docs/development-guide.md)
- [API Reference](docs/api-reference.md)
- [Configuración Avanzada](docs/advanced-configuration.md)
- [Solución de Problemas](docs/troubleshooting.md)

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit los cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

### Estándares de Código

- Usar PEP 8 para Python
- Documentar funciones y clases
- Añadir pruebas para nuevas funcionalidades
- Mantener compatibilidad con Odoo 18

## 📝 Changelog

### [Versión 1.0.0] - 2024-01-XX
- Configuración inicial del proyecto
- Estructura base de módulos
- Documentación inicial

## 🐛 Reportar Problemas

Si encuentras algún bug o tienes sugerencias, por favor:

1. Revisar si ya existe un issue similar
2. Crear un nuevo issue con:
   - Descripción detallada del problema
   - Pasos para reproducir
   - Versión de Odoo y sistema operativo
   - Screenshots si es necesario

## 📄 Licencia

Este proyecto está bajo la Licencia [LICENCIA] - ver el archivo [LICENSE.md](LICENSE.md) para detalles.

## 👥 Equipo

- **Desarrollador Principal**: [Rafael Lopez Flores]
- **Colaboradores**: [Earvin Pérez]

## 🔗 Enlaces Útiles

- [Documentación Oficial de Odoo 18](https://www.odoo.com/documentation/18.0/)
- [Odoo Developer Documentation](https://www.odoo.com/documentation/18.0/developer.html)
- [Community Odoo](https://www.odoo.com/forum/)

---

**¿Necesitas ayuda?** No dudes en contactarnos o abrir un issue en el repositorio.