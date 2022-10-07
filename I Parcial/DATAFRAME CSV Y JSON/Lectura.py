#!/usr/bin/env python
# coding: utf-8

# In[253]:


import pandas as pd
universidad = pd.read_csv("Info_Academica.csv")


# In[254]:


estudiantes = pd.read_json("Info_Estudiante.json")


# In[255]:


dm = pd.merge(estudiantes, universidad, on = ["asignatura", "asignatura"])


# In[221]:


#1 Clase con mayor numero de reprobados en el primer periodo del 2022
clases_con_reprobados = dm[['asignatura', 'periodo', 'fecha']][dm.nota < 65]
clases_con_reprobados_2022 = clases_con_reprobados[['asignatura', 'periodo']][clases_con_reprobados.fecha > '01/01/2022']
clases_con_reprobados_1 = clases_con_reprobados_2022[clases_con_reprobados_2022.periodo == 1]
clase = clases_con_reprobados_1.groupby(['asignatura'])[['asignatura']].count()
clase['asignatura'].idxmax()


# In[227]:


#2 Clase con mayor numero de aprobados en el tercer periodo del año 2022
clases_con_aprobados = dm[['asignatura', 'periodo', 'fecha']][dm.nota >= 65]
clases_con_aprobados_2022 = clases_con_aprobados[['asignatura', 'periodo']][clases_con_aprobados.fecha > '01/01/2022']
clases_con_aprobados_3 = clases_con_aprobados_2022[clases_con_aprobados_2022.periodo == 3]
clase = clases_con_aprobados_3.groupby(['asignatura'])[['asignatura']].count()
clase['asignatura'].idxmax()


# In[252]:


#3 Alumnos con calificaciones mas altas en el segundo periodo
alumnos = dm[['nombre', 'asignatura' ,'nota']][dm.periodo == 2]
alumnos_notas_altas = alumnos[alumnos.nota == alumnos.nota.max()]
alumnos_notas_altas


# In[ ]:




