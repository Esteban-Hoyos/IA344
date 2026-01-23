training_data = [
        # Saludos
        ("Hola", "¡Hola! Bienvenido a Sublimados Esteban. ¿En qué puedo ayudarte con camisas o gorras?"),
        ("Buenas tardes", "¡Hola! Bienvenido a Sublimados Esteban. ¿En qué puedo ayudarte con camisas o gorras?"),
        ("Buenas noches", "¡Hola! Bienvenido a Sublimados Esteban. ¿En qué puedo ayudarte con camisas o gorras?"),
        ("Hey", "¡Hola! Bienvenido a Sublimados Esteban. ¿En qué puedo ayudarte con camisas o gorras?"),

        # Preguntas sobre el chatbot
        ("¿Quién eres?", "Soy el chatbot de Sublimados Esteban, aquí para ayudarte con pedidos y consultas."),
        ("¿Cuál es tu nombre?", "Soy el chatbot de Sublimados Esteban, aquí para ayudarte con pedidos y consultas."),

        # Preguntas sobre productos
        ("¿Qué vendes?", "Vendemos camisas y gorras con diseños sublimados personalizados. Camisas: $20.000 COP, Gorras: $15.000 COP."),
        ("¿Tienes camisas?", "Sí, tenemos camisas sublimadas en varios diseños. Precio: $20.000 COP cada una."),
        ("¿Tienes gorras?", "Sí, gorras sublimadas disponibles. Precio: $15.000 COP cada una."),
        ("¿Cuáles diseños tienes?", "Tenemos diseños de animales, frases motivadoras, paisajes y personalizados. ¿Quieres ver opciones?"),
        ("¿Puedo personalizar?", "¡Claro! Envía tu diseño y lo sublimamos. Agrega $5.000 COP por personalización."),

        # Preguntas sobre precios
        ("¿Cuánto cuesta una camisa?", "Una camisa sublimada cuesta $20.000 COP."),
        ("¿Precio de gorra?", "Una gorra sublimada cuesta $15.000 COP."),
        ("¿Hay descuentos?", "Por compras de 5 o más, 10% de descuento. ¡Pregunta por promociones!"),

        # Pedidos y órdenes
        ("Quiero comprar una camisa", "Genial. ¿Qué diseño? ¿Talla? ¿Cantidad? Te guío: envía detalles y confirmo stock."),
        ("Pedido de gorra", "Genial. ¿Qué diseño? ¿Cantidad? Te guío: envía detalles y confirmo stock."),
        ("¿Cómo hago un pedido?", "Dime el producto, diseño, talla/cantidad y dirección. Pago por transferencia o contraentrega."),
        ("¿Stock disponible?", "Tenemos 100 camisas y 100 gorras en stock. ¡Actualizado al momento!"),

        # Envíos y entrega
        ("¿Envíos a Cali?", "Sí, envíos gratis en Cali. Fuera: $10.000 COP. Tiempo: 1-3 días."),
        ("¿Cuánto demora el envío?", "En Cali: mismo día o siguiente. Nacional: 2-5 días."),
        ("¿Métodos de pago?", "Transferencia bancaria, Nequi, Daviplata o contraentrega en Cali."),

        # Otras consultas
        ("¿Horarios?", "Atendemos 24/7 por este chat. Entregas de 8am a 6pm."),
        ("¿Garantía?", "Garantía de 30 días por defectos. ¡Calidad asegurada!"),
        ("Gracias", "¡De nada! ¿Algo más?"),
        ("Adiós", "¡Hasta pronto! Gracias por visitar Sublimados Esteban."),

        # Variaciones para robustez (el modelo aprenderá similitudes)
        ("Hola qué tal", "¡Hola! Bienvenido a Sublimados Esteban. ¿En qué puedo ayudarte con camisas o gorras?"),
        ("Precio camisa", "Una camisa sublimada cuesta $20.000 COP."),
        ("Comprar gorras", "Genial. ¿Qué diseño? ¿Cantidad? Te guío: envía detalles y confirmo stock."),
    ]
