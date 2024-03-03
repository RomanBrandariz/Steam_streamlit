import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json


# Insertar la imagen con el ancho calculado en píxeles
st.image("logo.jpg")

columna1, columna2, columna3  = st.columns(3)
with columna1:
    '''### Endpoint 1'''
    st.write('Devuelve año con mas horas jugadas para un género dado')
with columna2:
    if st.checkbox('EndPoint1', value=False):
        
        result_df = pd.read_csv('PlayTimeGenre.csv')
        # Obtener los valores únicos de la columna 'genres'
        valores_unicos = result_df['genres'].unique()
        # Mostrar la caja desplegable en la interfaz de Streamlit
        key_genero = "selectbox_genero"
        genero = st.selectbox('Selecciona un género:', valores_unicos, key=key_genero)
        filtered_df = result_df[result_df['genres'] == genero]
        grouped_df = filtered_df.groupby('year')['hours_game'].sum()
        max_hours_year = grouped_df.idxmax()
        # Construye el response_data
        response_data = "Año de lanzamiento con más horas jugadas para {}: {}".format(genero, max_hours_year)
        # Muestra el resultado
        #st.write(response_data)
with columna3:
    try:
        if response_data is not None:
            #st.write(response_data)
            formatted_text = "<h3>{}</h3>".format(response_data)
            st.markdown(formatted_text, unsafe_allow_html=True)
    except NameError:
        
        st.write("Aguardando Seleccion.")


columna1, columna2, columna3  = st.columns(3)
with columna1:
    '''### Endpoint 2 '''
    st.write('Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.')
with columna2:
    if st.checkbox('EndPoint2', value=False):
        consulta2 = pd.read_csv('UserForGenre.csv')
        # Filtrar el DataFrame por el género dado
        valores_unicos2 = consulta2['genres'].unique()
        genero2 = st.selectbox('Selecciona un género:', valores_unicos2,)
        genre_data2 = consulta2[consulta2['genres'] == genero2]
        # Encontrar al usuario con más horas jugadas para ese género
        top_user = genre_data2.loc[genre_data2['hours_game'].idxmax()]['user_id']
        # Crear una lista de acumulación de horas jugadas por año
        hours_by_year = genre_data2.groupby('year')['hours_game'].sum().reset_index()
        hours_by_year = hours_by_year.rename(columns={'year': 'Año', 'hours_game': 'Horas'})
        hours_list = hours_by_year.to_dict(orient='records')
        # Crear el mensaje con el resultado
        mensaje_usuario = "Usuario con más horas jugadas para Género {}: {}".format(genero2, top_user)
        mensaje_horas = "Horas jugadas por año:"
        # Mostrar el resultado en la interfaz de Streamlit
        #st.write(mensaje_usuario)
        #st.write(mensaje_horas)
        #st.write(pd.DataFrame(hours_list))
with columna3:
    try:
        if mensaje_usuario is not None:
            st.write(mensaje_usuario)
            st.write(mensaje_horas)
            st.write(pd.DataFrame(hours_list))
    except NameError:
        
        st.write("Aguardando Seleccion.")
        
        
columna1, columna2, columna3  = st.columns(3)
with columna1:
    '''### Endpoint 3'''
    st.write('Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.')
    
    # **def UsersRecommend( año : int )**: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
    # Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    # Input: **UsersRecommend.csv**
with columna2:
    if st.checkbox('EndPoint3', value=False):
        df3 = pd.read_csv('UsersRecommend.csv')
        valores_unicos3 = df3['year'].unique()
        # Filtrar el DataFrame por el año especificado
        year = st.selectbox('Selecciona un año:', valores_unicos3)
        result_df = df3[df3['year'] == year]
        response_data3 = [{"Puesto 1": result_df.iloc[0]['name']},
                        {"Puesto 2": result_df.iloc[1]['name']},
                        {"Puesto 3": result_df.iloc[2]['name']}]
        #st.write(response_data)
        
with columna3:
    try:
        if response_data3 is not None:
            st.title("Top 3 Puestos")
            st.subheader(f"1. {response_data3[0]['Puesto 1']}")
            st.write(f"2. {response_data3[1]['Puesto 2']}")
            st.write(f"3. {response_data3[2]['Puesto 3']}")
            #st.write(response_data)
            #formatted_text = "<h3>{}</h3>".format(response_data)
            #st.markdown(formatted_text, unsafe_allow_html=True)
    except NameError:
        
        st.write("Aguardando Seleccion.")

columna1, columna2, columna3  = st.columns(3)
with columna1:
    ''' ### Endpoint 4 
    Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.'''
with columna2:
    if st.checkbox('EndPoint4', value=False):
        df4 = pd.read_csv('UsersWorstDeveloper.csv')
        # Filtrar el DataFrame por el año especificado
        valores_unicos3 = df4['year'].unique()
        year = st.selectbox('Selecciona un año:', valores_unicos3)
        result_df = df4[df4['year'] == year]
        response_data4 = [{"Puesto 1": result_df.iloc[0]['developer']},
                            {"Puesto 2": result_df.iloc[1]['developer']},
                            {"Puesto 3": result_df.iloc[2]['developer']}]
            
        #st.write(response_data)
with columna3:
    try:
        if response_data4 is not None:
            st.title("Top 3 Puestos Menos Recomendados")
            st.subheader(f"1. {response_data4[0]['Puesto 1']}")
            st.write(f"2. {response_data4[1]['Puesto 2']}")
            st.write(f"3. {response_data4[2]['Puesto 3']}")
    except NameError:
        st.write("Aguardando Seleccion.")

columna1, columna2, columna3  = st.columns(3)

with columna1:
    
    ''' ### Endpoint 5
    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
    '''
with columna2:
    if st.checkbox('EndPoint5', value=False):
        df5 = pd.read_csv('sentiment_analysis.csv')

        valores_unicos5 = df5['developer'].unique()
        # Filtrar el DataFrame por el año especificado
        empresa_desarrolladora = st.selectbox('Empresa Desarrolladora:', valores_unicos5)
            # Filtrar por la empresa desarrolladora
        result_df = df5[df5['developer'] == empresa_desarrolladora]
            # Convertir a formato de diccionario
        response_data5 = result_df.set_index('developer').to_dict(orient='index')
        #st.write(response_data5)
with columna3:
    try:
        st.write(response_data5)
    except NameError:
        st.write("Aguardando Seleccion.")

columna1, columna2, columna3  = st.columns(3)
with columna1:
    ''' ### ML
    ### Recomendación item-item
    '''
with columna2:
    if st.checkbox('EndPointML', value=False):
        df6 = pd.read_csv('recomienda_item_item.csv')
        valores_unicos6 = df6['item_id'].unique()
        item_id = st.selectbox('Item Id:', valores_unicos6)
        # Filtrar el DataFrame por el año especificado
        result_df = df6[df6['item_id'] == item_id]
        response_data6 = result_df['Recomendaciones']
        #st.write(response_data6)
with columna3:
    try:
        st.write(response_data6)
    except NameError:
        st.write("Aguardando Seleccion.")