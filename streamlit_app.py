import streamlit as st
import pandas as pd
import plotly.express as px

# Muestra el título y descripción
st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Recoge los datos de los empleados desde el csv
employees = pd.read_csv("employees.csv")

# Muestra los datos de los empleados en una tabla
st.dataframe(employees)

# Crea una línea horizontal de separación
st.markdown("""---""")

# Creamos el selector de colores
color = st.color_picker("Elige un color para las barras", "#3475B3")

# Creamos el checkbox para mostrar el nombre y sueldo
show_name = st.toggle("Mostrar el nombre", value=True)
show_salary = st.toggle("Mostrar sueldo en la barra")

# Creamos la gráfica que muestra los datos de los empleados
fig = px.bar(
        employees,
        x="salary",
        y="full name" if show_name else None,
        orientation="h",
        color_discrete_sequence=[color],
        text="salary" if show_salary else None
)
fig.update_traces(
    textposition="outside",  # Asegura que el texto del salario esté fuera de la barra
    textfont=dict(size=18)
)
fig.update_layout(
    xaxis_title="Sueldo",
    yaxis_title="Nombre completo" if show_name else "",
    template="simple_white"
)
st.plotly_chart(fig)

# Muestra el nombre del desarrollador y el centro
st.write("© Jairo Andrades Bueno - CPIFP Alan Turing")
