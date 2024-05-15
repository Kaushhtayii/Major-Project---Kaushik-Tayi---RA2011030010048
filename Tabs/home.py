"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Alzheimer Stage Detector based on EEG Biomarkers")

    # Add image to the home page
    st.image("./images/home.jpeg")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Alzheimer's disease progresses through several stages, each with distinct characteristics and symptoms. Broadly, it's categorized into three main stages: <u>early</u>, <u>middle</u>, and <u>late</u> stages.

1. **Early Stage:**
   - Mild cognitive decline characterized by subtle memory lapses and challenges in recalling familiar words or names.
   - Individuals may experience difficulty in organizing thoughts or planning tasks.
   - These symptoms might not be immediately noticeable, but close friends or family might observe subtle changes in behavior or memory.

2. **Middle Stage:**
   - Moderate cognitive decline becomes more apparent.
   - Memory loss intensifies; individuals may struggle with recognizing friends or family members, and confusion about time and place might arise.
   - Difficulty with basic tasks like dressing or personal hygiene might become noticeable.
   - Changes in behavior and personality might occur, such as wandering or agitation.

3. **Late Stage:**
   - Severe cognitive decline leading to an inability to communicate effectively.
   - Individuals might require assistance with daily activities and personal care.
   - Loss of physical abilities, difficulty swallowing, and increased vulnerability to infections are common.
   - Complete dependence on caregivers for basic needs becomes the norm.

    

    """, unsafe_allow_html=True)
    with st.expander('Mathematical Formula for Alzheimer Detection'):
      st.subheader('Mathematical Formula for Alzheimer Detection')
      st.image('images/formula.png')
      st.image('images/formula-2.png')

      st.markdown('''Alzheimer's disease is a complex neurological disorder characterized by progressive cognitive decline, memory loss, and behavioral changes. While there isn't a single mathematical model that fully captures all aspects of Alzheimer's disease, researchers have developed various models to understand its underlying mechanisms and progression. Here, I'll outline some key components and concepts often included in mathematical models of Alzheimer's disease:

1. **Neurodegeneration**: Alzheimer's disease is associated with the accumulation of abnormal protein aggregates, such as beta-amyloid plaques and tau tangles, in the brain. Mathematical models may represent the dynamics of these protein aggregates, their formation, clearance, and spread throughout the brain.

2. **Cellular Processes**: Models may incorporate cellular processes involved in Alzheimer's disease, such as synaptic dysfunction, neuronal loss, inflammation, oxidative stress, and mitochondrial dysfunction. These processes can be represented using differential equations or other mathematical formulations.

3. **Genetics and Risk Factors**: Genetic factors, such as mutations in genes like APP, PSEN1, and PSEN2, play a role in Alzheimer's disease risk. Mathematical models may include genetic components to explore how different genetic variants influence disease onset and progression. Additionally, models may consider other risk factors like age, lifestyle, and environmental factors.

4. **Network Dynamics**: The brain is a complex network of interconnected neurons, and Alzheimer's disease disrupts this network. Mathematical models may represent brain networks and their connectivity patterns to study how network dynamics are altered in Alzheimer's disease and how these changes contribute to cognitive decline.

5. **Clinical Progression**: Alzheimer's disease progresses through stages, starting with mild cognitive impairment (MCI) and progressing to dementia. Mathematical models may simulate disease progression over time, capturing the transition between different disease stages and the associated changes in cognitive function.

6. **Therapeutic Interventions**: Mathematical models can be used to evaluate the efficacy of potential therapeutic interventions for Alzheimer's disease, such as drugs targeting beta-amyloid or tau, cognitive training programs, lifestyle interventions, or combinations of treatments. Models can simulate the effects of these interventions on disease progression and cognitive outcomes.

Overall, mathematical models provide a valuable tool for understanding the complex dynamics of Alzheimer's disease, exploring potential mechanisms, and guiding the development of new diagnostic tools and therapeutic strategies. However, it's important to note that Alzheimer's disease is a multifactorial condition with many unknowns, and mathematical models are simplifications of the underlying biological processes. Therefore, while models can provide insights and predictions, they must be interpreted in the context of experimental data and clinical observations.''')