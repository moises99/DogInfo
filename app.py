import streamlit as st

#Rotas das paginas
pg = st.navigation([
        st.Page('./pages/homepage.py', title='Dogs disponiveis'),        
                   ],
        position="top"
        )

pg.run()