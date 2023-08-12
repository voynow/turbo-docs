# Turbo Docs 📚

![GitHub stars](https://img.shields.io/github/stars/voynow/turbo-docs?style=social)
![PyPI version](https://badge.fury.io/py/turbo-docs.svg)

Turbo Docs es una herramienta de documentación de software que utiliza modelos de lenguaje GPT para generar automáticamente documentación para su código Python. 

## ¿Por qué usar Turbo Docs? 🚀

Turbo Docs le permite generar documentación de alta calidad para su código de manera rápida y eficiente. Al utilizar modelos de lenguaje GPT, Turbo Docs puede generar descripciones detalladas y precisas de las funciones en su código. Esto puede ahorrarle tiempo y esfuerzo, y asegurarse de que su documentación esté siempre actualizada.

## Estructura del repositorio 📂

```
turbo_docs/
│
├── commands/
│   ├── docs.py
│   ├── readme.py
│   └── __init__.py
│
├── utils/
│   ├── cli_options.py
│   ├── directory.py
│   ├── openai_api.py
│   └── __init__.py
│
├── generate.py
├── setup.py
└── __init__.py
```

## Ejemplo de uso 💻

Para generar documentación para su código, simplemente ejecute el siguiente comando en la raíz de su repositorio:

```bash
turbo_docs --docs
```

Esto generará documentación para todas las funciones en su código y la guardará en un directorio `docs`.

## Instalación 🛠️

Puede instalar Turbo Docs a través de pip:

```bash
pip install turbo-docs
```

## Contribuir 🤝

Las contribuciones son bienvenidas! Por favor, consulte las [directrices de contribución](CONTRIBUTING.md) para más detalles.

## Licencia 📄

Turbo Docs está licenciado bajo la licencia MIT. Consulte el archivo [LICENSE](LICENSE) para más detalles.