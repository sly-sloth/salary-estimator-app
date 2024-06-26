import streamlit as st


def show_about_page():
    st.title("About")

    
    st.write("""
        ## What the app does? 
""")
    
    # st.markdown(body="""
    #     The app utilizes the power of machine learning in order to predict the salary of a Software Developer given various parameters such as experience, education etc."""  
    # )

    st.markdown('''
                <style>
                    .big-font {
                        font-size:19px !important;
                        font-style:italic;
                    }
                </style>

                <span class="big-font">
                The app utilizes the power of machine learning in order to predict the salary of a Software Developer given various parameters such as experience, education etc. and then calculates the salary based on those parameters. Finally, outputs the estimated result.
                <br>
                <br>
                The model behind it is trained on the Stack Overflow Developer Survey 2023, hence the latest data. The model also converts the salary to native currency using real time exchange rates.
                </span>
                ''', 
                unsafe_allow_html=True)
    

    st.divider()

    st.caption('''
                <style>
                    .caption {
                    }
                </style>

                <span class="caption">
                Created by <strong><a href="https://slysloth-portfolio.netlify.app/">SlySloth</a></strong>
                </span>
                ''', 
                unsafe_allow_html=True)
    
    
    # img = st.image("favicon.png")

    # st.logo(icon_image=img)
    

