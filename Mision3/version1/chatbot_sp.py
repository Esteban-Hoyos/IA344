#scikit-learn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#función de entrenamiento pregunta-respuesta
def build_and_train_model(train_pairs):
    #train_pairs: lista de pares (pregunta, respuesta)
    #Ejemplo [("Hola", "Hola") ("Adios","hasta luego")]

    questions=[q for q,_ in train_pairs] #lista de preguntas
    answers=[a for _,a in train_pairs]   #lista de respuestas 

    #Crear el vectorizador, que traducirá texto a números 
    vectorizer=CountVectorizer()

    #Entrenamiento
    x=vectorizer.fit_transform(questions)

    #obtenemos una lista de respuestas únicas
    unique_answers= sorted(set(answers))

    #Crear el diccionario con las etiquetas 
    answers_to_labels={a:i for i,a in enumerate(unique_answers)}

    #creamos una lista
    y=[answers_to_labels[a] for a in answers]

    #modelo clasificación de texto
    model =MultinomialNB()
    model.fit(x,y)
    return model,vectorizer,unique_answers

#función predict_answer
def predict_answer(model,vectorizer,unique_answers,user_text):
    #vectorizar la entrada del usuario
    x = vectorizer.transform([user_text])

    #predecir la etiqueta de la respuesta correcta 
    label = model.predict(x)[0]

    #devolver la respuesta correspondiente a la etiqueta
    return unique_answers[label]

#programa principal
if __name__=="__main__":
    training_data=[
        ("Hola","Hola, ¿en qué puedo ayudarte?"),
        ("¿Cuál es tu nombre?","Soy un chatbot creado para ayudarte."),
    ]
    #Entrenar el modelo con la lista
    model,vectorizer,unique_answers=build_and_train_model(training_data)

    #mostrar un mensaje inicial al usuario 
    print("Chatbot supervisado: ¡Hola! Soy un chatbot. Escribe 'salir' para terminar la conversación./n")
    while True:
        #Pedimos una frase al usuario
        user =input("Tú: ")
        if user.lower() in {"salir", "exit","quit"}:
            print("Chatbot: ¡Adiós!")
            break
        response=predict_answer(model,vectorizer,unique_answers,user)
        print("Chatbot:",response)
    